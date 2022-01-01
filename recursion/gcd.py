import math
def gcd(a,b):
    assert a==int(a) and b==int(b), 'The number must be integers only!'
    if a<0:
        a = -1 * a ## gcd of +ve num == gcd of -ve num
    if b<0:
        b = -1 * b ## gcd of +ve num == gcd of -ve num
    if a==0: ## 0 remainder
        return b ## gcd
    else:
        return gcd(b%a,a) ## if b%a then a, if a%b then b -> also change the remainder condition accordingly

if __name__ == '__main__':
    a,b = 48,18
    print(f'gcd({a},{b})=',gcd(a,b))
    a,b = -48,18
    print(f'gcd({a},{b})=',gcd(a,b))
    a,b = -48,-18
    print(f'gcd({a},{b})=',gcd(a,b))
    a,b = -18,-48
    print(f'gcd({a},{b})=',gcd(a,b))