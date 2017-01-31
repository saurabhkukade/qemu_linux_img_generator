"""Script to setup prerequisites pacakages and tools"""

#!/usr/bin/python
import os
import subprocess

def run_cmd(command):
    '''Run commands on shell, one by one'''
    print command
    subprocess.call(command, shell=True)


def create_generic_linux_disk_img(img_path, img_name, img_size):
    """Creates generic linux qemu img"""
    img_path = create_blank_disk_image(img_path, img_name, img_size)


def create_blank_disk_image(dest_disk_path, disk_name, disk_size):
    """Creates blank disk image for qemu return image path"""
    path = dest_disk_path + "/" + disk_name
    if os.path.isfile(path):
        print "gerneric image found, Not creating one.", path
        return

    if not os.path.isdir(dest_disk_path):
        os.makedirs(dest_disk_path)

    cmd = "qemu-img create -f qcow2 %s/%s.img %s" % (dest_disk_path, disk_name, disk_size)
    run_cmd(cmd)
    return dest_disk_path + "/" + disk_name + ".img"


def replicate_linux_image(genr_image_path, dest_disk_path, disk_name):
    """Make a copy of generic image to desired image"""
    if not os.path.isfile(genr_image_path):
        print "gerneric image not found, creating one."
        return

    if not os.path.isdir(dest_disk_path):
        os.makedirs(dest_disk_path)
    cmd = "cp  %s %s/%s " % (genr_image_path, dest_disk_path, disk_name)
    run_cmd(cmd)
    return dest_disk_path

def install_minimal_debian(disk_img_path, iso_path):
    """Boots minimal deb iso and install it on qemu img"""

    cmd = "qemu-system-x86_64 -m 256 -hda %s -cdrom %s " % (disk_img_path, iso_path)
    run_cmd(cmd)


#create_generic_linux_disk_img()
#replicate_linux_image("qemu_images/generic_linux.img", "qemu_images", "websrv.img")
# IMG_PATH = create_blank_disk_image(sys.argv[1], sys.argv[2], sys.argv[3])
# install_minimal_debian(IMG_PATH, sys.argv[4])
