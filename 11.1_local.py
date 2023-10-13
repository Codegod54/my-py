
"""
The locale module accesses a database of culture specific data formats. The grouping attribute of locale’s format function provides a direct way of formatting numbers with group separators:
"""

import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')

conv = locale.localeconv()                  # get a mappijnng of conventions
x = 1234567.8
print(locale.format("%d", x, grouping = True))

print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping = True))
