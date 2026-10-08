from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Module 1 Assignment</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                text-align: center;
                padding-top: 100px;
            }

            .container {
                background: white;
                width: 600px;
                margin: auto;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }

            h1 {
                color: #1f2937;
            }

            .status {
                color: green;
                font-weight: bold;
                font-size: 20px;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>DevOps Module 1 Assignment</h1>

            <p class="status">
                Application Running Successfully
            </p>

            <p><strong>Environment:</strong> Local Development</p>
            <p><strong>Technology:</strong> Python Flask</p>
            <p><strong>Port:</strong> 5000</p>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)