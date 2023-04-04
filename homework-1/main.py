from src.stack import Node, Stack

if __name__ == '__main__':
    n1 = Node(5, None)
    n2 = Node('a', n1)
    print(n1.data)  # 5
    print(n2.data)  # a
    print(n1)  # <__main__.Node object at 0x0000022803036050>
    print(n2.next_node)  # <__main__.Node object at 0x0000022803036050>

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    print(stack.pop())  # data3
    print(stack.pop())  # data2
    print(stack.pop())  # data1
    print(stack.pop())  # None
    print(stack.top())  # AttributeError: 'NoneType' object has no attribute 'data'
