def palindrome(word: str) -> bool:
    i = 0
    j = len(word) - 1
    while i <= j:

        if not word[i].isalpha():
            i += 1
            continue
        elif not word[j].isalpha():
            j -= 1
            continue
        elif word[i] != word[j]:
            return False

        i += 1
        j -= 1

    return True

text = input("Введите слово: ").lower()
print(palindrome(text))
