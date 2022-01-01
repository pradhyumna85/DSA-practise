def findPairs(arr,num): ## O(n^2) time and O(1) space
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]: ## skip same number pairs
                continue
            elif (arr[i]+arr[j]) == num:
                return i,j ## stop at first solution

    return None

def findPairs_dict(arr,num): ## O(n) avg (worst O(n^2)) time and O(n) space
    set_nums = set(arr) ## O(1) time and O(n) space
    index_map = {key:val for val,key in enumerate(arr)} ## O(n) time and space
    indexes = [None,None]

    for n in set_nums:
        if num-n in set_nums and num-n != n: ## skip same number case: ## O(n) avg (worst O(n^2))
            indexes[0], indexes[1] = index_map[n], index_map[num-n]
            break
    
    if not indexes[0]:
        return None
    else:
        indexes.sort() ## O(1) as only 2 elements everytime
        return indexes

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(f'nums: {nums} | target: {target}')
    print(findPairs(nums,target))

    print('###############')

    nums = [3,2,4]
    target = 6
    print(f'nums: {nums} | target: {target}')
    print(findPairs(nums,target))

    print('###############')

    nums = [3,3]
    target = 6
    print(f'nums: {nums} | target: {target}')
    print(findPairs(nums,target))

    print('###############')

    nums = [2,1,11,3,7,4,3,15]
    target = 6
    print(f'nums: {nums} | target: {target}')
    print(findPairs_dict(nums,target))

    print('###############')


    # ## last element check
    # print(list(range(4,4)))