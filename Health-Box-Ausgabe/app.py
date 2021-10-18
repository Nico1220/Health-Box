from flask import Flask, jsonify, request, abort, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/login', methods=['POST'])
def calculate_bmi():
    # request enthält die vom Client übergebenen Daten
    # Parmeter force ...Mimetype ignorieren und immer als JSON parsen
    data = request.get_json(force=True)
    try:
        user = data['user']
        password = data['password']
    except:
        abort(500, "paramerzers user and password needed")

    if ((user == "user42") and (password == "geheim")):
         return jsonify({'result': "true"})
    else:
         return jsonify({'result': "false"})


if __name__ == "__main__":
    app.run()
