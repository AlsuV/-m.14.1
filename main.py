import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# ----
# Заполните её 10 записями:
# for i in range(11):
#     if i != 0:
#         cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"newuser{i}", f"ex@gmail.com{i}", f"{i}0", "1000"))

# ----
# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, "newuser2"))
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, "newuser4"))
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, "newuser6"))
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, "newuser8"))
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, "newuser10"))

# ----
# Удалите каждую 3ую запись в таблице начиная с 1ой:
# cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser1",))
# cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser4",))
# cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser7",))
# cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser10",))

# ----
# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
cursor.execute("SELECT username, age FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user in users:
    print(user)
connection.commit()
connection.close()

