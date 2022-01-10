# python string transformation
def transformSentence(sentence):
    splitsentence = sentence.split()
    output = ""
    for i in splitsentence:
        output += i[0]
        for j in range(1, len(i)):
            if i[j-1].lower() < i[j].lower():
                output += i[j].upper()
            elif i[j-1].lower() > i[j].lower():
                output += i[j].lower()
            else:
                output += i[j]
        output += " "
    return output[:-1:]


print(transformSentence('hello'))
