def f23(lst):
    size= len(lst)
    res=[]
    for i in range(size):
        res0=[]
        res1=[]
        for val in lst[i]:
            if val is not None:
                if "|" in val:
                    str1=""
                    str2=""
                    flag=False
                    for k in range(len(val)):
                        if val[k]=="|":
                            flag=True
                        if (flag==False and val[k]!='|'):
                            str1+=val[k]
                        elif (flag==True and val[k]!='|'):
                            str2+=val[k]
                    res0.append(str1)
                    res0.append(str2)
                else:
                    res0.append(val)
        for j in range(len(res0)-1):
            res1.append(res0[j])
            if res0[j]==res0[j+1]:
                j+=1
        name=res1[0]
        number=res1[1]
        email=res1[2]
        res1[0]=''
        res1[1]=''
        res1[2] = ''
        for k in range(5,len(name)):
            res1[0]+=name[k]
        res1[0] +=' '+name[0]+'.'
        for k in range(3,len(number)):
            if(number[k]!=' ' and number[k]!='-' and number[k]!='‐'):
                res1[1]+=number[k]
        for k in range(len(email)):
            if(email[k]=='['):
                break
            res1[2] += email[k]
        res.append(res1)
    number=[]
    email=[]
    name=[]
    for i in range(size):
        number.append(res[i][1])
        email.append(res[i][2])
        name.append(res[i][0])
    table=[number,email,name]
    return table
"""
def check():
    if (f23([[None, 'К.У. Бофяк|+7 005 101-0491', None, 'bofak79[at]yandex.ru', 'bofak79[at]yandex.ru'], [None, 'Т.О. Килий|+7 101 296-9027', None, 'kilij81[at]yandex.ru', 'kilij81[at]yandex.ru'], [None, 'М.К. Чецук|+7 598 590-9570', None, 'cezuk68[at]gmail.com', 'cezuk68[at]gmail.com'], [None, 'А.К. Шабко|+7 662 846-2710', None, 'sabko73[at]yahoo.com', 'sabko73[at]yahoo.com']])==[['0051010491', '1012969027', '5985909570', '6628462710'], ['bofak79', 'kilij81', 'cezuk68', 'sabko73'], ['Бофяк К.', 'Килий Т.', 'Чецук М.', 'Шабко А.']]):
        print("TRUE")
    else:
        print("FALSE")
    if (f23([[None, 'И.С. Цегурян|+7 773 201-6447', None, 'zeguran31[at]mail.ru', 'zeguran31[at]mail.ru'], [None, 'Н.У. Фучочяк|+7 294 206-4135', None, 'fucocak8[at]rambler.ru', 'fucocak8[at]rambler.ru'], [None, 'А.З. Чегосий|+7 876 405-9246', None, 'cegosij13[at]mail.ru', 'cegosij13[at]mail.ru'], [None, 'С.Б. Самогли|+7 939 096-4058', None, 'samogli65[at]gmail.com', 'samogli65[at]gmail.com']])==[['7732016447', '2942064135', '8764059246', '9390964058'], ['zeguran31', 'fucocak8', 'cegosij13', 'samogli65'], ['Цегурян И.', 'Фучочяк Н.', 'Чегосий А.', 'Самогли С.']]):
        print("TRUE")
    else:
        print("FALSE")
    if (f23([[None, 'К.Ц. Завий|+7 914 644-1243', None, 'zavij83[at]gmail.com', 'zavij83[at]gmail.com'], [None, 'В.Д. Геривский|+7 822 397-0890', None, 'gerivskij81[at]gmail.com', 'gerivskij81[at]gmail.com'], [None, 'Б.Н. Рикберг|+7 779 202-9407', None, 'rikberg82[at]yahoo.com', 'rikberg82[at]yahoo.com'], [None, 'Д.У. Гебко|+7 212 249-2647', None, 'gebko81[at]mail.ru', 'gebko81[at]mail.ru']])==[['9146441243', '8223970890', '7792029407', '2122492647'], ['zavij83', 'gerivskij81', 'rikberg82', 'gebko81'], ['Завий К.', 'Геривский В.', 'Рикберг Б.', 'Гебко Д.']]):
        print("TRUE")
    else:
        print("FALSE")
    if (f23([[None, 'Р.Ц. Бовберг|+7 661 429-2174', None, 'bovberg72[at]gmail.com', 'bovberg72[at]gmail.com'], [None, 'А.С. Шачибянц|+7 748 145-9410', None, 'sacibanz61[at]yahoo.com', 'sacibanz61[at]yahoo.com'], [None, 'И.Б. Чутелич|+7 785 963-0704', None, 'cutelic53[at]rambler.ru', 'cutelic53[at]rambler.ru'], [None, 'М.С. Цичиди|+7 221 730-4871', None, 'zicidi48[at]yandex.ru', 'zicidi48[at]yandex.ru']])==[['6614292174', '7481459410', '7859630704', '2217304871'], ['bovberg72', 'sacibanz61', 'cutelic53', 'zicidi48'], ['Бовберг Р.', 'Шачибянц А.', 'Чутелич И.', 'Цичиди М.']]):
        print("TRUE")
    else:
        print("FALSE")
    if (f23([[None, 'М.А. Талич|+7 325 857-5952', None, 'talic70[at]mail.ru', 'talic70[at]mail.ru'], [None, 'М.Ч. Фачев|+7 678 007-1349', None, 'facev10[at]rambler.ru', 'facev10[at]rambler.ru'], [None, 'А.Е. Гумий|+7 965 183-2917', None, 'gumij59[at]rambler.ru', 'gumij59[at]rambler.ru']])==[['3258575952', '6780071349', '9651832917'], ['talic70', 'facev10', 'gumij59'], ['Талич М.', 'Фачев М.', 'Гумий А.']]):
        print("TRUE")
    else:
        print("FALSE")
    if (f23([[None, 'В.Т. Дичский|+7 099 063-2973', None, 'dicskij65[at]gmail.com', 'dicskij65[at]gmail.com'], [None, 'М.Т. Лолачман|+7 504 539-3655', None, 'lolacman64[at]mail.ru', 'lolacman64[at]mail.ru'], [None, 'И.О. Базский|+7 827 610-4834', None, 'bazskij29[at]yahoo.com', 'bazskij29[at]yahoo.com']])==[['0990632973', '5045393655', '8276104834'], ['dicskij65', 'lolacman64', 'bazskij29'], ['Дичский В.', 'Лолачман М.', 'Базский И.']]):
        print("TRUE")
    else:
        print("FALSE")
    if (f23([[None, 'М.А. Чутавянц|+7 605 549-5168', None, 'cutavanz12[at]yahoo.com', 'cutavanz12[at]yahoo.com'], [None, 'Я.К. Росасич|+7 553 144-3893', None, 'rosasic86[at]gmail.com', 'rosasic86[at]gmail.com'], [None, 'Я.К. Киний|+7 813 371-0584', None, 'kinij87[at]rambler.ru', 'kinij87[at]rambler.ru'], [None, 'М.Ч. Бусин|+7 884 124-7926', None, 'busin23[at]gmail.com', 'busin23[at]gmail.com']])==[['6055495168', '5531443893', '8133710584', '8841247926'], ['cutavanz12', 'rosasic86', 'kinij87', 'busin23'], ['Чутавянц М.', 'Росасич Я.', 'Киний Я.', 'Бусин М.']]):
        print("TRUE")
    else:
        print("FALSE")

check()
"""