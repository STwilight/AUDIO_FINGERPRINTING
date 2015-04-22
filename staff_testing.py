line_number = 1
with open('user-agent.list', 'r') as f:
    i = 0
    for line in f:
        i += 1
    print (i)
    '''
    if line_number > i+1:
        print ('Number is too big!')
        f.close()
        exit()
    else:
        tmp = f.readlines()[line_number-1]
        f.close()
    if '\n' in tmp:
        tmp = tmp.replace('\n', '')
    elif '\r' in tmp:
        tmp = tmp.replace('\r', '')
    print(tmp)
        '''