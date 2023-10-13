import os
print(dir(os))

print(help(os))

import shutil
shutil.copyfile('data.db', 'archive.db')

shutil.move('/build/executables', 'installdir')