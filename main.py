from random import randint

print('Zadanie1')
a = [1 - x for x in range(10)]
print(a)
b = [4 ** n for n in range(8)]
print(b)
c = [x for x in b if x % 2 == 0]
print(c)
print('\nZadanie2')
lista1 = []
for element in range(10):
    randomliczba = randint(0, 9999)
    lista1.append(randomliczba)
print(lista1)
parzyste = [x for x in lista1 if x % 2 == 0]
print(parzyste)
print('\nZadanie3')
produkty = {'masło': 'szt', 'jabłka': 'kg', 'chleb': 'szt', 'majonez': 'szt',
            'banany': 'kg', 'ziemniaki': 'kg', 'ketchup': 'szt', 'sok pomarańczowy': 'szt',
            'żelki': 'szt', 'pomidory': 'kg', 'mięso mielone': 'kg'}
listasztuki = [key for key, wartosc in produkty.items() if wartosc == 'szt']
print('Produkty kupowane na sztuki: ' +str(listasztuki))
print('\nZadanie4')
def trojkat_prostokatny(a,b,c):
    boki[float(a),float(b),float(c)]
print('Podaj boki trójkąta. Sprawdzę, czy jest prostokątny.')
a = float(input('a) Podaj długość pierwszego boku: '))
b = float(input('a) Podaj długość drugiego boku: '))
c = float(input('a) Podaj długość trzeciego boku: '))
if (a + b > c) & (b + c > a) & (a + c > b):
    if (a ** 2 + b ** 2 == c ** 2) or (c ** 2 + b ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2):
        print('To jest trójkąt prostokątny.')
    else:
        print('To nie jest trójkąt prostokątny.')
else:
    print('To nie jest trójkąt.')
print('\nZadanie5')


def poletrapezu(a=4, b=5, h=6):
    trapez = [a, b, h]
    pole = ((a + b) * h) / 2
    return pole


print('Pole trapezu: ' + str(poletrapezu()))
