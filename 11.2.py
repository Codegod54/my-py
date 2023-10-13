"""The string module includes a versatile Template class with a simplified syntax suitable for editing by end-users. This allows users to customize their applications without having to alter the application."""

from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village = 'Nottingham', cause = 'the ditch fund'))

t = Template('Return the $item to $owner.')
d = dict(item = 'unladen swallow')
print(t.substitute(d))


print(t.safe_substitute(d))