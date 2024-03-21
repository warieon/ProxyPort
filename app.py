from flask import Flask
from Routes.NHI.Patient import Patient

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the ProxyPort API'

app.register_blueprint(Patient)

if __name__ == '__main__':
    app.run(debug=True)