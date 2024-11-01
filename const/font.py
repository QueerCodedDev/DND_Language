import csv

font = {}
# Load csv font data
with open('font.csv', newline='') as csvfile:
    buffer = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in buffer:
        font[row[0]] = row[1]

# Load special character font data
font_special = {
    ' ': '',
    '.': 'WA:AD:WS',
    ',': 'WA:AD:WD:WS',
    ':': 'WA:AD:DS:SW',
    ';': 'WA:AS:AD:WS',
    '+': 'AD:DW:WS',
    '-': 'WS:SD:DW:AD',
    '*': 'WS:SA:AD:DW',
    '/': 'WS:SA:AD:SD',
    '(': 'WS:AD',
    ')': 'WS:AD:AS',
    '=': 'WD:DS:SA:AW:WS:AD',
    '?': 'WA:AS:SD',
    '!': 'WA:WD:DS',
    '"': 'WD:WA:WS',
    '\'': 'WD:DS:SA'
}

# Add special characters to main list
font.update(font_special)
