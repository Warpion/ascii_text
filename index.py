from lib import letters #Подключаем алфавит
str = input('')
str = str.lower()
vivod = ''
str_len = len(str)

for z in range(7): #вывод в консоль
    for j in range(str_len):
        for i in range(0+9*z,8+9*z):
            vivod = vivod + letters[str[j]][i]
    print(vivod)
    vivod= ''

f = open('output.txt','w')
for z in range(7): #вывод в файл
    for j in range(str_len):
        for i in range(0+9*z,8+9*z):
            vivod = vivod + letters[str[j]][i]
    f.write(vivod+'\n')
    vivod = ''
f.close()