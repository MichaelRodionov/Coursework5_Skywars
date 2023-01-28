# from flask import Blueprint, request, render_template, redirect, url_for
#
# from application.classes.unit.unit import PlayerUnit, EnemyUnit
# from implemented import unit_classes, equipment
#
#
# # ----------------------------------------------------------------
# # initialize warrior blueprint
# warrior_blueprint = Blueprint('warrior_blueprint', __name__, template_folder='templates')
# heroes = {}
#
#
# # ----------------------------------------------------------------
# # warrior views
# @warrior_blueprint.route("/choose-hero/", methods=['POST', 'GET'])
# def choose_hero():
#     """
#     View to choose a hero and redirect to enemy choosing page
#     :return: rendered enemy choosing page
#     """
#     if request.method == 'POST':
#
#         heroes['player']: PlayerUnit = PlayerUnit(
#             name=request.form.get('name'),
#             unit_class=unit_classes.get(request.form.get('unit_class'))
#         )
#
#         heroes['player'].equip_weapon(equipment.get_weapon(request.form.get('weapon')))
#         heroes['player'].equip_armor(equipment.get_armor(request.form.get('armor')))
#
#         return redirect(url_for('warrior_blueprint.choose_enemy'))
#
#     result = {
#         "header": "Выберите героя",
#         "classes": unit_classes.keys(),
#         "weapons": equipment.get_weapons_names(),
#         "armors": equipment.get_armors_names()
#     }
#     return render_template('hero_choosing.html', title='Choose hero', result=result)
#
#
# @warrior_blueprint.route("/choose-enemy/", methods=['post', 'get'])
# def choose_enemy():
#     """
#     View to choose an enemy and redirect to fight page
#     :return: rendered fight page
#     """
#     if request.method == 'POST':
#
#         heroes['enemy']: EnemyUnit = EnemyUnit(
#             name=request.form.get('name'),
#             unit_class=unit_classes.get(request.form.get('unit_class'))
#         )
#
#         heroes['enemy'].equip_weapon(equipment.get_weapon(request.form.get('weapon')))
#         heroes['enemy'].equip_armor(equipment.get_armor(request.form.get('armor')))
#
#         return redirect(url_for('arena_blueprint.start_fight'))
#
#     result = {
#         "header": "Выберите противника",
#         "classes": unit_classes.keys(),
#         "weapons": equipment.get_weapons_names(),
#         "armors": equipment.get_armors_names()
#     }
#     return render_template('hero_choosing.html', title='Choose enemy', result=result)
