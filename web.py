from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix = "/")
#app.secret_key = "inception"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#db = SQLAlchemy(app)

#class users(db.Model):
#    _id = db.Column("id", db.Integer, primary_key = True)
#    name = db.Column(db.String(100))
#    mailID = db.Column(db.String(100))

    #def __init__(self, name, mailID):



if __name__ == "__main__":
#    db.create_all()
    app.run(debug = True)
