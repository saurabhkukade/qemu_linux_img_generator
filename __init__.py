"""Main awds"""
import ConfigParser
import sys
import generate_debian_img

CONF = ConfigParser.ConfigParser()
CONF.read(sys.argv[1])
SECTION_LIST = CONF.sections()
SERVER_LIST = [section for section in SECTION_LIST if section != 'generic']

def fetch_param(server):
    """Fetch all param for given section"""
    return map (lambda x: x[1], CONF.items(server))

def gen_generic_qemu_linux_img():
    """Generate gen qemu linux image"""
    if 'generic' in SECTION_LIST:
        img_path = CONF.get('generic', 'img_path')
        img_name = CONF.get('generic', 'img_name')
        img_size = CONF.get('generic', 'img_size')
        generate_debian_img.create_generic_linux_disk_img(img_path, img_name, img_size)
        return img_path + "/" + img_name

def gen_server_qemu_linux_img(genr_image_path):
    """Generate server linux qemu images"""
    for server in SERVER_LIST:
        args = fetch_param(server)
        generate_debian_img.replicate_linux_image(genr_image_path, args[0], args[1])
def main():
    '''Main function'''
    genr_image_path = gen_generic_qemu_linux_img()
    gen_server_qemu_linux_img(genr_image_path)

main()
