import pymysql

con = pymysql.connect(host='localhost',database='jesftechnology',user='root',password='')

cursor = con.cursor()

cursor.execute("SELECT codImpressora FROM impressoras WHERE trabalhando = 'Nao'")

for x in cursor:
    print(x)