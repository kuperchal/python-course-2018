# t = {'PM 200': 30, 'N3200': 23, 'N3300': 21.8, 'N3400': 21.8, 'N3900': 23.5, 'N100': 22, 'XP2406': 2.8, 'XP2580': 19.5,
#      'XP2714': 16, 'XP2730': 22.7, 'N75': 16.5, 'Z4470': 11.9, 'Tolonate HDT LV': 23, 'Tolonate HDB LV': 23.7,
#      'PM 700': 31, 'ONGRONATE 2100': 31, 'TDI': 47, 'Voranol CP 4711': 1.047, 'RA 640': 19.49, 'Oktil': 13.05,
#      'Synthanol 4413': 7.5, 'Synthanol 4415': 4.5, 'Poly P 2200': 1.81, 'Voranol 1010L': 3.34, 'PDA 800': 4.4,
#      'Laprocsid 301': 0.151, 'Laprocsid 702': 3.318, 'Laprocsid 703': 6.32, 'Laprocsid 181': 10.863, 'FtorGlik': 8.196}
# k={'PM 200': 'NCO', 'N3200': 'NCO', 'N3300': 'NCO', 'N3400': 'NCO', 'N3900': 'NCO', 'N100': 'NCO', 'XP2406': 'NCO',
#    'XP2580': 'NCO', 'XP2714': 'NCO', 'XP2730': 'NCO', 'N75': 'NCO', 'Z4470': 'NCO', 'Tolonate HDT LV': 'NCO',
#    'Tolonate HDB LV': 'NCO', 'PM 700': 'NCO', 'ONGRONATE 2100': 'NCO', 'TDI': 'NCO', 'Voranol CP 4711': 'OH',
#    'RA 640': 'OH', 'Oktil': 'OH', 'Synthanol 4413': 'OH', 'Synthanol 4415': 'OH', 'Poly P 2200': 'OH',
#    'Voranol 1010L': 'OH', 'PDA 800': 'OH', 'Laprocsid 301': 'OH', 'Laprocsid 702': 'OH', 'Laprocsid 703': 'OH',
#    'Laprocsid 181': 'OH', 'FtorGlik': 'OH'}
file = open("k.txt")
onstring = file.read().split("\n")[:-1]
k=dict()
for item in onstring:
    key = item.split(":")[0]
    value = item.split(":")[1]
    k[key] = value
file.close()
file = open("t.txt")
onstring = file.read().split("\n")[:-1]
t=dict()
for item in onstring:
    key = item.split(":")[0]
    value = float(item.split(":")[1])
    t[key] = value
file.close()
print('Bbedute kol-vo komponentov OCHOBbI')
a=input()
d={}
for i in range(int(a)): #Цикл для ввода наименнования компонента и его массы. Необходимо для того, чтобы расчитать NCO
                        #основы, состоящей из данных компонентов.
    print(str(i+1)+' KOMPOHEHT')
    name=input()
    print('MACCA')
    m=input()
    d[name]=m
s=0
p=0
p1=0
for i in d: #Считаем общую массу основы.
    s=s+int(d[i])
for x in d: #Проходимся по словарям, ищем чтобы совпадали ключи.
    for j in k:
        if x==j:
            if k[j]=='NCO': #В случае если этот компонент имеет природу NCO, то мы считаем содержанние данных групп.
                for c in t: #Ищем в словаре молекулярную массу компонента.
                    if c==x:
                        p=p+(int(t[c])*int(d[x])/s) #Подсчет содержания групп NCO
            else: #Аналогичная операция только, если компонент имеет природу OH
                for c in t:
                    if c==x:
                        p1=p1+(int(t[c])*int(d[x])/s) #Подсчет содержания групп OH

p1=p1*2.47
NCO=p-p1
print('Bbedute kol-vo komponentov OTBEPDUTELYA') #Аналогичная операция для отвердителя.
b=input()
d1={}
for i in range(int(b)):
    print(str(i+1)+' KOMPOHEHT')
    name=input()
    print('MACCA')
    m=input()
    d1[name]=m
p2=0
for i in d1:
    for j in k:
        if i==j:
            if k[j]=='NCO':
                for c in t:
                    if c==i:
                        p2=p2+((int(t[c])*int(d1[i])/100)/42)
            else:
                for c in t:
                    if c==i:
                        p2=p2+((int(t[c])*int(d1[i])/100)/17)
NC=NCO/42
print('FUNCIONAL SOOTNOSCHENIE')
k=input()
sot=round((float(k)*p2/NC),3) #Просто считаем массовое соотношение, в котором нужно смешать, учитывая функциональное соотношение.
print('NCO=',NCO)
print('MASSOVOE SOOTNOSCHENIE=',sot)
