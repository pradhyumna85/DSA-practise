def dec2bin_int(num):
    assert num==int(num), 'The number must be integers only!'
    if num==0:
        return 0
    else:
    ## return remainder + dec2bin(quotient)*10
        return num%2 + dec2bin_int(int(num/2))*10 ## don't use floor division // here as it will interpret example: -6.5 as -7 instead of -6

def dec2bin(num):
    out = dec2bin_int(num)
    if num<0: ## for -ve number time complexity of len(str(out)) -> O(n)
        out = str(out)
        transTable = out.maketrans("10", "01")
        out = out.translate(transTable).lstrip('0') ## interchange 1 and 0 s -> compliment
        max_len = len(out)
        add = '1'.zfill(max_len)

        # Initialize the result and do binary addition with out and 1
        result = ''
        
        # Initialize the carry
        carry = 0
        
        # Traverse the string
        for i in range(max_len - 1, -1, -1):
            r = carry
            r += 1 if out[i] == '1' else 0
            r += 1 if add[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result
        
            # Compute the carry.
            carry = 0 if r < 2 else 1
        
        if carry != 0:
            result = '1' + result

        return int(result)
    else:
        return out


if __name__=='__main__':
    num = 4
    print(f'{num}-base-10 = {dec2bin(num)}-base-2')
    num = 13
    print(f'{num}-base-10 = {dec2bin(num)}-base-2')
    num = -13
    print(f'{num}-base-10 = {dec2bin(num)}-base-2')
    num = 10
    print(f'{num}-base-10 = {dec2bin(num)}-base-2')
    num = -10
    print(f'{num}-base-10 = {dec2bin(num)}-base-2')
