def findMaxProd(arr): ## time O(n^2) and space O(1)
    max_prod = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            prod = arr[i] * arr[j]
            if prod>max_prod:
                max_prod = prod
                indexes = (i,j)
    return {'max_prod':max_prod,"indexes":indexes}

def findMaxProd_dict(arr): ## time O(n+nlogn)~O(n) and space O(n)

    index_map = {key:val for val,key in enumerate(arr)} ## O(n) time and space

    sorted_arr = sorted(arr) ## O(nlogn) time

    max_prod = sorted_arr[-1] * sorted_arr[-2]

    indexes = (index_map[sorted_arr[-1]],index_map[sorted_arr[-2]])

    return {'max_prod':max_prod,"indexes":indexes}


def find_max_prod(arr): ## O(n) time and o(1) space

    assert len(arr)>1, "The array should be atleast 2 elements"

    max1 = arr[0]
    max2 = 0

    indexes = [None,None]

    for i in range(len(arr)):  ## O(n) 
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]      
            indexes[0] = i

        elif arr[i] > max2 and arr[i] < max1:
            max2 = arr[i]
            indexes[1] = i

    max_prod = max1*max2
    indexes.sort() ## O(1) as always 2 elements

    return {'max_prod':max_prod,"indexes":indexes}

if __name__ == '__main__':
    # nums = [20,1,0,2,7,11,18,15]
    # print(f'nums: {nums}')
    # print(findMaxProd(nums))

    # print('###############')

    # print(f'nums: {nums}')
    # print(findMaxProd_dict(nums))

    # print('###############')

    nums = [20,1,0,2,7,11,18,15]
    print(f'nums: {nums}')
    print(find_max_prod(nums))

    print('###############')