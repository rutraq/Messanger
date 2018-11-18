import psycopg2
try:
    conn = psycopg2.connect("dbname='dbkwmnvo' user='dbkwmnvo' host='stampy.db.elephantsql.com' password='Svlw7QnOgENeOI6XnC2obr5GY8ojNINR'")
    print("подключился к базе данных")
except:
    print("не подключился к базе данных")
#a = str(input("Введите count "))
#b = str(input("Введите domain"))
#c = str(input("Введите name"))
#d = str(input("Введите username"))
cur = conn.cursor()
#res = cur.execute("SELECT * FROM users domain where lower(domain) like lower('%Desmond%')") #поиск информации
res = cur.execute("SELECT * FROM users")
row = cur.fetchone()

#print(row) #простой вывод

#res = cur.execute("INSERT INTO users(count ,domain ,name ,surname) VALUES (%s,%s,%s,%s)", (a, b, c, d))  #Добавление информации
#conn.commit()
#row = cur.fetchone()
print(row[1])        # Вывод информации с мансами
for entry in cur:
    print(entry[1])

conn.close() # Разрываем подключение.



# import psycopg2
# try:
#     conn = psycopg2.connect("dbname='dbkwmnvo' user='dbkwmnvo' host='stampy.db.elephantsql.com' password='Svlw7QnOgENeOI6XnC2obr5GY8ojNINR'")
#     print("подключился к базе данных")
# except:
#     print("не подключился к базе данных")
# #a = str(input("Введите domain для поиска :"))
# cur = conn.cursor()
# #res = cur.execute("SELECT * FROM users")
# res = cur.execute("SELECT * FROM users WHERE DOMAIN ='arturdesmond'")
# row = cur.fetchone()
# if not row:
#     print('не найдено')
# else:
#     print('найдено')
#
# res = cur.execute("SELECT * FROM users")
# row = cur.fetchone()
# print(row)