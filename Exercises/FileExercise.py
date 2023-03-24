fh = open('mbox.txt')

for lx in fh:
    print(lx.upper().rstrip())
