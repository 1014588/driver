#這是一姑關於台灣和美國駕照判別年齡的程式
country = input('請問你哪個國家的?')
age = input('你幾歲呢?')
age = int(age)
if country == 'Taiwan':
    if age >= 18:
        print('你可以考照喔')
    else:
        print('你太老了')
elif country == 'America':
    if age >= 16:
        print('你可以考照喔!')
    else:
        print('不能考喔!')
else:
    print('請輸入_America or Taiwan')                   