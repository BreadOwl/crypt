import numpy as np
from numpy import matrix

def int_r(num):#фукнция правильного округления
    num = int(num + (0.5 if num > 0 else -0.5))
    return num

def revers(a):#проверка на обратимость
  print ("Проверка на обратимость")
  a = preobr(a)
  a_inv = np.linalg.inv(a)
  if (np.linalg.det(a) != 0):
    print("Обратимая")
  else:
    print("Ошибка")

def mult(a, b):#умножение матриц
  a = np.array(a)
  b = np.array(b)
  res = a.dot(b)
  return res

def preobr(text):#преобразование строки в двумерный массив
  c = []
  w = []
  text = text.split(';')
  for i in range(0, len(text)):
    text[i] = text[i].split(' ')
  for i in range(0, len(text)):
    for j in range(0, 3):
      if (text[i][j].find('-') == 0):
        e = text[i][j].replace("-", "")
        w.append(int(e)*(-1))
      else:
        w.append(int(text[i][j]))
    c.append(w)
    w = []
  return c

def matr(text, alph): #Матричный шифр 
  print ("Введите ключ:")
  key = input()
  revers(key)
  print ("1. Зашифровать \n2. Расшифровать")
  t = int(input())
  output = ""
  if (t == 1):
    text = replace(text, alph)
    key = preobr(key)
    if (len(text)%3 != 0):
      print('Ошибка')
    else:
      for i in range (0, len(text), 3):
        b = [text[i], text[i+1], text[i+2]]
        res = mult(key, b)
        output = output + str(res)
    print (output)
  if (t == 2):
    c = preobr(text)
    resul = []
    key = preobr(key)
    a = matrix(key)
    key = (a.I)#инверсия
    for i in range (0, len(c)):
      res = mult(key, c[i])
      for l in range(0, len(res)):
        resul.append(res[l])
    print (replace2(resul, alph))

def playfair(text): #Шифр Плэйфера – шифр биграммной замены
  print ("Введите ключ:")
  key = input()
  alphp = key
  alphp = fillalph(alphp)
  text = list(text)
  w = []
  tex = []
  res = []
  r = []
  p = []
  t = []
  print ("1. Зашифровать \n2. Расшифровать")
  t = int(input())
  output = ""
  if (t == 1):
    t = []
    for i in range(0, len(text)):
      if (text[i] == text[i-1]):
        t.append('ф')
        t.append(text[i])
      else:
        t.append(text[i])
    for i in range(0, len(t), 2):#разбиение текста на биграммы
      for j in range(0,2):
        w.append(t[i+j])
      tex.append(w)
      w = []
    for i in range (0, len(tex)):
      for l in range (0, len(alphp)):
        for j in range (0, len(alphp[l])):
          if (tex[i][0] == alphp[l][j]):
            r.append(l)
            r.append(j)
          if (tex[i][1] == alphp[l][j]):
            p.append(l)
            p.append(j)
      if (r[0] == p[0]):#в одной строке таблицы, слева направо шифрование
        res.append(alphp[r[0]][(r[1]+1)%6])
        res.append(alphp[p[0]][(p[1]+1)%6])
      if (r[1] == p[1]):#в одном столбце таблицы, шифрование сверху вниз
        res.append(alphp[(r[0]+1)%6][r[1]])
        res.append(alphp[(p[0]+1)%6][p[1]])
      if ((r[0] != p[0])and(r[1] != p[1])):#если в разных столбцах и строках 
        res.append(alphp[r[0]][p[1]])
        res.append(alphp[p[0]][r[1]])
      r = []
      p = []
    output = ''.join(res)
    print (output)
  if (t == 2):
    t = []
    for i in range(0, len(text), 2):#разбиение текста на биграммы
      for j in range(0,2):
        w.append(text[i+j])
      tex.append(w)
      w = []
    for i in range (0, len(tex)):
      for l in range (0, len(alphp)):
        for j in range (0, len(alphp[l])):
          if (tex[i][0] == alphp[l][j]):
            r.append(l)
            r.append(j)
          if (tex[i][1] == alphp[l][j]):
            p.append(l)
            p.append(j)
      if (r[0] == p[0]):#в одной строке таблицы, слева направо шифрование
        res.append(alphp[r[0]][(r[1]-1)%6])
        res.append(alphp[p[0]][(p[1]-1)%6])
      if (r[1] == p[1]):#в одном столбце таблицы, шифрование сверху вниз
        res.append(alphp[(r[0]-1)%6][r[1]])
        res.append(alphp[(p[0]-1)%6][p[1]])
      if ((r[0] != p[0])and(r[1] != p[1])):#если в разных столбцах и строках 
        res.append(alphp[r[0]][p[1]])
        res.append(alphp[p[0]][r[1]])
      r = []
      p = []
    output = ''.join(res)
    print (output)

def fillalph(fill):#создание алфавита для Плейфера
  alph =["а","б","в","г","д","е","ж","з","и","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ы","ь","э","ю","я"]
  fill = list(fill)
  t = 0
  for i in range(0,len(alph)):
    for j in range(0, len(fill)):
      if(alph[i] == fill[j]):
        t = 1
    if (t == 0):
      fill.append(alph[i])
    else:
      t = 0
  w = []
  fillf = []
  for i in range(0, len(fill), 6):
    for j in range(0,6):
      w.append(fill[i+j])
    fillf.append(w)
    w = []
  return fillf

def replace(rep, alph): #преобразование букв алфавита в их порядковый номер
  res = []
  for i in range (0, len(rep)):
    for j in range (0, len(alph)):
      if (rep[i] == alph[j]):
        res.append(j+1)
  return (res)

def replace2(rep, alph): #преобразование номера буквы алфавита в букву
  res = ''
  for i in range (0, len(rep)):
    for j in range (0, len(alph)):
      if (int_r(rep[i]-1) == j):
        res = res + alph[j]
  return (res)

alph = ["А","Б","В","Г","Д","Е","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я", "а","б","в","г","д","е","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я", "-",",",".", " ", "–"]
#alph = ["а","б","в","г","д","е","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
print ("Выбрать шифр: \n 1. Матричный шифр \n 2. Шифр Плэйфера – шифр биграммной замены")
t = int(input())
print("Введите текст:")
text = input()
if (t == 1):
  matr(text, alph)
if (t == 2):
  playfair(text)