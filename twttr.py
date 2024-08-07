def main():
    word = input('Input: ').strip()
    print(f'Output: {shorten(word)}')


def shorten(word):
    lst = []
    for aletter in range(len(word)):
        lst.append(word[aletter])


if __name__ == "__main__":
    main()