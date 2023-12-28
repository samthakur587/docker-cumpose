from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_condition')
def get_condition():
    # Add your condition checking logic here
    # For example, a simplified condition check:
    condition = 'dog'
    return jsonify({'condition': condition})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
