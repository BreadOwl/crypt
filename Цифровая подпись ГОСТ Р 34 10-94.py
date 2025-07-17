def gost94(text, alph):
  print("Введите p, q, a, x (x < q):")
  key = input()
  key = key.split(' ')
  p = int(key[0])
  q = int(key[1])
  a = int(key[2])
  if (a**q)%p != 1:
    return print("Ошибка a")
  x = int(key[3])
  y = (a**x)%p
  text = replace(text, alph)
  h = 0
  for i in range(len(text)):
    h = ((h+text[i])**2)%p #формируем хэш
  print("Хэш равен ",h)
  print("Введите k (k<q)")
  k = int(input())
  if k>q:
    return print("Ошибка k")
  r = ((a**k)%p)%q
  s = (x*r + k*h)%q
  print("r =",r,"s =",s,"\nПроверка")
  v = (h**(q-2)) % q
  z1 = (s * v) % q
  z2 = ((q-r) * v) % q
  u = ((a**(z1) * y**(z2) ) % p) % q
  if u == r:
    print ("u = r. Подпись верная")
  else:
    print ("Подпись не верна")

def replace(rep, alph): #преобразование букв алфавита в их порядковый номер
  res = []
  for i in range(0, len(rep)):
    for j in range(0, len(alph)):
      if (rep[i] == alph[j]):
        res.append(j + 1)
  return (res)

def replace2(rep, alph): #преобразование номера буквы алфавита в букву
  res = ''
  for i in range(0, len(rep)):
    for j in range(0, len(alph)):
      if (int(rep[i] - 1) == j):
        res = res + alph[j]
  return (res)

alph = ["а","б","в","г","д","е","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
#alph = [ "А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я", "а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", "-", ",", ".", " ", "–"]
print("Выбрать цифровую подпись: \n 1. ГОСТ Р 34.10-94 \n 2. ГОСТ Р 34.10-2012")
t = int(input())
print("Введите текст:")
text = input()
if (t == 1):
  gost94(text, alph)
if (t == 2):
  gost2012(text, alph)
