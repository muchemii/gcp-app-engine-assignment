import flask
from datetime import datetime
import os

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = flask.Flask(__name__)

@app.route("/")
def hello():
    """Return a friendly HTTP greeting with HTML."""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>GCP App Engine Application</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                text-align: center;
                max-width: 600px;
            }
            h1 {
                color: #667eea;
                margin-bottom: 20px;
            }
            .info {
                background: #f5f5f5;
                padding: 20px;
                border-radius: 5px;
                margin: 20px 0;
            }
            .status {
                color: #28a745;
                font-weight: bold;
                font-size: 18px;
            }
            .footer {
                margin-top: 30px;
                color: #666;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Google App Engine Application</h1>
            <div class="info">
                <p class="status">✅ Application Successfully Deployed!</p>
                <p><strong>Student:</strong> SAITOTI NJAPIT</p>
                <p><strong>Registration Number:</strong> 23/05817</p>
                <p><strong>Course:</strong> CPP 3102 - General</p>
                <p><strong>Current Time:</strong> {}</p>
                <p><strong>Environment:</strong> {}</p>
            </div>
            <div class="footer">
                <p>This application is deployed on Google Cloud Platform App Engine</p>
                <p>Built with Python Flask Framework</p>
            </div>
        </div>
    </body>
    </html>
    """.format(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Production (App Engine)" if os.environ.get("GAE_ENV") else "Development"
    )
    return html_content

@app.route("/health")
def health():
    """Health check endpoint."""
    return {"status": "healthy", "service": "app-engine-python"}, 200

if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)