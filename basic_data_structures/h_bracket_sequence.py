PATTERN = {
    '(': ')',
    '[': ']',
    '{': '}',
}


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]


if __name__ == '__main__':
    inp_line = list(input())
    stack = Stack()
    for value in inp_line:
        if value in PATTERN.keys():
            stack.push(value)
        elif not stack.isEmpty() and PATTERN.get(stack.peek()) == value:
            stack.pop()
        else:
            stack.push(value)
    if stack.isEmpty():
        print('True')
    else:
        print('False')
