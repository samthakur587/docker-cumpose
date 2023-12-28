from flask import Flask

app = Flask(__name__)

@app.route('/do_another_thing')
def do_another_thing():
    # Define the functionality of service_1 when called
    # This is a placeholder, put your logic here
    return "Service 3 did something! because the condition was neither cat nor dog"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)
