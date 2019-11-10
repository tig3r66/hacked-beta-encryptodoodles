def readtxt(filename):
    f = open(filename, 'r')
    if f.mode == 'r':
        contents = f.read()
        return contents