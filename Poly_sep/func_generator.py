import os

path = os.path.dirname(os.path.realpath(__file__))+ '\\' + 'catalog.txt'
path_out = os.path.dirname(os.path.realpath(__file__))+ '\\' + 'functions.txt'
with open(path, 'r') as func_catalog, open (path_out, 'w') as out:
    correct = ''
    lines = func_catalog.readlines()
    n = len(lines)
    for i in range(n):
        if not lines[i].isspace():
            if i != 0 and lines[i].startswith('#'):
                correct = correct.split('f')[1].strip(';') + correct.split('f')[0].rstrip(';')
                out.write(correct + '\n')
                correct =''
            correct += lines[i].replace('\n',';')
    correct += lines[n - 1].replace('\n',';')
    correct = correct.split('f')[1].strip(';') + correct.split('f')[0].rstrip(';')
    out.write(correct)


