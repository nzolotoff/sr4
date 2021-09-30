
person_year = int(input('Введите количество лет\n'))
person_eks = int (input('Введите количество экспонатов \n'))
za_den = 96
za_god = za_den * 365
eks = za_god * person_year
print ('За', person_year, 'лет/год(а) будет просмотрено', eks, 'экспонатов')


v_min = person_eks * 5
v_dnyah = v_min // 460 
v_godah = v_dnyah // 365 
print (v_min, ' - минут ', v_dnyah, ' - дней ', v_godah, ' - лет')
