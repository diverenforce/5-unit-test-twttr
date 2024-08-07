def main():
    word = input('Input: ').strip()
    print(f'Output: {shorten(word)}')


def shorten(word):
    lst = []
    for aletter in range(len(word)):
        lst.append(word[aletter])

    for letters in range(len(lst)):
        match lst[letters]:
            case 'a' | 'e' | 'i' | 'o' | 'u' | 'A' | 'E' | 'I' | 'O' | 'U':
                lst[letters] = lst[letters].replace(lst[letters][0],'')
    
    return ''.join(lst)

if __name__ == "__main__":
    main()