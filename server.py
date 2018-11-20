import psycopg2
import uuid
try:
    conn = psycopg2.connect("dbname='dbkwmnvo' user='dbkwmnvo' host='stampy.db.elephantsql.com' password='Svlw7QnOgENeOI6XnC2obr5GY8ojNINR'")
    print("подключился к базе данных")
except:
    print("не подключился к базе данных")
key = str(uuid.uuid4())
cur = conn.cursor()
res = cur.execute("INSERT INTO key (domain, domain1, chat ) VALUES (%s,%s,%s)", ('1','1',key))
conn.commit()
