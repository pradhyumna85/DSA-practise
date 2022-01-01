def pow(num,power):
    assert power>=0 and  power == int(power), 'Power must be a +ve integer only'
    if power==1: ## or power==0
        return num ## return 1
    else:
        return num * pow(num,power-1)

if __name__ == '__main__':
    x,p = 2,8
    print(f'{x}^{p}=',pow(x,p))