import mysql.connector # подключаем нужные библиотеки и соединяемся с локальной базой данных
from config_db import ht, us, pd, db

daba = mysql.connector.connect(
    host=ht,
    user=us,
    passwd=pd,
    database=db
) # берем данные обозначенные переменными из конфиг файла для подключения к бд

message_user = input() # переменная для ввода сообщения пользователем
# Курсор для взаимодействия с бд который нужен для создания запроса и получения результата
cursor = daba.cursor()

query = "SELECT GROUP_CONCAT(answer SEPARATOR ', ') AS answers FROM block1 WHERE question = %s" # ввод запроса где select
# выбор, group_concat - функция, позволяющая четко вывести строки, as answers - из значений answer в sql таблицах, block 1
# указание самой таблицы, where question - где вопрос ищется среди таблиц
query1 = "SELECT GROUP_CONCAT(answer SEPARATOR ', ') AS answers FROM block2 WHERE question = %s"
query2 = "SELECT GROUP_CONCAT(answer SEPARATOR ', ') AS answers FROM block3 WHERE question = %s"
query3 = "SELECT GROUP_CONCAT(answer SEPARATOR ', ') AS answers FROM block4 WHERE question = %s"
query4 = "SELECT GROUP_CONCAT(answer SEPARATOR ', ') AS answers FROM block5 WHERE question = %s"

value_to_search = message_user # присвиаем значение для поиска

try:
    cursor.execute(query, (value_to_search,)) # производим запрос через переданные значения и выборку
    result = cursor.fetchone()[0] #присваиваем значение результата
    cursor.execute(query1, (value_to_search,))
    result1 = cursor.fetchone()[0]
    cursor.execute(query2, (value_to_search,))
    result2 = cursor.fetchone()[0]
    cursor.execute(query3, (value_to_search,))
    result3 = cursor.fetchone()[0]
    cursor.execute(query4, (value_to_search,))
    result4 = cursor.fetchone()[0]

    if result:
        print(result) #если ответ найден, выводим результат
    elif result1:
        print(result1)
    elif result2:
        print(result2)
    elif result3:
        print(result3)
    elif result4:
        print(result4)
    else:
        print("Не поняла ваш вопрос. Попробуйте ещё раз")


except mysql.connector.Error as err:
    print(f"Ошибка при выполнении запроса: {err}")

finally:
    daba.close()
