from data_structures.stacks import stack

if __name__ == '__main__':
    stack_ = stack()
    print('printing stack after creation:')
    print(stack_)

    push_val = 5
    print(f'printing stack after pushing {push_val}:')
    stack_.Push(push_val)
    print(stack_)

    stack_.Push(10)
    stack_.Push(15)
    print('printing stack after pushing 10 and 15:')
    print(stack_)

    print("default Peek at Top of stack: ",stack_.Peek())
    print("Peek at bottom of stack: ",stack_.Peek(bottom=True))

    print("stack isEmpty?: ",stack_.isEmpty())
    print('Stack size: ',stack_.len)

    print("Popping:")
    popval = stack_.Pop()
    print(f'value {popval} popped!')
    print(stack_)
    print('stack size: ',stack_.len)

    stack_.Pop()
    stack_.Pop()
    # stack_.Pop() ## empty stack error
    print('After popping twice:')
    print(stack_)

    print('pushing 20 and 30:')
    stack_.Push(20)
    stack_.Push(30)
    print(stack_)
    print('clear/delete stack: ')
    stack_.deleteStack()
    print(stack_)

    print('\n\n')
    stack_size = 3
    stack_ = stack(size=stack_size)
    print(f'Stack with size_limit={stack_size}')
    stack_.Push(100)
    stack_.Push(200)
    stack_.Push(300)
    print(stack_)
    stack_.Push(400) ## try to push after size limit



