import rumps

class currencyConverter(rumps.App):
    def __init__(self):
        super(currencyConverter, self).__init__("Currency Converter")
        self.menu = ["Preferences", "Pick a currency"]

    @rumps.clicked("Preferences")
    def prefs(self, _):
        rumps.alert("jk! no preferences available!")

    @rumps.clicked("Silly button")
    def onoff(self, sender):
        sender.state = not sender.state

    @rumps.clicked("Say hi")
    def sayhi(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

if __name__ == "__main__":
    currencyConverter().run()
