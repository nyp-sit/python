import re
sentence = "wheel of fortune"
p = re.compile('\w')
hidden_sentence = p.sub('-', sentence)
print('Guess the phrase :', hidden_sentence)
# while loop starts here
while True :
    if hidden_sentence == sentence :
        print('Yeah, you got it right!')
        break
    char = input('Give me a letter : ')
    for i in range(len(sentence)) :
        if char == sentence[i] :
            hidden_sentence = hidden_sentence[:i] + char + hidden_sentence[i+1:]
    print('Guess the phrase :', hidden_sentence)
