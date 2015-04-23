line_number = 0
patch = 'user-agent.list'
i = 0
f = open(patch, 'r')
for line in f:
    i += 1
f.close()
if line_number > i-1:
    print ('Line number is too big!')
    exit()
else:
    f = open(patch, 'r')
    tmp = f.readlines()[line_number]
    f.close()
    if '\n' in tmp:
        tmp = tmp.replace('\n', '')
    elif '\r' in tmp:
        tmp = tmp.replace('\r', '')
    print(tmp)