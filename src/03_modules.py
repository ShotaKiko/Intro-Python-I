"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(sys.argv)
print(sys.base_exec_prefix)
print(sys.base_prefix)
print(sys.byteorder)
print(sys.copyright)
print(sys.getwindowsversion)
print(sys.path)


# Print out the OS platform you're using:
# YOUR CODE HERE
print("PLATFORM", sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("VERSION", sys.version)
print("VERSION INFO", sys.version_info)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("PROCESS ID", os.getpid())


# Print the current working directory (cwd):
# YOUR CODE HERE
print("CURRENT WORKING DIRECTORY", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("MACHINE LOGIN NAME", os.getlogin())
