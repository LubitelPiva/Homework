def f(word, words):
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
    return words
with open("file.txt") as f:
    b = f.read()
    file = b.split()
    words = {}
    for word in file:
        words = f(word, words)
    nums = list(words.items())
    nums.sort(key=lambda i: i[1], reverse=1)

with open("output.txt", 'w') as f:
    for i in nums:
        f.writelines(str(i[0]) + " " + str(i[1]) + "\n")