import time
import matplotlib.pyplot as plt

def fibo_loop(n):
    last_num = 0
    summ = 0
    for i in range(n):
        if i in [0,1]:
            curr = i
            continue
        if i==2:
            summ = 0 + 1
            last_num = 1
            curr = summ
            continue

        summ = curr + last_num
        last_num = curr
        curr = summ

    return curr


rec_depth = 0
verbose = False

def fibo(n):
    global rec_depth
    rec_depth += 1
    if verbose:
        print('rec depth: ',rec_depth)
    assert n>0 ## checking n is +ve
    assert n == int(n) ## checking n is int
    if n in [1,2]:
        return 0 if n==1 else 1

    return fibo(n-1) + fibo(n-2)

if __name__ == '__main__':
    n = 10
    t1 = time.time()
    print(f'{n}th fibo num: ',fibo(n))
    time_taken = time.time() - t1
    print('max function calls: ',rec_depth)
    print('time taken in seconds: ',round(time_taken,2))
    print(f'\n\n{n}th fibo num by for loop: ',fibo_loop(n))

    # print('------- Time complexity analysis -------')
    # x = [] ## n
    # y = [] ## seconds
    # z = [] ## recursion calls
    # max_n = 42 ## 42 has ~540 million function calls and takes around ~3 minutes
    # for i in range(max_n):
    #     rec_depth = 0
    #     print('running recurson case, n = ',i+1,end='')
    #     x.append(i)
    #     t1 = time.time()
    #     res = fibo(i+1)
    #     time_taken = time.time() - t1
    #     print(', Recursion calls: ',rec_depth)
    #     y.append(time_taken)
    #     z.append(rec_depth)
    #     print('-------------------------')

    # print('n: ',x)
    # print('time (s): ',y)
    # print('n calls: ',z)

    # plt.figure(figsize=(6,6))
    # plt.plot(x,y)
    # plt.xlabel('nth fibo num')
    # plt.ylabel('time taken in seconds')
    # plt.title('Fibo recursion time complexity')
    # plt.savefig('fibo_recursion_time_scaling.jpg',dpi=300)
    # # plt.show()