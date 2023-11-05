# Operating Syatem Interface
"""The os module provides dozens of functions for interacting with the operating system:"""

import os
print(os.getcwd())                                  # Return the current working directory

os.chdir('/server/accesslogs')                      # Change current working directory
os.system('mkdir today')                            # Run the command mkdir in the system shell
