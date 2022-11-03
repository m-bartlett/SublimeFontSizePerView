import sublime
import sublime_plugin

class AdjustFontSizePerViewCommand(sublime_plugin.TextCommand):

    @staticmethod
    def get_font_size_global():
        return sublime.load_settings("Preferences.sublime-settings").get('font_size')


    def get_font_size(self):
        return self.view.settings().get('font_size')


    def set_font_size(self, font_size):
        self.view.run_command('set_setting', {"setting": "font_size", "value": font_size});


    def add_font_size(self, delta):
        self.set_font_size(self.get_font_size() + delta)


    def reset_font_size(self):
        self.set_font_size(self.get_font_size_global())


    def run(self, edit, **kwargs):
        font_size_delta = kwargs.get('delta')
        if font_size_delta:
            self.add_font_size(font_size_delta)
            return

        font_size = kwargs.get('font_size')
        if font_size_delta:
            self.set_font_size(font_size_delta)
            return

        self.reset_font_size()
