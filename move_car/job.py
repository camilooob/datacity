from sqlalchemy import create_engine
from sqlalchemy import URL

url_object = URL.create(
	"mysql",
	username="opeencamilo",
	password="QHb-MfJjFQea3XBUo3NTf*We4",  # plain (unescaped) text
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
