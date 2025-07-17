def diffie_hellman():
  print("Введите a и n:")
  key = input()
  key = key.split(' ')
  a = int(key[0])
  n = int(key[1])
  print("Введите секретный ключ пользователя A")
  Ka = int(input())
  Ya = (a**Ka)%n #открытый ключ A
  print("Введите секретный ключ пользователя B")
  Kb = int(input())
  Yb = (a**Kb)%n #открытый ключ B
  gka = (Yb**Ka)%n
  gkb = (Ya**Kb)%n
  if gka == gkb:
    print("Ключи совпали. Общий секретный ключ: ", gka, "\nОткрытый ключ пользователя A ", Ya, "\nОткрытый ключ пользователя B ", Yb)
  else:
    print("Общего секретного ключа нет. Ошибка")


print("Обмен ключами по Диффи-Хеллману")
diffie_hellman()
