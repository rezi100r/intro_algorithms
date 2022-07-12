class ListQueue:
    class Node:
        def __init__(self, value=None, next_item=None):
            self.value = value
            self.next_item = next_item

        def __str__(self):
            return self.value

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.qsize = 0

    def is_empty(self):
        return self.qsize == 0

    def get(self):
        if self.is_empty():
            return 'error'
        if self.qsize == 1:
            removed = self.head
            self.__init__()
            return removed.value
        if self.qsize == 2:
            removed = self.head
            self.head = self.tail
            self.qsize -= 1
            return removed.value
        removed = self.head
        self.head = self.tail.next_item.next_item
        self.tail.next_item = self.head
        self.qsize -= 1
        return removed.value

    def put(self, item):
        if self.is_empty():
            self.head = self.Node(value=item)
            self.tail = self.head
        else:
            self.tail.next_item = self.Node(value=item)
            self.tail.next_item.next_item = self.head
            self.tail = self.tail.next_item
        self.qsize += 1

    def size(self):
        return self.qsize


if __name__ == '__main__':
    number = int(input())
    stack = ListQueue()
    result_list = []
    for index in range(number):
        command = input().split()
        if command[0] == 'put':
            stack.put(int(command[1]))
            # continue
        if command[0] == 'get':
            result_list.append(stack.get())
            # continue
        if command[0] == 'size':
            result_list.append(stack.size())
    for index in result_list:
        print(index)
