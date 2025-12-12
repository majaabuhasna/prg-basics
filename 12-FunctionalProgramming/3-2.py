sentence = 'I completely agree with you'
sentence = sentence.split()

result = list(map(lambda x:len(x),sentence))
print(result)