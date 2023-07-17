import psutil

def get_drives():
    drives = []
    for drive in psutil.disk_partitions():
        if 'cdrom' in drive.opts or drive.fstype == '':
            # Skip CD-ROM drives and drives with no file system type
            continue
        drives.append(drive.device)
    return drives