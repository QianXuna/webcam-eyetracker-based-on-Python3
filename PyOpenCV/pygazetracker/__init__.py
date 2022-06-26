import os
import sys # 即添加包名的搜索路径
sys.path.append("pygazetracker")

# # # # #
# CONSTANTS

# VERBOSITY
# 0 is errors only
# 1 is errors and warnings
# 2 is errors, warnings, and messages
# 3 is errors, warnings, messages, and debug info.
_VERBOSITY = 2

# DEBUG MODE
# In this mode, images of each step of the frame-processing are stored.
_DEBUG = False

# FILES AND FOLDERS
# Get the main directory

_DIR = os.path.abspath(os.path.dirname(__file__))
_DEBUGDIR = os.path.join(_DIR, 'DEBUG')
# Face detection cascade from:
# https://github.com/shantnu/FaceDetect
_FACECASCADE = os.path.join(_DIR, u'haarcascade_frontalface_default.xml')
# Eye detection cascade from:
# http://www-personal.umich.edu/~shameem/haarcascade_eye.html
_EYECASCADE = os.path.join(_DIR, u'haarcascade_eye.xml')