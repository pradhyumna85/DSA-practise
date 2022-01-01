import sys
if __name__=='__main__':
    verbose = False
    n = 20
    last_num = 0
    summ = 0
    for i in range(n):
        if i in [0,1]:
            curr = i
            if verbose:
                print(f'{curr}, ',end='')
            continue
        if i==2:
            summ = 0 + 1
            last_num = 1
            curr = summ
            if verbose:
                print(f'{curr}, ',end='')
            continue

        summ = curr + last_num
        last_num = curr
        curr = summ
        if verbose:
            print(f'{curr}, ',end='')

    print(f'\n{n}th: {curr}')
    print('num size (MB): ',sys.getsizeof(curr)/(1024*1024))


    

    
