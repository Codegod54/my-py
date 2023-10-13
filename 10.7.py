# internet Access
"""There are a number of modules for accessing the internet and processing internet protocols. Two of the simplest are urllib.request for retrieving data from URLs and smtplib for sending mail:"""

from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')                     # Decodinggg the binary dsata to text.
        if 'EST' in line or 'EDT' in line:              # Look foor Eastern Time
            print(line)


import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org', 
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")

server.quit()

# Note that the second example needs a mailserver running on localhost.