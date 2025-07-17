def trithemium(text, alph): #шифр Тритемия
  print ("1. Зашифровать \n2. Расшифровать")
  t = int(input())
  output = ""
  text = replace(text, alph)
  if (t == 1):
      for i in range (0, len(text)
        output = output + alph[(text[i]+i-1)%len(alph)]
        print (output)
  if (t == 2):
    for i in range (0, len(text)
      output = output + alph[(text[i]-i-1)%len(alph)]
      print (output)
 
def belazo(text, alph): #шифр Белазо
    text = replace(text, alph)
    print ("Введите ключ:")
    k = input ()
    key = replace(k, alph)
    print ("1. Зашифровать \n2. Расшифровать")
    t = int(input())
    output = ""
    sh = 0
    if (t == 1):
      for i in range (0, len(text)):
        output = output + alph[(text[i]+key[sh]-2)%len(alph)]
        sh += 1
        if (sh >= len(key)):
        sh = 0
        print (output)
    if (t == 2):
      for i in range (0, len(text)):
        output = output + alph[(text[i] - key[sh])%len(alph)]

def vigener(text, alph): #ширф Виженера
  print ("Введите ключ:")
  k = input ()
  print ("1. Зашифровать \n2. Расшифровать")
  t = int(input())
  output = ""
  if (t == 1):
    k =k + text
    key = replace(k, alph)
    text = replace(text, alph)
    for i in range (0, len(text)):
      output = output + alph[(text[i] + key[i] - 2)%len(alph)]
      print (output)
  if (t == 2):
    key = replace(k, alph)
    text = replace(text, alph)
    for i in range (0, len(text)):
      if ((i%2) != 0):
        output = output + alph[(text[i] - key[i] - 1)%len(alph)]
      else:
        output = output + alph[(text[i] - key[i])%len(alph)]
      key.append((text[i] - key[i])%len(alph))
    print (output)

alph = ["А","Б","В","Г","Д","Е","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я", "а","б","в","г","д","е","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я", "-",",",".", " ", "–"]
#alph
print ("Выбрать шифр: \n 1. Тритемия \n 2. Белазо \n 3. Виженера")
t = int(input())
print("Введите текст:")
text = input()
if (t == 1)
  trithemium(text, alph)
if (t == 2)
  belazo(text, alph)
if (t == 3)
  vigener(text, alph)
