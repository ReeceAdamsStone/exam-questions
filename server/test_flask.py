
import flask from Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """
This function defines a basic Flask route with a single endpoint ("/") that
returns a 'Hello, World!' message.
    """
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
