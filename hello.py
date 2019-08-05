from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/public')
def public():
    return jsonify({'access_type': 'public'})


@app.route('/protected')
def protected():
    return jsonify({'access_type': 'protected'})


@app.route('/admin')
def admin():
    return jsonify({'access_type': 'admin'})


if __name__ == "__main__":
    app.run(debug=True, port=5667)
