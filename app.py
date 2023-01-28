from flask import Flask, render_template, redirect, url_for, request

from application.classes.unit.unit import PlayerUnit, EnemyUnit
# from application.views.arena import arena_blueprint
# from application.views.menu import menu_blueprint
# from application.views.warriors import warrior_blueprint
from implemented import unit_classes, equipment, arena

# ----------------------------------------------------------------
# initialize application and register blueprints
app = Flask(__name__)
heroes = {}
# app.register_blueprint(warrior_blueprint)
# app.register_blueprint(arena_blueprint)
# app.register_blueprint(menu_blueprint)


@app.route("/")
def menu_page():
    """
    Main menu view
    :return: main page
    """
    return render_template('index.html', title='main menu')


@app.route("/choose-hero/", methods=['POST', 'GET'])
def choose_hero():
    """
    View to choose a hero and redirect to enemy choosing page
    :return: rendered enemy choosing page
    """
    if request.method == 'POST':

        heroes['player']: PlayerUnit = PlayerUnit(
            name=request.form.get('name'),
            unit_class=unit_classes.get(request.form.get('unit_class'))
        )

        heroes['player'].equip_weapon(equipment.get_weapon(request.form.get('weapon')))
        heroes['player'].equip_armor(equipment.get_armor(request.form.get('armor')))

        return redirect(url_for('choose_enemy'))

    result = {
        "header": "Выберите героя",
        "classes": unit_classes.keys(),
        "weapons": equipment.get_weapons_names(),
        "armors": equipment.get_armors_names()
    }
    return render_template('hero_choosing.html', title='Choose hero', result=result)


@app.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy():
    """
    View to choose an enemy and redirect to fight page
    :return: rendered fight page
    """
    if request.method == 'POST':

        heroes['enemy']: EnemyUnit = EnemyUnit(
            name=request.form.get('name'),
            unit_class=unit_classes.get(request.form.get('unit_class'))
        )

        heroes['enemy'].equip_weapon(equipment.get_weapon(request.form.get('weapon')))
        heroes['enemy'].equip_armor(equipment.get_armor(request.form.get('armor')))

        return redirect(url_for('start_fight'))

    result = {
        "header": "Выберите противника",
        "classes": unit_classes.keys(),
        "weapons": equipment.get_weapons_names(),
        "armors": equipment.get_armors_names()
    }
    return render_template('hero_choosing.html', title='Choose enemy', result=result)


@app.route("/fight/")
def start_fight():
    """
    View to start game and render fight page
    :return: rendered fight page
    """
    arena.start_game(hero=heroes['player'], enemy=heroes['enemy'])
    return render_template('fight.html', title='fight', heroes=heroes)


@app.route("/fight/hit")
def hit():
    """
    view to hit enemy and render fight page
    :return: rendered fight page
    """
    if arena.game_is_running:
        result: str = arena.player_hit()
    else:
        result: str = arena.battle_result

    return render_template('fight.html', heroes=heroes, result=result)


@app.route("/fight/use-skill")
def use_skill():
    """
    View to use a skill and render the fight page
    :return: rendered fight page
    """
    if arena.game_is_running:
        result: str = arena.player_use_skill()
    else:
        result: str = arena.battle_result
    return render_template('fight.html', heroes=heroes, result=result)


@app.route("/fight/pass-turn")
def pass_turn():
    """
    View to pas turn and render the fight page
    :return: rendered fight page
    """
    if arena.game_is_running:
        result: str = arena.next_turn()
    else:
        result: str = arena.battle_result
    return render_template('fight.html', heroes=heroes, result=result)


@app.route("/fight/end-fight")
def end_fight():
    """
    View to end the battle
    :return: rendered main page
    """
    return render_template("index.html", heroes=heroes)


# ----------------------------------------------------------------
# run application
if __name__ == "__main__":
    app.run()
