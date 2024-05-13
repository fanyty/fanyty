import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, insatance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py',silent=True)
        
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    return app