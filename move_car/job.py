from sqlalchemy import create_engine
from sqlalchemy import URL
from get_pass import mysql_login

username1p, password1p = mysql_login()


url_object = URL.create(
	"mysql+pymysql",
	username=username1p,
	password=password1p,  # plain (unescaped) text
	host="localhost",
	database="cityopeen",
	port="3308"
)

# Create the engine
engine = create_engine(url_object)

# Test the connection
try:
	connection = engine.connect()
	print("Connected to MySQL database successfully!")
	connection.close()
except Exception as e:
	print("Error connecting to MySQL database:", str(e))
