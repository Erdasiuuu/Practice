from welcome_window import WelcomeWindow
from main_window import MainWindow

class WindowManager:
    def __init__(self, root):
        self.root = root
        self.windows = {}
        self.current_window = None
        self.image = [None]

    def get_window(self, word, switch_callback):
        if word == "welcome":
            if "welcome" not in self.windows:
                self.windows["welcome"] = WelcomeWindow(
                                                    self.root,
                                                    self.image,
                                                    switch_callback)
        elif word == "main":
            if "main" not in self.windows:
                self.windows["main"] = MainWindow(
                                            self.root,
                                            self.image,
                                            switch_callback)
        window = self.windows.get(word, None)
        return window

    def hide_all(self):
        for window in self.windows.values():
            window.hide()
