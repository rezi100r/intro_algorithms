"""
Астрологи объявили день очередей ограниченного размера. Тимофею нужно написать класс MyQueueSized, который принимает параметр max_size, означающий максимально допустимое количество элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать работу такой очереди. Функции, которые надо поддержать, описаны в формате ввода.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 5000.
Во второй строке задан максимально допустимый размер очереди, он не превосходит 5000.
Далее идут команды по одной на строке. Команды могут быть следующих видов:

push(x) — добавить число x в очередь;
pop() — удалить число из очереди и вывести на печать;
peek() — напечатать первое число в очереди;
size() — вернуть размер очереди;
При превышении допустимого размера очереди нужно вывести «error». При вызове операций pop() или peek() для пустой очереди нужно вывести «None».
Формат вывода
Напечатайте результаты выполнения нужных команд, по одному на строке.
"""


class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.qsize = 0

    def is_empty(self):
        return self.qsize == 0

    def push(self, x):
        if self.qsize != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.qsize += 1
            return 'OK'
        else:
            return 'error'

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.qsize -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def size(self):
        return self.qsize


if __name__ == '__main__':
    number = int(input())
    queue_length = int(input())
    stack = MyQueueSized(queue_length)
    result_list = []
    for index in range(number):
        command = input().split()
        if command[0] == 'push':
            result = stack.push(int(command[1]))
            if result == 'error':
                result_list.append(result)
        if command[0] == 'pop':
            result_list.append(stack.pop())
        if command[0] == 'peek':
            result_list.append(stack.peek())
        if command[0] == 'size':
            result_list.append(stack.size())

    for index in result_list:
        print(index)
