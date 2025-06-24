from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "22554523"))
API_HASH = environ.get("API_HASH", "d3cd72e44e4160ce1ee0b7947e8f2d89")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "7460363208")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://eno2223456:7Cdmqig5Ih2vrqW4@cluster0.ccpmee5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
