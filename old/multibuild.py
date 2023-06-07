#!/usr/bin/python3
from sphinx_multibuild import SphinxMultiBuilder
import logging
import time
import sys

# Package respects loglevel set by application. Info prints out change events
# in input directories and warning prints exception that occur during symlink
# creation/deletion.
loglevel = logging.INFO
logging.basicConfig(format='%(message)s', level=loglevel)

# You can register a handler that will be called when a symlink
# Can't be created or deleted.
def handle_autobuild_error(input_path, exception):
    pass

# Instantiate multi builder. The last two params are optional.
builder = SphinxMultiBuilder(# input directories
                             ["./", "./docs/"],
                             # Temp directory where symlinks are placed.
                             "./tmp",
                             # Output directory
                             "./docs/_build/sphinx",
                             # Sphinx arguments, this doesn't include the in-
                             # and output directory and filenames argments.
                             ["./docs"],
                             # Specific files to build(optional).
                             ["index.rst"],
                             # Callback that will be called when symlinking
                             # error occurs during autobuilding. (optional)
                             handle_autobuild_error)
# build once
builder.build()

# start autobuilding on change in any input directory until ctrl+c is pressed.
builder.start_autobuilding()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    builder.stop_autobuilding()

# return the last exit code sphinx build returned had as program exit code.
sys.exit(builder.get_last_exit_code())