from flask import Flask, jsonify


class Server(object):
    
    app = None

    def __init__(self, settings_module):

        self.app = Flask(__name__)
        self.app.secret_key = '7q%3=;8J+X5:f.+pU9e!;6x:E*n_9^Ky0~.R'

        # Load the config file specified by the APP environment variable
        self.app.config.from_object(settings_module)
        # Load the configuration from the instance folder
        #if app.config.get('TESTING', False):
        #    app.config.from_pyfile('config-testing.py', silent=True)
        #else:
        #    app.config.from_pyfile('config.py', silent=True)

        @self.app.route('/')
        def home():
            return jsonify({
                "ping": "pong",
                "ENV": self.app.config.get('ENV'),
                "DEBUG": self.app.config.get('DEBUG'),
                "TESTING": self.app.config.get('TESTING'),
                "APP_ENV": self.app.config.get('APP_ENV'),
                "BASE_DIR": self.app.config.get('BASE_DIR'),
                "MEDIA_DIR": self.app.config.get('MEDIA_DIR'),
                "POSTS_IMAGES_DIR": self.app.config.get('POSTS_IMAGES_DIR'),
            })

            