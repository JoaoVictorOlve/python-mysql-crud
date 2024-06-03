import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="notes"
)

mycursor = mydb.cursor()

# mycursor.execute("""CREATE TABLE Users (
#   id INT AUTO_INCREMENT PRIMARY KEY,
#   username VARCHAR(20) UNIQUE NOT NULL,
#   password VARCHAR(200) NOT NULL,
#   name VARCHAR(60) NOT NULL,
#   email VARCHAR(50) UNIQUE NOT NULL,
#   created_on DATETIME DEFAULT CURRENT_TIMESTAMP
# );
# """)

# mycursor.fetchall()

# mycursor.execute("""CREATE TABLE produtos (
#   id INT AUTO_INCREMENT PRIMARY KEY,
#   descricao VARCHAR(75),
#   qtd INT,
#   preco DOUBLE
# );
# """)

# mycursor.fetchall()