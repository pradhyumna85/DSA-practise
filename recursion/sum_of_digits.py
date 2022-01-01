def sod_loop(num):
    assert num>0 ## checking n is +ve
    assert num == int(num) ## checking n is int
    summ = 0
    while True:
        rem = num % 10
        summ += rem
        num//=10
        if num==0:
            break
    return summ
    
def sod_rec(num):
    assert num>=0 and  num == int(num) ## checking n is a +ve integer
    if num==0:
        return 0
    else:
        return num%10 + sod_rec(num//10)

if __name__ == '__main__':
    x = 131
    print('number: ',x)
    print('sod by loop: ',sod_loop(x))
    print('sod by recu: ', sod_rec(x))