print("Hello World\nThis is the main branch!")

print("This is part of feature-login branch")

print("This was added to main and feature branch isnt updated yet")

print("Testiing")

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    debug_mode = os.getenv('DEBUG', 'False')
    return f"Hello, World! Debug mode is {debug_mode}"

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug_mode = os.getenv('DEBUG')
    app.run(host='0.0.0.0', port=port, debug=(debug_mode == 'True'))
