import os
basedir=os.path.abspath(os.path.dirname(__file__))


class Config :
    # SECRET_KEY='a_secret_key'
    # DEBUG=True
    SQLALCHEMY_DATABASE_URI= 'sqlite:///'+os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

