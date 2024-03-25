import sys

from pymobiledevice3.services.mobile_image_mounter import auto_mount, DeveloperDiskImageMounter
from pymobiledevice3.exceptions import NotMountedError, AlreadyMountedError, DeveloperDiskImageNotFoundError


def mount_image(lockdown):
    try:
        auto_mount(lockdown)
    except AlreadyMountedError:
        print('DeveloperDiskImage already mounted')
    except DeveloperDiskImageNotFoundError:
        print('DeveloperDiskImage not found')
        sys.exit("Program terminated due to error")


def unmount_image(lockdown):
    try:
        DeveloperDiskImageMounter(lockdown).umount()
    except NotMountedError:
        print('Developer image isn\'t currently mounted')
