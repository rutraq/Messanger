import psycopg2
try:
    conn = psycopg2.connect("dbname='dbkwmnvo' user='dbkwmnvo' host='stampy.db.elephantsql.com' password='Svlw7QnOgENeOI6XnC2obr5GY8ojNINR'")
    print("подключился к базе данных")
except:
    print("не подключился к базе данных")
a = str(input("Введите имя для поиска "))
cur = conn.cursor()
res = cur.execute("SELECT * FROM users domain where lower(domain) like lower('%Desmond%')") #поиск информации
#res = cur.execute("SELECT * FROM users")
row = cur.fetchone()
print(row)        # Вывод информации с мансами
for entry in cur: #
    print(entry)  #

#print(row) #простой вывод

#res = cur.execute("INSERT INTO users(count ,domain ,name ,surname) VALUES (%s,%s,%s,%s)", ("2", "DESMOND", "ARTUR", "Youzefovich"))  #Добавление информации
#conn.commit()

conn.close() # Разрываем подключение.