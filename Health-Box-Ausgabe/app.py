from flask import Flask, jsonify, request, abort, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/health-box', methods=['POST'])
def calculate_bmi():
    # request enthält die vom Client übergebenen Daten
    # Parmeter force ...Mimetype ignorieren und immer als JSON parsen
    data = request.get_json(force=True)
    try:
<<<<<<< Updated upstream
        temp = data['temp']
        puls = data['puls']
=======
        temp = data['temperature']
        puls = data['pulsoxymeter']
>>>>>>> Stashed changes
    except:
        abort(500, "paramerzers needed")

if __name__ == "__main__":
    app.run()
