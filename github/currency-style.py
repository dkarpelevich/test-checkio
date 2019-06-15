# https://py.checkio.org/mission/currency-style/publications/Sim0000/python-3/first/?ordering=most_voted&filtering=all

import re

def checkio(text):
    reform = lambda match: match.group(0).translate(str.maketrans(',.', '.,'))
    return re.sub('\$\d{1,3}(\.\d{3})*(,\d{2})?(?!\d)', reform, text)

# \$            letter '$'
# \d{1,3}       [0-9] of length {1, 3}
# (\.\d{3})*    repetation of \.[0-9]{3}, if exists
# (,\d{2}){,1}  ,[0-9]{2}, if exists
# (?!\d)        no [0-9] after pattern


if __name__ == '__main__':
    assert checkio("$1.234.567,89") == "$1,234,567.89", "1st Example"
    assert checkio("$0,89") == "$0.89", "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
           "Euro Style = $12,345.67, US Style = $12,345.67", "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
           "Us Style = $12,345.67, Euro Style = $12,345.67", "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
           "$1,234, $5,678 and $9", "Dollars without cents"
