import os

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

_queries = {}

_queries['tiempo_de_uso'] = open(os.path.join(SCRIPT_PATH, 'sql', 'tiempo_de_uso.sql')).read()
_queries['uso_sugar_gnome'] = open(os.path.join(SCRIPT_PATH, 'sql', 'uso_sugar_gnome.sql')).read()
_queries['ranking_actividades'] = open(os.path.join(SCRIPT_PATH, 'sql', 'ranking_actividades.sql')).read()
_queries['ranking_aplicaciones'] = open(os.path.join(SCRIPT_PATH, 'sql', 'ranking_aplicaciones.sql')).read()


def get_queries():
    return _queries
