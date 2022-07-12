class StackMax:
    def __init__(self):
        self.items = []
        self.max = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.isEmpty() or item >= self.max[-1]:
            self.max.append(item)
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return 'error'
        removed = self.items.pop()
        if removed == self.max[-1]:
            self.max.pop()
        if self.isEmpty():
            self.max.clear()
        return removed

    def get_max(self):
        if self.isEmpty():
            return 'None'
        return self.max[-1]


if __name__ == '__main__':
    stack = StackMax()
    n = int(input())
    result = []
    for index in range(n):
        command = input().split()
        if command[0] == 'push':
            stack.push(int(command[1]))
        if command[0] == 'pop':
            if stack.pop() == 'error':
                result.append('error')
        if command[0] == 'get_max':
            result.append(stack.get_max())
    for index in result:
        print(index)
