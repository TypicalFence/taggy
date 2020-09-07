import os
from gi.repository import Gtk


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()


def on_activate(app):
    path = os.path.dirname(os.path.realpath(__file__))
    builder = Gtk.Builder()
    builder.add_from_file(path + "/data/main_window.glade")
    builder.connect_signals(Handler())

    window = builder.get_object("main_window")
    window.set_application(app)
    window.show_all()


app = Gtk.Application(application_id="moe.zaun.Taggy")
app.connect("activate", on_activate)
