"""The string module includes a versatile Template class with a simplified syntax suitable for editing by end-users. This allows users to customize their applications without having to alter the application."""

from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village = 'Nottingham', cause = 'the ditch fund'))
t = Template('Return the $item to $owner.')
d = dict(item = 'unladen swallow')
print(t.substitute(d))


print(t.safe_substitute(d))



import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimeter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')
print(fmt)
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext =os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename,newname))


    