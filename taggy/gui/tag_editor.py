from gi.repository import Gtk
from . import util


class TagEditor(Gtk.Bin):
    __gtype_name__ = 'TagEditor'

    def __init__(self):
        super().__init__()

        builder = Gtk.Builder()
        builder.add_from_file(util.get_glade("tag_editor.glade"))
        builder.connect_signals(self)
        editor = builder.get_object("tag_editor")

        self.add(editor)
