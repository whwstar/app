from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap


mail = Mail()
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
#csrf = CSRFProtect()
bootstrap = Bootstrap()



@login_manager.user_loader
def load_user(user_id):
    from monitor.models import User
    user = User.query.get(int(user_id))
    return user
