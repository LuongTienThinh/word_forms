list_word = []

with open('list_word.txt', 'r') as file:
    for line in file:
        list_word.append(str(line).replace('\n', ''))

list_word_api = []

for i in list_word:
    f = open(f"./word_json/{i}.json", "r")
    list_word_api.append(f.read())

with open(f'list_api.json', 'w') as f:
    f.write(str(list_word_api).replace('\'', '\"').replace('\\n', '').replace('\"{', '{').replace('}\"', '}'))
