import os
from src.server import Server

settings_module = os.getenv('APP_SETTINGS_MODULE')

new_server = Server(settings_module)
app = new_server.app

flask_environment = os.getenv('FLASK_ENV')
if flask_environment == 'production':
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    app.run()