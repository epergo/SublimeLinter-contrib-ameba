import os

import sublime_plugin


class MaybeDisableSublimeLinterAmeba(sublime_plugin.EventListener):
    def on_load(self, view):
        filename = view.file_name()
        if filename and os.path.basename(filename).startswith("syntax_test_"):
            view.settings().set("SublimeLinter.linters.contrib-ameba.disable", True)
