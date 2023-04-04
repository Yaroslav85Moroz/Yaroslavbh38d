text = input()
first_space = text.find(' ')
last_space = text.rfind(' ')

first_word = text[:first_space]
last_word = text[last_space+1]
center = text[first_space:last_space+1]

result = last_word + center + first_word
print(result)
