def atbash(text, alph): #атбаш, работает и на зашифровку и на расшифровку
  res = ""
  for i in range (0, len(text)):
    for j in range (0, len(alph)):
      if(text[i] == alph[j]):
        res  = res + alph[len(alph) - 1 - j]
        break
  print(res)



def cezar(text, alph): #шифр Цезаря
  print ("1. Зашифровать \n2. Расшифровать")
  t = int(input())
  print("Введите ключ:")
  k = int(input())
  res = ""
  if (t == 1):
    for i in range (0, len(text)):
      for j in range (0, len(alph)):
        if (text[i] == alph[j]):
          res  = res + alph[(j+k)%len(alph)]
          break
    print(res)
  if (t == 2):
    for i in range (0, len(text)):
      for j in range (0, len(alph)):
        if(text[i] == alph[j]):
          res  = res + alph[(j-k)%len(alph)]
          break
    print(res)


def polybius(text): #квадрат Полибия
  alph = [[11,"а"],[12,"б"],[13,"в"],[14,"г"],[15,"д"],[16,"е"],[21,"ж"],[22,"з"],[23,"и"],[24,"й"],[25,"к"],[26,"л"],[31,"м"],[32,"н"],[33,"о"],[34,"п"],[35,"р"],[36,"с"],[41,"т"],[42,"у"],[43,"ф"],[44,"х"],[45,"ц"],[46,"ч"],[51,"ш"],[52,"щ"],[53,"ъ"],[54,"ы"],[55,"ь"],[56,"э"],[61,"ю"],[62,"я"]]
  res = ""
  print ("1. Зашифровать \n2. Расшифровать")
  t = int(input())
  if (t == 1):
    for i in range (0, len(text)):
      for j in range (0, len(alph)):
        if(text[i] == alph[j][1]):
          res = res + str(alph[j][0]) + " "
          break
    print(res)
  if (t == 2):
    a = []
    r = ""
    for w in range (0, len(text)):#для удобства преобразование текста с цифрами в массив
      if (text[w] == " "):
        a.append(r)
        r = ""
      else:
        r = r + text[w]
    for i in range (0, len(a)):
      for j in range (0, len(alph)):
        if(a[i] == str(alph[j][0])):
          res = res + alph[j][1]
          break
    print(res)


alph = ["А","Б","В","Г","Д","Е","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я", "а","б","в","г","д","е","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я", "-",",",".", " ", "–"]
print ("Выбрать шифр: \n 1. Атбаш \n 2. Цезарь \n 3. Квадрат Полибия")
t = int(input())
print("Введите текст:")
text = input()
if (t == 1):
  atbash(text, alph)
if (t == 2):
  cezar(text, alph)
if (t == 3):
  polybius(text)