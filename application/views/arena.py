from flask import Blueprint, render_template

from application.views.warriors import heroes
from implemented import arena


# ----------------------------------------------------------------
# initialize arena blueprint
arena_blueprint = Blueprint('arena_blueprint', __name__, template_folder='templates')


# ----------------------------------------------------------------
# arena views
@arena_blueprint.route("/fight/")
def start_fight():
    """
    View to start game and render fight page
    :return: rendered fight page
    """
    arena.start_game(player=heroes['player'], enemy=heroes['enemy'])
    return render_template('fight.html', title='fight', heroes=heroes)


@arena_blueprint.route("/fight/hit")
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


@arena_blueprint.route("/fight/use-skill")
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


@arena_blueprint.route("/fight/pass-turn")
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


@arena_blueprint.route("/fight/end-fight")
def end_fight():
    """
    View to end the battle
    :return: rendered main page
    """
    return render_template("index.html", heroes=heroes)
