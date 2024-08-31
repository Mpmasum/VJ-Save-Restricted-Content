import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22594398"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3a2408d97d6a222d87766dac2da302df")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://janubapu5:janubapu5@cluster0.ld2ya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
