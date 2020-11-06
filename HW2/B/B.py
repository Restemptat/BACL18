def solution(x):
    t = ''
    l = 0
    for i in range(len(x)):
        if x[i] == 'h':
            l+=1
            if l > 1 :
                x = x[:i] + 'H' + x[i+1:]
    for i in range(len(x)-1,0,-1):
        if x[i] == 'H':
            x = x[:i] + 'h' + x[i+1:]
            break
    for i in range(len(x)):
        if i % 3 != 0 or i == 0:
            t = t + x[i]
    t = t.replace('1','one')
    return(t)