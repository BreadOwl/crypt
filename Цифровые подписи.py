def gcd(n,m): #проверка на взаимно простые
  if m==0:
    return n
  else:
    return gcd(m,n%m)

def task(n,m):
   return gcd(n,m)==1

def rsa(text, alph): #RSA
  print("Введите p, q и e:")
  key = input()
  key = key.split(' ')
  p = int(key[0])
  q = int(key[1])
  n = p*q
  fn = (p-1)*(q-1)
  e = int(key[2])
  prov = task(e,fn)
  if prov == True:
    print("e и φ(n) взаимно простые")
  else:
    print("Ошибка")
  d = pow(e, -1, fn) #что-то вроде алгоритма Евклида
  text = replace(text, alph)
  h = 0
  for i in range(len(text)):
    h = ((h+text[i])**2)%p #формируем хэш
  print("Хэш равен ",h)
  s = (h**d)%n
  print("S =",s)
  m = (s**e)%n
  if h == m:
    print("Подпись совпадает. m =",h,", m' =",m)
  else:
    print("Подпись не совпадает")

def elgamal(text, alph): #Elgamal
  print("Введите p, g (g<p), x, k:")
  key = input()
  key = key.split(' ')
  p = int(key[0])
  fp = p-1
  x = int(key[2])
  g = int(key[1])
  k = int(key[3])
  if g > p:
    print("g > p, ошибка")
  y = (g**x)%p
  text = replace(text, alph)
  h = 0
  for i in range(len(text)):
    h = ((h+text[i])**2)%p #формируем хэш
  prov = task(k,fp)
  if prov == True:
   print("k и p-1 взаимно простые")
  else:
    print("Ошибка")
  a = (g**k)%p
  b = linearCongruence(k, (h-x*a), fp)
  print("Хеш равен",h," S = (",a,",",b,")")
  print("Проверка")
  a1 = (y**a)*(a**b)%p
  a2 = (g**h)%p
  if a1 == a2:
    print("Подпись совпадает, a1 =",a1,", a2 =",a2)
  else:
    print("Подпись не совпадает")

def ExtendedEuclidAlgo(a, b):#расширенный алгоритм Евклида
  if a == 0:
    return b, 0, 1
  gcd, x1, y1 = ExtendedEuclidAlgo(b % a, a)
  x = y1 - (b // a) * x1
  y = x1
  return gcd, x, y

def linearCongruence(A, B, N):#линейная конгруэнтность
  A = A % N
  B = B % N
  u = 0
  v = 0
  d, u, v = ExtendedEuclidAlgo(A, N)
  if (B % d != 0):
    print(-1)
    return
  x0 = (u * (B // d)) % N
  ans = []
  if (x0 < 0):
    x0 += N
  for i in range(d):
    return (x0 + i * (N // d)) % N

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

alph = [ "А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О",
"П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю",
"Я", "а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р",
"с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", "-", ",", ".",
" ", "–"]
print(
 "Выбрать цифровую подпись: \n 1. RSA \n 2. Elgamal")
t = int(input())
print("Введите текст:")
text = input()
if (t == 1):
  rsa(text, alph)
if (t == 2):
  elgamal(text, alph)
