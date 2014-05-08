import sublime, sublime_plugin
import subprocess
import os

class EnlisterCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.show_quick_panel()

    def show_quick_panel(self):
        pd = self.window.project_data();
        if 'enlister' not in pd:
            return

        self.commands = pd['enlister']

        panel_data = []
        for cmd in self.commands:
            try:
                panel_data.append(cmd['name'])
            except KeyError as e:
                if str(e) == "'name'":
                    print('enlister commands require "name". Provided (' + str(cmd) + ')')
                    sublime.error_message('enlister commands require "name". Provided (' + str(cmd) + ')')
                else:
                    raise(e)

        if not len(panel_data):
            return

        self.window.show_quick_panel(panel_data, self.on_quick_panel_select)

    def on_quick_panel_select(self, picked):
        if picked < 0:
            return

        shell = False

        if 'shell' in self.commands[picked] and self.commands[picked]['shell'] == True:
            shell = True

        print('Shell: %s' % shell)

        print(self.commands[picked])
        subprocess.Popen(self.commands[picked]['command'], cwd=self.commands[picked]['working_dir'], shell=shell)
