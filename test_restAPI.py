from flask import Flask, jsonify

app = Flask(__name__)


Body = [
    {
        'message': 'this was customized'
    }
]

@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'body': Body})

if __name__ == '__main__':
    app.run(debug=True)
