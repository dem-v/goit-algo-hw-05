# Завдання 3

В цьому завданні було порівняно швидкість виконання 
алгоритмів Кнута-Морріса-Пратта, Боєра-Мура та Рабін-Карпа
на запропонованих текстах (статті 1 та 2). 
Під час перевірки я використав тестові підмножини для пошуку:

q1 = "задачу можливо вирішити" 

Присутній у статті 1, висока кількість подібних хешів

q2 = "або задачу або"

Відсутній у статті 1, висока кількість подібних хешів

q3 = "можливість зберігати дані"

Присутній у статті 2, висока кількість подібних хешів

q4 = "стрруктура дуже"

Відсутній у статті 2, висока кількість подібних хешів

q5 = "exponentialSearch"

Присутній у статті 1, низька кількість подібних хешів, відсутній у статті 2.

q6 = "zzZZzz"

Присутній у статті 1, низька кількість подібних хешів, відсутній у статті 2.


Маємо наступні результати:

| Етап тестування                             | Пошук Кнута-Морріса-Пратта | Пошук Боєра-Мура | Пошук Рабін-Карпа |
|---------------------------------------------|----------------------------|------------------| ----------------- | 
| позитивний кейс, текст 1 | 0.0153 | 0.0032 | 0.0330|
| негативний кейс, текст 1 | 0.0202 | 0.0062 | 0.0348|
| позитивний кейс, текст 2 | 0.0094 | 0.0027 | 0.0249|
| негативний кейс, текст 2 | 0.0220 | 0.0062 | 0.0535|
| додатковий позитивний кейс, текст 1 | 0.0065 | 0.0017 | 0.0207|
| додатковий негативний кейс, текст 1 | 0.0116 | 0.0072 | 0.0352|
| додатковий позитивний кейс, текст 2 | 0.0163 | 0.0037 | 0.0502|
| додатковий негативний кейс, текст 2 | 0.0198 | 0.0094 | 0.0460|


Згідно з результатами, наведеними в таблиці, найшвидшим виявився пошук Боєра-Мура.
