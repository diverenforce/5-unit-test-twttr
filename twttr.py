def main():
    word = input('Input: ').strip()
    print(f'Output: {shorten(lstmaker(word))}')


def shorten(lst):

    for letters in range(len(lst)):
        match lst[letters]:
            case 'a' | 'e' | 'i' | 'o' | 'u' | 'A' | 'E' | 'I' | 'O' | 'U':
                lst[letters] = lst[letters].replace(lst[letters],'')
    
    return ''.join(lst)

def lstmaker(word):
    lst = []
    for aletter in range(len(word)):
        lst.append(word[aletter])
    return lst


if __name__ == "__main__":
    main()