def gcd(n,m): #проверка на взаимно простые
    if m==0:
       return n
    else:
       return gcd(m,n%m)
 
def task(n,m):
    return gcd(n,m)==1

def rsa(text, alph): #RSA 13 11 31
  # print("Введите ключи в порядке p, q, e:")
  # key = input()
  # key = key.split(' ')
  p, q, e = 13, 11, 31
  # p = int(key[0])
  # q = int(key[1])
  n = p*q
  fn = (p-1)*(q-1)
  # e = int(key[2])
  prov = task(e,fn)
  if prov == True:
    print("e и φ(n) взаимно простые")
  else:
    print("Ошибка")
  d = pow(e, -1, fn) #что-то вроде алгоритма Евклида
  print("1. Зашифровать \n2. Расшифровать")
  l = int(input())
  output = ''
  b = []
  if l == 1: #Зашифровка
    text = replace(text, alph)
    for i in range (len(text)):
      b.append((text[i]**e)%n)
    print("Зашифрованно: ", b)
    b = replace2(b, alph)
  if l == 2:  #Расшифровка
    print("d =", d)
    text = text.split(', ')
    for i in range (len(text)):
      b.append((int(text[i])**d)%n)
    b = replace2(b, alph)
    for i in range(len(b)):
      output = output + b[i]
    print("Расшифровка:", output)

def elgamal(text, alph): #Elgamal
  p, x, g = 41, 8, 5
  # print("Введите ключи в порядке p, x, g:")
  # key = input()
  # key = key.split(' ')
  # p = int(key[0])
  fp = p-1
  # x = int(key[1])
  # g = int(key[2])
  y = (g**x)%p
  print("1. Зашифровать \n2. Расшифровать")
  l = int(input())
  output = ''
  k = [11, 9, 7]
  q = []
  w = []
  j = 0
  if l == 1: #Зашифровка 
    text = replace(text, alph)
    for i in range (0, len(text)):
      ki = k[j]
      j = (j+1)%(len(k))
      prov = task(ki,fp)
      if prov == False: #проверка на взаимно простые
        print("Ошибка")
        break
      m = text[i] + 1
      a = (g**ki)%p
      b = ((y**ki)*text[i])%p
      w = [a, b]
      q.append(w)
    print(q)
  if l == 2: #Расшифровка
    ans = []
    text = text.split('], [')
    for i in range(len(text)):
      text[i] = text[i].split(', ')
      for j in range(2):
        text[i][j] = int(text[i][j])
    for i in range(len(text)):
      m = linearCongruence((text[i][0]**x), text[i][1], p)
      ans.append(m)
    ans = replace2(ans, alph)
    output = ''.join(ans)
    print(output)

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

# def ecc(text, alph): #ECC
#   print("1. Зашифровать \n2. Расшифровать")
#   l = int(input())
#   output = ''
#   if l == 1:
#     print(output)
#   if l == 2:
#     print(output)

def replace(rep, alph):  #преобразование букв алфавита в их порядковый номер
    res = []
    for i in range(0, len(rep)):
        for j in range(0, len(alph)):
            if (rep[i] == alph[j]):
                res.append(j + 1)
    return (res)


def replace2(rep, alph):  #преобразование номера буквы алфавита в букву
    res = ''
    for i in range(0, len(rep)):
        for j in range(0, len(alph)):
            if (int(rep[i] - 1) == j):
                res = res + alph[j]
    return (res)
  
alph = [ "А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я", "а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы",  "ь", "э", "ю", "я", "-", ",", ".", " ", "–"]
#alph = ["а","б","в","г","д","е","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
print(
    "Выбрать шифр: \n 1. RSA \n 2. Elgamal")
t = int(input())
print("Введите текст:")
text = input()
if (t == 1):
  rsa(text, alph)
if (t == 2):
  elgamal(text, alph)
# if (t == 3):
#   ecc(text, alph)
