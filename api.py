import os
from flask import Flask, request, redirect, url_for, jsonify

UPLOAD_FOLDER = '/tmp'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file :

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return redirect(url_for('upload_file',
                                filename=file.filename))

@app.route('/', methods=['GET'])
def get_list():
    onlyfiles = [f for f in os.listdir(UPLOAD_FOLDER) if os.path.isfile(os.path.join(UPLOAD_FOLDER, f))]
    return jsonify(onlyfiles)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

