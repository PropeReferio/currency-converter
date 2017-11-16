import rumps, json, requests
url = "https://api.fixer.io/latest?base=CAD"


data = requests.get(url=url).json()
all_currencies = list(data['rates'])
rumps.debug_mode(True)


class currencyConverter(rumps.App):
    def __init__(self):
        self.currencies = all_currencies
        self.sub_menu = []
        self.currency_menu()
        self.selected_currency = 'USD'
        self.selected_rate = data['rates'][self.selected_currency]
        super(currencyConverter, self).__init__("Currency Converter", title = "CAD:" + self.selected_currency + ' %.3f' % self.selected_rate)

        self.menu = [
        'About',
        'Preferences',
        None,
        ('Pick a Currency', self.sub_menu),
        None
        ]

    def current_currency(self):
        print('hi')

    def currency_menu(self):
        smenu = []
        for currency in self.currencies:
            item = (rumps.MenuItem(currency, callback=self.current_currency))
            smenu.append(item)
        self.sub_menu = smenu


    #def current_rate(self):

    @rumps.clicked("About")
    def about(self, sender):
        rumps.alert("This is a currency conversion app created by Ahmed El Gohary. \n It currently defaults to base CAD, I will later add an option that makes it possible to pick any desired base currency.")

    @rumps.clicked("Preferences")
    def prefs(self, _):
        rumps.alert("jk! no preferences available!")


if __name__ == "__main__":
    currencyConverter().run()

# add red for decrease, green for increase
# option for quantity
