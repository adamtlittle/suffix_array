with open ('/home/squee/Dropbox/OHSU/compbio/suffix/Test_Text.txt') as file:

    lines = []

    for line in file:
        lines.append(line.rstrip())


    no_lines = ''.join(lines)

    for char in no_lines[:]:
        if char == ' ':
            char = char.replace(' ', '_')
        else:
            next

    char_set = set(no_lines)

print(char_set)

appendix = [str(len(no_lines)) + ':$']

for i in range(len(no_lines), 0, -1):
    appendix.append(str(i-1) + ':' + no_lines[i-1:] + '$')


with open ('/home/squee/Dropbox/OHSU/compbio/suffix/output.txt', 'w') as output:
    for item in appendix:
        output.write(item + '\n')


appendix.sort()
print(appendix[9001])

# Next make into dictionary with key index position, and value as suffix
