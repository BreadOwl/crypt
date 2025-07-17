def numb(a): #переводим ключ в числовой вид
  b = []
  for i in range(len(a)):
    b.append(a[i])
  k = 0
  for i in range(len(a)):
    r = min(b)
    for j in range(len(a)): #место минимума
        if a[j] == r:
          d = j
    b.remove(r)
    a[d] = k
    k +=1
  return a
  

def verticalis(text, alph): #Вертикальная перестановка
  print ("Введите ключ:")
  key = input()
  key = replace(key, alph)
  key = numb(key)
  print(key)
  print ("1. Зашифровать \n2. Расшифровать")
  t = int(input())
  output = ""
  texte = []
  y = 0
  while y == 0: #дополнение недостающих звеньев
      if len(text)%len(key)==0:
        y = 1
      else:
        text = text + ' '
  if (t == 1):#зашифровка
    for o in range (0,len(text),len(key)):#разбиваем фразу на блоки равные длине ключа
      w = []
      for u in range(len(key)):
        w.append(text[o+u])
      texte.append(w)
    res1 = [0]*len(key)
    for u in range(len(key)):
      w = []
      for i in range(len(texte)):
        w.append(texte[i][key[u]])
      res1[key[u]] = w
    e = 0
    res = []
    for i in range (len(res1)):
      for p in range(len(key)):
        if key[p] == e:
          res.append(res1[p])
          e+=1
          break
    for i in range(len(res)):
      for j in range(len(res[i])):
        output = output + res[i][j]
    print (output)  
  if (t == 2): #расшифровка
    res = []
    r = len(text)//len(key)
    for o in range (0,len(text),r):#разбиваем фразу на блоки
      w = []
      for u in range(r):
        w.append(text[o+u])
      texte.append(w)
    for i in range(len(text)//len(key)): #создание списка результата
      w = []
      for j in range(len(key)):
        w.append(0)
      res.append(w)
    for i in range(len(texte)): #перестановка
      for t in range(len(key)):
        if key[t] == i:
          y = t
          break
      j = 0
      for l in range(len(res)):
        res[l][y] = texte[i][j]
        j +=1
    for i in range(len(res)):
      for j in range(len(res[i])):
        output = output + res[i][j]
    print (output) 

def cardano(text, alph): #Решетка Кардано
  print ("Введите ключ:")
  key = input()
  key = key.split(' ')
  print ("1. Зашифровать \n2. Расшифровать")
  t = int(input())
  output = ""
  if (t == 1):
    j = 0
    text=list(text)
    if len(text)<len(key):#заполнение текста до длины ключа
      for i in range(len(text),(len(key)-1)):
        text.append(alph[j%len(alph)])
        j+=1
    for i in range (len(text)):
      for q in range(len(key)):
        if str(i+1) == key[q]:
          key[q]=text[i]
    output = ''.join(key)
    print (output)
  if (t == 2):
    text=list(text)
    res = []
    for i in range(60):
      for j in range(len(key)):
        if i == (int(key[j])-1):
          res.append(text[j])
    output = ''.join(res)
    print (output)

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
#alph = ["а","б","в","г","д","е","ж","з","и","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
print ("Выбрать шифр: \n 1. Вертикальная перестановка \n 2. Решетка Кардано")
t = int(input())
print("Введите текст:")
text = input()
if (t == 1):
  verticalis(text, alph)
if (t == 2):
  cardano(text, alph)