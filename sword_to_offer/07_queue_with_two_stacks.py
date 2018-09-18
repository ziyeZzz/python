#-*- coding: utf-8 -*-
#栈的实现（pop，push），用两个栈实现队列
'''
Q:用两个栈实现一个队列，队列的声明如下，
请实现它的两个函数appendTail和deleteHead,
分别完成在队列尾部插入结点和在队列头部删除结点的功能。
template <> class CQueue{
    public:
        CQueue(void);
        ~CQueue(void);
        void appendTail(const T& node);
        T deleteHead();
    private:
        stack<T> stack1;
        stack<T> stack2;
};
'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self._next = None
    def __repr__(self):
        return self.data

# Stack:先进后出
class stack(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        if self.isEmpty():
            return 'Empty stack'
        else:
            nlist = ''
            node = self.head
            while node:
                nlist += str(node.data) + ' '
                node = node._next
            return nlist

    def isEmpty(self):
        return (self.length==0)
    def pop(self):
        pop_node = None
        if self.isEmpty():
            return 'Error:empty stack'
        elif self.length == 1:
            pop_node = self.head
            self.head = None
            self.length = 0
        else:
            node = self.head
            i = 0
            while i < self.length-2:
                node = node._next
                i += 1
            pop_node = node._next
            node._next = None
            self.length -= 1
        return pop_node

    def push(self, dataOrNode):
        push_node = None
        if isinstance(dataOrNode, Node):
            push_node = dataOrNode
        else:
            push_node =Node(dataOrNode)
        if self.isEmpty():
            self.head = push_node
            self.length += 1
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = push_node
            self.length += 1

# Queue:先进先出
class queue(object):
    def __init__(self):
        self.stack1 = stack()
        self.stack2 = stack()

    def __repr__(self):
        return self.stack1.__repr__()

    #append queue时，直接在stack1中push即可
    def append(self, dataOrNode):
        self.stack1.push(dataOrNode)

    #delete queue时，将stack1中除第一个node外其余node倒到stack2中，将stack1中第一个node pop出来。再将stack2中所有node倒到stack1中。
    def delete(self):
        if self.stack1.length == 0:
            return 'Error: empty queue'
        else:
            while self.stack1.length > 1:
                tmp = self.stack1.pop()
                self.stack2.push(tmp)
            self.stack1.pop()
            while not self.stack2.isEmpty():
                tmp = self.stack2.pop()
                self.stack1.push(tmp)

if __name__=='__main__':
    print('Stack:')
    stack1 = stack()
    print(stack1.__repr__())
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    print(stack1.__repr__())
    stack1.pop()
    print(stack1.__repr__())
    print('Queue:')
    queue1 = queue()
    print(queue1.__repr__())
    print(queue1.delete())
    queue1.append(4)
    queue1.append(5)
    queue1.append(6)
    print(queue1.__repr__())
    queue1.delete()
    print(queue1.__repr__())
    queue1.delete()
    print(queue1.__repr__())
    queue1.delete()
    print(queue1.__repr__())

