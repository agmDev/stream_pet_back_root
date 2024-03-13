from flask import Flask
from flask_migrate import Migrate


from .models import db
from .blueprint.user.user import user_bp

app = Flask(__name__)
app.config.from_object('app.config.DevConfig')


migrate = Migrate(app, db)
db.init_app(app)

app.register_blueprint(user_bp, url_prefix='/user')

if __name__ == '__main__':
    app.run()
