# -*- coding: utf-8 -*-
# import
from NK_Include import *


# system platform
if platform.platform().startswith('Linux'):
    PLATEFORM = 'linux'
elif platform.platform().startswith('Darwin'):
    PLATEFORM = 'mac'
elif platform.platform().startswith('Window'):
    PLATEFORM = 'win'


# osOpen
def osOpen(path):
    if PLATFORM == 'linux':
        os.system('gnome-open %s' % path)
    elif PLATFORM == 'mac':
        os.system('open %s' % path)
    elif PLATFORM == 'win':
        path = path.replace('/', '\\')
        subprocess.Popen('explorer %s' % path)
    else:
        logging.info('platform_Error')


# SHOW_PATH
if PLATEFORM == 'linux':
    ZACK_PATH_f = '/zack_file'
    ZACK_PATH_i = '/zack_image'
if PLATEFORM == 'mac':
    ZACK_PATH_f = '/zack_file'
    ZACK_PATH_i = '/zack_image'
if PLATEFORM == 'win':
    ZACK_PATH_f = 'Y:\\zack_file'
    ZACK_PATH_i = 'W:\\zack_image'

ZACK_FILE_SEVER = ZACK_PATH_f
ZACK_IMAGE_SEVER = ZACK_PATH_i


# defined nuke plugin path
def NUKE_PLUGIN_PATH_(*argv):
    pass
ZACK_PLUGIN_PATH = NUKE_PLUGIN_PATH_


# sys and nuke cmd
opj = os.path.join
opb = os.path.basename
opd = os.path.dirname

try:
    nm = nuke.message
    nask = nuke.ask
    ntprint = nuke.tprint
except NameError,e:
    logging.info(e)


# get username
def USERNAME_():
    userName = ''
    try:
        userName = nuke.toNode('preferences')['pref_login_name'].getValue()
    except NameError,e:
        logging.info(e)
        pass
    if not userName:
        userName = getpass.getuser()
    if not userName:
        userName = os.environ.get('LOGNAME')
    if not userName:
        userName = ''
    return userName

# get show plugin path
def GET_SHOW_PLUGIN_PATH(show, *argv):
    path = opj(ZACK_FILE_SEVER, 'PLE', 'show', show, 'app', 'nuke')

    for p in argv:
        path = opj(path, p)
    return path

if __name__ == '__main__':
    logging.info(str(GET_SHOW_PLUGIN_PATH('ZZZ', 'nuke......')))








