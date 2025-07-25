# crypt
<h1>Реализованные шифры</h1>

В рамках лабораторных работ по предмету "Программирование критографических алгоритмов" (2022) были реализованы различные шифры и цифровые подписи в виде девяти отдельных консольных одноразовых скриптов на языке Python.

Для каждого шифра реализованы процессы шифрования и дешифровки.

Запуск:
```
python <имя файла>
```
______
<b>Ассиметричные шифры</b> представляют RSA и схема Эль-Гамаля (Elgamal). Рассчитанные ключи заранее вписаны в код. Алфавит для вводимых для шифрования символов ограничен русскими заглавными и строчными буквами и некоторыми спец символами ("-", ",", ".", " ", "–"). 

RSA — популярный метод асимметричного шифрования, основанный на сложностях факторизации больших чисел. Используется пара ключей: открытый для шифрования и закрытый для расшифровки. Безопасность обеспечивается сложностью нахождения простых сомножителей большого числа, которое открыто публикуется.

Эль-Гамаль — алгоритм шифрования, использующий проблему дискретного логарифма. В классическом варианте применяется умножение в конечном поле, а в современных реализациях часто используются эллиптические кривые. Работает аналогично RSA, обеспечивая надёжную защиту при меньшей длине ключей.
______
Среди <b>комбинационных шифров</b> - Магма и Кузнечик (ГОСТ 34.13-2018). Алфавит ограничен строчными русскими, английскими буквами и цифрами.

Магма — российский стандарт блочного шифрования, 64-разрядный блочный шифр с длиной ключа 256 бит, построенный на сетевой структуре Фейстеля. Использует собственные таблицы замены (S-блоки).

Кузнечик — аналогичный российский стандарт блочного шифрования. Представляет собой 128-разрядный шифр с размером блока также 128 бит. Отличительной особенностью является использование линейных преобразований над конечным полем GF(2^8), а также собственных S-блоков.
______
В файле <b>"Обмен ключами по алгоритму Diffie–Hellman"</b> реализован обмен ключами по протоколу Диффи-Хеллмана, обеспечивающий безопасный способ обмена криптографическими ключами между двумя пользователями («A» и «B») через открытый канал связи.
______
<b>Цифровая подпись ГОСТ Р 34 10-94</b> - государственный стандарт Российской Федерации, который устанавливает процедуры выработки и проверки электронной цифровой подписи (ЭЦП) сообщений (документов), передаваемых по незащищённым телекоммуникационным каналам общего пользования. Алфавит ограничен русскими строчными буквами.
______
Помимо отечественной цифровой подписи, отдельно в <b>цифровых подписях</b> реализованы подписи RSA и схема Эль-Гамаля (Elgamal). Алфавит ограничен русскими заглавными и строчными буквами и некоторыми спец символами ("-", ",", ".", " ", "–").

Цифровая подпись RSA основана на одноимённом асимметричном шифровании. Подпись формируется путём вычисления хэш-функции от подписываемого документа и последующего её шифрования приватным ключом отправителя. Проверка подписи осуществляется обратным процессом — расшифровкой полученного результата открытым ключом и сравнением хэша с ожидаемым значением.

Подпись Эль-Гамаля строится на проблемах дискретного логарифма. Процесс включает создание подписи путём формирования двух значений, зависящих от случайно выбранного параметра и хэша подписываемых данных. Проверка заключается в проверке соответствия полученных величин определённым условиям, связанным с параметрами подписи и публичным ключом владельца.
______
<b>Шифр Плейфера</b> — ручная симметричная техника шифрования, в которой использована замена биграмм. Для шифрования необходим ключ, представляющий собой таблицу букв (в русском алфавите без букв "Й" и "Ъ"). Процесс шифрования сводится к поиску биграммы в таблице и замене её на пару букв, образующих с исходной биграммой прямоугольник. Алфавит ограничен русскими заглавными и строчными буквами и некоторыми спец символами ("-", ",", ".", " ", "–"). Единственная программа, используящая стороннюю библиотеку numpy.
______
Представленные <b>шифры многозначной замены</b> - Тритемия, Белазо, Виженера. Алфавит ограничен русскими заглавными и строчными буквами и некоторыми спец символами ("-", ",", ".", " ", "–").

Тритемия — классический шифр простой замены, каждая буква текста замещается другой согласно фиксированному алфавиту, что делает шифр легко вскрываемым методом частотного анализа.

Белазо и Виженера — классические полибуквенные шифры, отличающиеся использованием ключевого слова для сдвига каждой буквы исходного текста по циклически повторяемому правилу. Шифр Виженера отличается большей стойкостью благодаря переменному сдвигу, тогда как Белазо представляет упрощённую версию, применяя одну таблицу Цезаря для всех символов.
______
Простые <b>шифры однозначной замены</b> - атбаш, шифр Цезаря и квадрат Полибия. Алфавит ограничен русскими заглавными и строчными буквами и некоторыми спец символами ("-", ",", ".", " ", "–").

Атбаш — древний шифр простой замены, в котором каждая буква алфавита заменяется противоположной ей буквой. Например, первая буква меняется на последнюю, вторая — на предпоследнюю и так далее.

Шифр Цезаря — самый известный шифр простой замены, при котором каждая буква текста смещается на фиксированное число позиций вправо или влево по алфавиту. В программе можно задать сдвиг.

Квадрат Полибия — система шифрования, разработанная греческим историком Полибием. Каждое письмо представляется координатами клетки квадрата 5×6, заполненного алфавитом.
______
В <b>шифрах перестановки</b> вертикальная перестановка и решетка Кардано. Алфавит ограничен русскими заглавными и строчными буквами и некоторыми спец символами ("-", ",", ".", " ", "–"). 

Вертикальная перестановка — это метод шифрования, при котором текст записывается построчно в столбцы матрицы, а затем считывается по строкам. Порядок чтения строк заранее определяется ключевым словом или числом. В программном виде фраза разбивается на блоки и переставляется в соотвествии с ключом.

Решётка Кардано — старинный метод шифрования, предложенный итальянским учёным Джероламо Кардано. Представляет собой специальную трафаретную маску с отверстиями, накладываемую на лист бумаги. Через отверстия последовательно вписываются буквы сообщения, а свободные места заполняются произвольными символами. 
