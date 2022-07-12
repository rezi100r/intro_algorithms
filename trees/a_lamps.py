# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root):
    value = root.value

    def _sub(links, value):

        if links.left is not None:
            value = (links.value if value < links.value else value)
            value = _sub(links.left, value)
        if links.right is not None:
            value = (links.value if value < links.value else value)
            value = _sub(links.right, value)
        if value < links.value:
            return links.value
        else:
            return value
    value = _sub(root, value)
    return value


def test():
    node9 = Node(0)
    node8 = Node(0, None, node9)
    node7 = Node(111)
    node6 = Node(0)
    node5 = Node(0)
    node4 = Node(3, node7, node8)
    node3 = Node(3, node5, node6)
    node2 = Node(2, None, node4)
    node1 = Node(2, node3, None)
    node0 = Node(0, node1, node2)
    assert solution(node0) == 111


if __name__ == '__main__':
    test()
