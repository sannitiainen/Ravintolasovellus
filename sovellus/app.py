from flask import Flask
from os import getenv

print(getenv("SECRET_KEY"))

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

import routes