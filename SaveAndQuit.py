import sublime, sublime_plugin

class SaveAndQuitCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("save_all")
        self.window.run_command("exit")