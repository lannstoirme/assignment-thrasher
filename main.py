import os

from flask import Flask, request, send_file
from model import extend


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return send_file('index.html')
    data = request.form.get('text')
    return extend(data)



if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))