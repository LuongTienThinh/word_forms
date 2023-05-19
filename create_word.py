from word_forms.word_forms import get_word_forms
word = "beach"
result = get_word_forms(word)

def getFile(obj):
    write_file = str(obj).replace('\'', '\"').replace('{', '[').replace('}', ']')
    temp = list(write_file)
    temp[0] = "{"
    temp[len(temp) - 1] = "}"
    write_file = ''.join(temp)
    return write_file.replace("set()", "null")


with open(f'./word_json/{word}.json', 'w') as f:
    f.write(getFile(result))

with open('list_word.txt', 'a') as f:
    f.write(f"{word}\n")