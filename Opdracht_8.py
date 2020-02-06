def compress(filename):
    fileUncompressed = open(filename, 'r')
    fileCompressed = open(('compressed_' + filename), 'w+')

    fileLines = fileUncompressed.readlines()
    for line in fileLines:
        compressLine = line.strip()
        if compressLine != '':
            fileCompressed.write(compressLine + '\n')


compress('Opdracht_8')

