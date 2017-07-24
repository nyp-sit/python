
clist = []
for i in range(3):
    w = input('Enter the word to be censored: ')
    clist.append(w)

count = 0
while count < 3:
    s = input('Enter a string : ')
    for word in clist :
        i = s.count(word)
        if i > 0:
            count += 1
            print('You have been censored', count, 'times')
            s = s.replace(word, word[0] + 'x'*(len(word)-1))

    print(s)
print('You have been banned!')
