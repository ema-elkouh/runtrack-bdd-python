import mysql.connector

db = mysql.connector.connect(host = "localhost", user = "root", password = "meschats", database = "LaPlateforme")


cursor = db.cursor()
req = "SELECT * FROM Etudiant"
cursor.execute(req)
results = cursor.fetchall()
print(results)
cursor.close()




