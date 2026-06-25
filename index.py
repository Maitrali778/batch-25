from flask import Flask

# Elastic Beanstalk looks specifically for the 'application' callable
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, World! This is a simple Python app on Elastic Beanstalk.'

if __name__ == '__main__':
    # Beanstalk routes traffic internally, usually looking for port 5000
    application.run(host='0.0.0.0', port=5000)
