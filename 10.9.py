# Data Compression

import zlib
s = b'witch which has which witches wrist watch'
print(len(s))


t = zlib.compress(s)
print(t)
print(len(t))

u = zlib.decompress(t)
print(u)
print(len(u))

print(zlib.crc32(s))
