import glob
for name in glob.glob('*[0-9]*.txt'):
    print(name)