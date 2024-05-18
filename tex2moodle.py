import sys

filename = sys.argv[1]
output = '<p>'
with open(filename, encoding='utf-8') as f:
    for line in f:
        if line.startswith('\\['):
            output += '\n\n$$'
        if line.startswith('\\]'):
            output += '$$\n\n'
        elif not line.startswith('\\'):
            if line.startswith('\n'):
                output += '</p>\n<p>'
            else:
                output += line[:-1].replace('$','$$') \
                            .replace('``','&ldquo;') \
                            .replace("''",'&rdquo;') \
                            .replace('---','&mdash;') \
                            .replace('--','&ndash;')
print(output + '</p>')