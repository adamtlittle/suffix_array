with open ('/home/squee/Dropbox/OHSU/compbio/suffix/Test_Text.txt') as file:

    lines = []

    for line in file:
        lines.append(line.rstrip())


    no_lines = ''.join(lines)

    backwards = ''
    for char in no_lines[::-1]:
        if char == ' ':
            char = char.replace(' ', '_')
            backwards = backwards + char
        else:
            backwards = backwards + char

    print(backwards)

appendix = []

index = 1
for i in range(0, len(backwards)):
    appendix.append(backwards[i:i+index])
    index += 1

print(appendix)


# Next make into dictionary with key index position, and value as suffix
