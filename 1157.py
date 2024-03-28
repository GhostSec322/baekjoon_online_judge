input_alphabet = input("").upper()
alphabet = list(set(input_alphabet))

count_alphabet = {}
for char in alphabet:
    word = input_alphabet.count(char)
    count_alphabet[char] = word
maximum=max(list(count_alphabet.values()))
if list(count_alphabet.values()).count(maximum)>=2:
    print("?")
else:
    for i in count_alphabet:
        if count_alphabet[i]== maximum:
            print(i)
            break

