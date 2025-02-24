from flask import Flask, render_template, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    app.logger.info("Homepage accessed")
    return """
    <html>
        <head>
            <title>Flask Web Server</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
                h1 { color: #333; }
                p { font-size: 18px; }
            </style>
        </head>
        <body>
            <h1>🚀 Flask Web Server Running in Docker! 🚀</h1>
            <p>Your Flask application is working perfectly inside a Docker container.</p>
        </body>
    </html>
    """

@app.route('/health')
def health_check():
    return jsonify({"status": "OK", "message": "Server is running"}), 200

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Page not found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
