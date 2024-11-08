from flask import Flask, jsonify

app = Flask(__name__)

provinces = [
    {"name": "Tehran", "area": 18691, "population": 13834500},
    {"name": "Isfahan", "area": 107029, "population": 5200000},
    {"name": "Khorasan Razavi", "area": 118000, "population": 6220000},
    {"name": "Persia", "area": 122608, "population": 5000000},
    {"name": "East Azerbaijan", "area": 67000, "population": 4400000},
]

@app.route('/provinces', methods=['GET'])
def get_provinces():
    return jsonify(provinces)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

