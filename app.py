from kivy.app import App

class mainApp(App):
    def build(self):
        self.icon = ""


if __name__ == "__main__":
    app = mainApp()
    app.run()