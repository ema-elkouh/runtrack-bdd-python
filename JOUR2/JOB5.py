import mysql.connector

db = mysql.connector.connect(host = "localhost", user = "root", password = "meschats", database = "LaPlateforme")


cursor = db.cursor()
req = "SELECT CONCAT('La superficie de La Plateforme est de ', SUM(superficie), ' m2') as resultat FROM etage;"
cursor.execute(req)
results = cursor.fetchall()
print(results)
cursor.close()