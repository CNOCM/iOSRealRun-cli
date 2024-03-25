import os
import logging
import coloredlogs
from driver import location, connect, mount
from pymobiledevice3.cli.remote import RemoteServiceDiscoveryService
from pymobiledevice3.cli.developer import DvtSecureSocketProxyService
from init import init, route
import run
import config

debug = os.environ.get("DEBUG", False)

# Set logging level
coloredlogs.install(level=logging.INFO)
for logger_name in [
        'wintun', 'quic', 'asyncio', 'zeroconf', 'parso.cache',
        'parso.cache.pickle', 'parso.python.diff', 'humanfriendly.prompts',
        'blib2to3.pgen2.driver', 'urllib3.connectionpool'
]:
    logging.getLogger(logger_name).setLevel(
        logging.DEBUG if debug else logging.WARNING)


def main():
    # Set level
    logger = logging.getLogger(__name__)
    coloredlogs.install(level=logging.INFO)
    logger.setLevel(logging.INFO)
    if debug:
        logger.setLevel(logging.DEBUG)
        coloredlogs.install(level=logging.DEBUG)

    logger.info("Initialization started")

    DeviceName, version = init.init()

    logger.info(f"Connected to {DeviceName}")
    logger.info(f"iOS version: {version}")

    lockdown = connect.get_usbmux_lockdownclient()
    logger.info("Initialization done")

    loc = route.get_route(config.config.routeConfig)
    logger.info(f"Got route from {config.config.routeConfig}")
    if int(version.split(".")[0]) >= 17:
        process, address, port = init.start_tunnel_process(logger)

        with RemoteServiceDiscoveryService((address, port)) as rsd:
            with DvtSecureSocketProxyService(rsd) as dvt:
                try:
                    logger.info(
                        f"Simulation of running has started with speed around {config.config.v} m/s"
                    )
                    logger.info("Press Ctrl+C to exit")

                    run.run(dvt, version, loc, config.config.v)

                except KeyboardInterrupt:
                    logger.info("Received KeyboardInterrupt")
                    logger.info("Clearing location")
                    location.clear_location_17(dvt)
                    logger.info("Location cleared")

                finally:
                    process.terminate()
                    logger.info("Tunnel process terminated")
                    logger.info("Bye")

    else:
        logger.info("Starting to mount image")
        mount.mount_image(lockdown)
        logger.info(
            f"Simulation of running has started with speed around {config.config.v} m/s"
        )
        logger.info("Press Ctrl+C to exit")

        try:
            run.run(lockdown, version, loc, config.config.v)

        except KeyboardInterrupt:
            logger.info("Received KeyboardInterrupt")
            logger.info("Clearing location")
            location.clear_location(lockdown)
            logger.info("Location cleared")
        finally:
            mount.unmount_image(lockdown)
            logger.info("Image unmounted")
            logger.info("Bye")


if __name__ == "__main__":
    main()
