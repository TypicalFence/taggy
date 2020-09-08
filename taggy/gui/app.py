from gi.repository import Gtk
from . import util
from .tag_editor import TagEditor


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()


def on_activate(app):
    builder = Gtk.Builder()
    builder.add_from_file(util.get_glade("main_window.glade"))
    builder.connect_signals(Handler())

    window = builder.get_object("main_window")
    window.set_application(app)
    window.show_all()

    paned = builder.get_object("paned")
    paned.add(TagEditor())


app = Gtk.Application(application_id="moe.zaun.Taggy")
app.connect("activate", on_activate)
