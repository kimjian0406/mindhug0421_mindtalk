from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Flask 앱 초기화
app = Flask(__name__)

# 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hugmind.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 라우트와 인증 모듈 import
from app import routes, auth

