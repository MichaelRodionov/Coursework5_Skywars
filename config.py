from os import path


# ----------------------------------------------------------------
# configuration class
class Config:
    equipment_path = path.abspath(path.join('application', 'data', 'equipment.json'))
