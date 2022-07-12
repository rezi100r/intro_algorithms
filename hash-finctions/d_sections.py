if __name__ == '__main__':

    count = int(input())

    sections = [input() for i in range(count)]
    sections = sorted(set(sections), key=lambda d: sections.index(d))

    for section in sections:
        print(section)
