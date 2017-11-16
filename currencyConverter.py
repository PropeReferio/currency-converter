import rumps, json, requests
url = "https://api.fixer.io/latest?base=CAD"


data = requests.get(url=url).json()
all_currencies = list(data['rates'])
rumps.debug_mode(True)


class currencyConverter(rumps.App):
    def __init__(self):
        self.currencies = all_currencies
        self.selected_currency = 'USD'
        self.selected_rate = data['rates'][self.selected_currency]

        self.sub_menu = []
        self.currency_menu()

        super(currencyConverter, self).__init__("Currency Converter", title =
        "CAD:" + self.selected_currency + ' %.3f' % self.selected_rate)

        self.menu = [
        'About',
        'Preferences',
        None,
        ('Pick a Currency', self.sub_menu),
        None
        ]

    def currency_menu(self):
        # builds the menu
        for currency in self.currencies:
            item = rumps.MenuItem(currency, callback = self.change_currency)
            item.state = 0
            self.sub_menu.append(item)


    def change_currency(self, sender):
        # changes to other currency if user changes it from the menu
        self.selected_currency = sender.title
        self.selected_rate = data['rates'][self.selected_currency]

        super(currencyConverter, self).__init__("Currency Converter", title =
        "CAD:" + self.selected_currency + ' %.3f' % self.selected_rate)

    @rumps.clicked('About')
    def about(self, sender):
        rumps.alert("This is a currency conversion app created by Ahmed El Gohary. \n It currently defaults to base CAD, I will later add an option that makes it possible to pick any desired base currency.")

    @rumps.clicked('Preferences')
    def prefs(self, _):
        rumps.alert("preferences to be added later!")

if __name__ == "__main__":
    currencyConverter().run()

# add red for decrease, green for increase
# option for quantity
