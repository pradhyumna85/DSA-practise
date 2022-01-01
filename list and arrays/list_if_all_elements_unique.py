def ifallunique(arr):
    if len(set(arr))==len(arr): ## O(1) time and O(n) space complexity
        return True
    else:
        return False

if __name__ == '__main__':
    arr = [1,3,6,2,5,4,7,89,0,9,10]

    print('nums: ',arr)
    print('All unique: ',ifallunique(arr))
    print('####################')

    arr.append(1)
    print('nums: ',arr)
    print('All unique: ',ifallunique(arr))
    print('####################')