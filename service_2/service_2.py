from flask import Flask

app = Flask(__name__)

@app.route('/do_something_else')
def do_something_else():
    # Define the functionality of service_1 when called
    # This is a placeholder, put your logic here
    return "Service 2 did something! because the condition was dog"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
