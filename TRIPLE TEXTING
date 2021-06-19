text = input()
freq = dict()
for i in range(0, 3):
    word = text[i * len(text) // 3 : (i + 1) * len(text) // 3]
    if word not in freq:
        freq[word] = 0
    freq[word] += 1
    if(freq[word] == 2):
        print(word)
        break
