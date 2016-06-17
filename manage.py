
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

import warcraft
from warcraft import create_app, db
from warcraft.models import User, Follow, Role, Permission, Post, Comment

app = create_app()
config = app.config

manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Follow=Follow, Role=Role,
                Permission=Permission, Post=Post, Comment=Comment)
         
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.option('-d', '--debug', action='store_true', help="Start the web server in debug mode")
@manager.option('-p', '--port', default=config.get("WARCRAFT_WEBSERVER_PORT"),  help="Specify the port on which to run the web server")
@manager.option('-w', '--workers', default=config.get("WARCRAFT_WORKERS", 16),  help="Number of gunicorn web server workers to fire up")
@manager.option('-t', '--timeout', default=config.get("WARCRAFT_WEBSERVER_TIMEOUT"),  help="Specify the timeout (seconds) for the gunicorn web server")
def runserver(debug, port, timeout, workers):
    """Starts a WarCraft web server"""
    debug = debug or config.get("DEBUG")
    if debug:
        app.run(host='0.0.0.0', port=int(port),debug=True)
    else:
        pass

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    manager.run()