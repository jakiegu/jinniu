import os,glob
filenames = glob.glob('*.pp')
for filename in filenames:
    if filename.endswith('.pp'):
        os.remove(filename)




