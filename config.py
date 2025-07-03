import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une-cle-secrete-tres-complexe-pour-le-projet'
    MAIL_SERVER = 'smtp.proton.me'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'thanosford@proton.me'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # Met le mot de passe en variable d’environnement
    MAIL_DEFAULT_SENDER = ('MaBanque BNP Paribas', 'thanosford@proton.me')