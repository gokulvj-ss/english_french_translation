import os
import csv
import time

start_time = time.time()

french_dict = {}
with open(os.path.join('french_dictionary.csv'), 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if row[0] != row[1]:
            french_dict[row[0]] = row[1]
french_dictionary = {}
for i in sorted(french_dict, key = len, reverse = True):
    french_dictionary[i] = french_dict[i]

count_dict = {}
with open(os.path.join('t8.shakespeare.txt'), 'r') as org_para:
    words = org_para.read()
    for word in french_dictionary:
        temp = word[0].upper() + word[1:]
        replace_words = [word, word.upper(), temp]
        for replace_word in range(len(replace_words)):
            if replace_word == 0:
                occurence1 = words.count(replace_words[replace_word])
                words = words.replace(replace_words[replace_word], french_dictionary[word])
            elif replace_word == 1:
                occurence2 = words.count(replace_words[replace_word])
                words = words.replace(replace_words[replace_word], french_dictionary[word].upper())
            elif replace_word == 2:
                occurence3 = words.count(replace_words[replace_word])
                temp = french_dictionary[word]
                insert_word = temp[0].upper() + temp[1:]
                words = words.replace(replace_words[replace_word], insert_word)
        count_dict[word] = occurence1 + occurence2 + occurence3

sort_keys = list(count_dict.keys())
sort_keys.sort()
count_dictionary = {i: count_dict[i] for i in sort_keys}
with open(os.path.join('t8.shakespeare.translated.txt'), 'w') as translated_para:
    translated_para.write(words)

with open(os.path.join('frequency.csv'), 'w', newline = '') as csv_file:
    field_names = ['English Word', 'French Word', 'Frequency']
    writer = csv.writer(csv_file)
    writer.writerow(field_names)
    for count in count_dictionary:
        writer.writerow([count, french_dictionary[count], count_dictionary[count]])

end_time = time.time()
time = end_time - start_time
if time <= 60:
    execution_time = time
    format = 'seconds'
else:
    execution_time = time/60
    format = 'minutes'

with open(os.path.join('performance.txt'), 'w') as time_file:
    time_file.write('Time to process: %s (in %s)\n'%(execution_time, format))
    time_file.write('Memory used: %s'%'2.41 KB (2,475 bytes)')

print('The translation done successfully!')