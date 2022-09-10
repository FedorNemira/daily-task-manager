from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from apps.main import views
from apps.main.models import db

from config import APP_HOST
from config import APP_PORT
from config import POSTGRES_URL

app = Flask(__name__)
CORS(app)
app.register_blueprint(views.main, url_prefix='')

app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True, host=APP_HOST, port=APP_PORT)
