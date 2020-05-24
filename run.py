from flask_script import Manager, Server
from app import app

manager = Manager(app)

port = int(os.environ.get("PORT", 5000))
manager.add_command("runserver", Server(
    use_reloader = True,
    host = '0.0.0.0',
    port = port)
)

if __name__ == "__main__":
    manager.run()
