import multiprocessing

from pymobiledevice3.lockdown import create_using_usbmux, LockdownClient
from pymobiledevice3.cli.remote import install_driver_if_required, select_device, RemoteServiceDiscoveryService, start_tunnel, verify_tunnel_imports
from pymobiledevice3.services.amfi import AmfiService
from pymobiledevice3.exceptions import NoDeviceConnectedError


def get_usbmux_lockdownclient():
    while True:
        try:
            lockdown = create_using_usbmux()
        except NoDeviceConnectedError:
            input("请连接设备后按回车...")
        else:
            break

    while lockdown.all_values.get("PasswordProtected"):
        input("请解锁设备后按回车...")

    return lockdown


def get_DeviceName(lockdown: LockdownClient):
    return lockdown.all_values.get("DeviceName")


def get_version(lockdown: LockdownClient):
    return lockdown.all_values.get("ProductVersion")


def get_developer_mode_status(lockdown: LockdownClient):
    return lockdown.developer_mode_status


def reveal_developer_mode(lockdown: LockdownClient):
    AmfiService(lockdown).create_amfi_show_override_path_file()


def enable_developer_mode(lockdown: LockdownClient):
    AmfiService(lockdown).enable_developer_mode()


def get_serverrsd():
    install_driver_if_required()
    if not verify_tunnel_imports():
        exit(1)
    return select_device(None)


async def tunnel(rsd: RemoteServiceDiscoveryService,
                 queue: multiprocessing.Queue):
    async with start_tunnel(rsd, None) as tunnel_result:
        queue.put((tunnel_result.address, tunnel_result.port))
        await tunnel_result.client.wait_closed()
