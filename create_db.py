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

# INSERT INTO produtos (descricao, qtd, preco) VALUES
# ('Arroz', 10, 19.99),
# ('Frango', 20, 29.99),
# ('Batata', 15, 14.99),
# ('Corinthians', 5, 49.99),
# ('Ovo', 8, 9.99);

# INSERT INTO Users (username, password) 
# VALUES ('ademilson', 'senha123');