import sys
import re

filename = sys.argv[1]
output = ''
with open(filename) as f:
    for line in f:
        if line.startswith('\\[') or line.startswith('\\]'):
            output += '\n$$\n'
        elif not line.startswith('\\'):
            if line.startswith('\n'):
                output += line
            else:
                output += re.sub(r'\\textit\{.*?\}', r'$$\g<0>$$', line[:-1].replace('$','$$')) + ' '
print(output)