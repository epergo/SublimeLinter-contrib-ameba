import os

class MaybeDisableSublimeLinterAmeba(sublime_plugin.EventListener):
    def on_loaded(self, view):
        if os.path.basename(window.active_view().file_name()).startswith("syntax_test_"):
            view.settings().set("SublimeLinter.linters.contrib-ameba.disable", True)

