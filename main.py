

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)

    words = file_contents.split()

    words_len = len(words)

    print(words_len)




    frankenstein_lower = file_contents.lower()

    letter_freq = {}
    for i in frankenstein_lower:
        if i in letter_freq:
            letter_freq[i] += 1
        else:
            letter_freq[i] = 1

    print(letter_freq)












