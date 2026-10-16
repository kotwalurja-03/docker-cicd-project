
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head><title>Docker CI/CD Project</title></head>
        <body>
            <h1>My Docker DevOps Project</h1>
            <p>Python application running successfully!</p>
            <p>Docker + GitHub Actions CI/CD</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
