import sqlite3

sql = "select * from surfers"	

banco = sqlite3.connect("surfersDB.sdb")
banco.row_factory = sqlite3.Row

cursor = banco.cursor()
cursor.execute(sql)

linhas = cursor.fetchall()

for linha in linhas:
	print("%s %s %s %s %s" %(linha["name"], linha["country"], linha["average"], linha["board"], linha["age"]))


