from app.utils.firebase_config import init_firebase
from flask import Flask, request, jsonify
import os

def create_app():
    app = Flask(__name__)
    app.config["ENV"] = os.getenv("FLASK_ENV", "development")
 
    # init firebase (reads serviceAccountKey.json or GOOGLE_APPLICATION_CREDENTIALS)
    init_firebase(app)

    from .controllers.user_controller import user_bp

    app.register_blueprint(user_bp)

    @app.route('/')
    def home():
        return jsonify({"message": "Firebase is running!"})

    @app.route('/health', methods=['GET'])
    def health():
        return {"status": "ok"}
    
    return app


