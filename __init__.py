from flask import Flask

# The following create a Flask App with __name__ refering to "PYTHON_TEST"
# or you can also write this as:  app = Flask("PYTHON_TEST")
app = Flask(__name__)

from app import routes
