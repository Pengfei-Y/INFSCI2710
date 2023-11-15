from flask import Flask
from apps.admin import admin_bp
from apps.user import user_bp
from apps.business import business_bp

app = Flask(__name__)
app.secret_key = 'sakdfjklasdjfklasjdfjiusiodafu'
# register blueprint
app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)
app.register_blueprint(business_bp)

if __name__ == '__main__':
    app.run()
