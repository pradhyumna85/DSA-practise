###### Solution start ######

def findmissingno(arr,n):
    '''
    Assumes only 1 missing integer (natural number)
    '''
    sn = (n*(n+1))/2
    arrsum = sum(arr) ## O(n)

    if sn==arrsum:
        print("No missing number")
        return None
    else: ## valid for only one missing number
        miss = int(sn-arrsum)
        print("Missing number: ",miss)
        return miss

if __name__=='__main__':
    n = 100

    ### Asume O(1) for creating of problem #######
    arr = [i for i in range(1,n+1)]

    ## delete one number
    arr.pop(8) ## 9

    res = findmissingno(arr,n)

    print('return val: ',res)


