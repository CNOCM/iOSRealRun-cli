import sys
import ctypes
import os
import asyncio
import signal
import multiprocessing

from driver import connect


def check_admin_privilege():
    # check if root on macOS or Administrator on Windows
    if sys.platform == "win32":
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("请以管理员权限运行")
            return False
    elif sys.platform == "darwin":
        if os.geteuid() != 0:
            print("请以root权限运行")
            return False
    else:
        print("仅支持macOS和Windows")
        return False

    return True


def get_device_info(lockdown):
    DeviceName = connect.get_DeviceName(lockdown)
    version = connect.get_version(lockdown)
    developer_mode_status = False

    if int(version.split(".")[0]) >= 16:
        developer_mode_status = connect.get_developer_mode_status(lockdown)
        if not developer_mode_status:
            connect.reveal_developer_mode(lockdown)
            print(
                "您未开启开发者模式，请打开设备的 设置-隐私与安全性-开发者模式 来开启，开启后需要重启并输入密码，完成后再次运行此程序")
            sys.exit(1)

    return DeviceName, version


def tunnel_proc(queue: multiprocessing.Queue):
    server_rsd = connect.get_serverrsd()
    asyncio.run(connect.tunnel(server_rsd, queue))


def start_tunnel():
    # start the tunnel in another process
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=tunnel_proc, args=(queue, ))
    process.start()

    # get the address and port of the tunnel
    address, port = queue.get()

    return process, address, port


def start_tunnel_process(logger):
    logger.info("Starting tunnel")
    original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
    process, address, port = start_tunnel()
    signal.signal(signal.SIGINT, original_sigint_handler)
    logger.info(f"Tunnel started at address: {address}, port: {port}")
    return process, address, port


def init():
    if not check_admin_privilege():
        print("权限不足，无法继续执行")
        return None
    else:
        lockdown = connect.get_usbmux_lockdownclient()
        DeviceName, version = get_device_info(lockdown)
        return DeviceName, version


if __name__ == "__main__":
    init()
