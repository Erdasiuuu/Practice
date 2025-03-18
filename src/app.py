from .window_manager import WindowManager

class App:
    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)

        self.window_manager = WindowManager(self.root)

        self.switch_window("welcome")

    def switch_window(self, word):
        if self.window_manager.current_window is not None:
            self.window_manager.get_window(
                                        self.window_manager.current_window,
                                        self.switch_window
            ).hide()

        self.window_manager.current_window = word
        window = self.window_manager.get_window(
                                            word,
                                            self.switch_window)
        window.show()
