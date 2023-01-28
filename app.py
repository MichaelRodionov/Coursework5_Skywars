from flask import Flask

from application.views.arena import arena_blueprint
from application.views.menu import menu_blueprint
from application.views.warriors import warrior_blueprint


# ----------------------------------------------------------------
# initialize application and register blueprints
app = Flask(__name__)
app.register_blueprint(warrior_blueprint)
app.register_blueprint(arena_blueprint)
app.register_blueprint(menu_blueprint)


# ----------------------------------------------------------------
# run application
if __name__ == "__main__":
    app.run()
