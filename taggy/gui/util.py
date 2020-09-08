import os

_path = os.path.dirname(os.path.realpath(__file__))


def get_glade(filename):
    return _path + "/data/" + filename
