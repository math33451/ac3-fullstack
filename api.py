from flask import Flask, jsonify

app = Flask(__name__)

data = [
  {'id': 1, 'name': 'João', 'age': 25},
  {'id': 2, 'name': 'Maria', 'age': 30},
  {'id': 3, 'name': 'Pedro', 'age': 35},
]

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
