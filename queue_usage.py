from data_structures.queues import queue

if __name__ == '__main__':
    queue_ = queue()
    print('printing queue after creation:')
    print(queue_)

    Enqueue_val = 5
    print(f'printing queue after Enqueuing {Enqueue_val}:')
    queue_.Enqueue(Enqueue_val)
    print(queue_)

    queue_.Enqueue(10)
    queue_.Enqueue(15)
    print('printing queue after Enqueuing 10 and 15:')
    print(queue_)

    print("default Peek at First of queue: ",queue_.Peek())
    print("Peek at last of queue: ",queue_.Peek(last=True))

    print("queue isEmpty?: ",queue_.isEmpty())
    print('queue size: ',queue_.len)

    print("Dequeuing:")
    Dequeueval = queue_.Dequeue()
    print(f'value {Dequeueval} Dequeued!')
    print(queue_)
    print('queue size: ',queue_.len)

    queue_.Dequeue()
    queue_.Dequeue()
    # queue_.Dequeue() ## empty queue error
    print('After dequeuing twice:')
    print(queue_)

    print('Enqueuing 20 and 30:')
    queue_.Enqueue(20)
    queue_.Enqueue(30)
    print(queue_)
    print('clear/delete queue: ')
    queue_.deleteQueue()
    print(queue_)

    print('\n\n')
    queue_size = 3
    queue_ = queue(size=queue_size)
    print(f'queue with size_limit={queue_size}')
    queue_.Enqueue(100)
    queue_.Enqueue(200)
    queue_.Enqueue(300)
    print(queue_)
    queue_.Enqueue(400) ## try to Enqueue after size limit



