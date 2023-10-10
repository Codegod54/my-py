# Fancier Output formatting
'''year = 2016
event= 'Referendum'
print(f'Results of the {year} {event}')'''

# string.format()

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} Yes votes {:2.2%}'.format(yes_votes, percentage))