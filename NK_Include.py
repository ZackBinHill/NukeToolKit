# -*- coding: utf-8 -*-
# import system modules
import os
import sys
import platform
import time
import logging
import math
import random
import glob 
import re
import cPickle as pickle 

try:
    import pwd
except Exception,e:
    sys.stderr.write('LOG:  '+str(e)+'\n')
    sys.stderr.flush()

import stat 
import threading
import thread
import subprocess
import shutil
import getpass
from pprint import pprint
import traceback

# import nuke api
try:
    import nuke
except Exception,e:
    sys.stderr.write('LOG:  '+str(e)+'\n')
    sys.stderr.flush()

try:
    import nukescripts 
except Exception,e:
    sys.stderr.write('LOG:  '+str(e)+'\n')
    sys.stderr.flush()

# import third party modules
try:
    import numpy as np  
except Exception,e:
    sys.stderr.write('LOG:  '+str(e)+'\n')
    sys.stderr.flush()

