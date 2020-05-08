import rumps, json, requests
url = 'https://api.exchangeratesapi.io/latest?base=USD'
#Previous APIs did not allow for free selection of base currency, so you could only convert from euros.
#That's why I chose a new API.
rumps.debug_mode(True)


class currencyConverter(rumps.App):
    def __init__(self):
        self.url = 'https://api.exchangeratesapi.io/latest?base=USD'
        self.data = requests.get(url=self.url).json()

        self.currencies = list(self.data['rates'])
        self.base_currency = self.data['base']
        self.selected_currency = 'CAD'
        self.selected_rate = self.data['rates'][self.selected_currency]

        self.sub_menu = []
        self.base_sub_menu = []
        self.currency_menu()
        self.base_currency_menu()

        super(currencyConverter, self).__init__("Currency Converter", title =
        self.data['base'] + ':' + self.selected_currency + ' %.3f' % self.selected_rate)
        #Instead of "CAD:", I can use data['base'] so that it correctly updates to the selected base currency.


        self.menu = [
        'About',
        'Preferences',
        None,
        ('Convert To:', self.sub_menu),
        ('Convert From:', self.base_sub_menu),
        None
        ]

    def currency_menu(self):
        # builds the menu of target currencies, for the "Convert To: " menu
        for currency in self.currencies:
            item = rumps.MenuItem(currency, callback = self.change_currency)
            item.state = 0
            self.sub_menu.append(item)

    def base_currency_menu(self):
        # builds the menu of base currencies, for the "Convert From: " menu
        for currency in self.currencies:
            item = rumps.MenuItem(currency, callback = self.change_base_currency)
            item.state = 0
            self.base_sub_menu.append(item)


    def change_currency(self, sender):
        # changes to other currency if user changes it from the "Convert To: " menu
        self.selected_currency = sender.title
        self.selected_rate = self.data['rates'][self.selected_currency]

        super(currencyConverter, self).__init__("Currency Converter", title =
        self.data['base'] + ':' + self.selected_currency + ' %.3f' % self.selected_rate)

    def change_base_currency(self, sender):
        # changes to other currency if user changes it from the "Convert From: " menu
        # format the URL, make a new API call, reassign updated JSON data to 'data'
        self.base_currency = sender.title
        self.url = 'https://api.exchangeratesapi.io/latest?base=' + self.base_currency
        self.data = requests.get(url=self.url).json()
        self.currencies = list(self.data['rates'])
        self.selected_rate = self.data['rates'][self.selected_currency]
        
        super(currencyConverter, self).__init__("Currency Converter", title =
        self.data['base'] + ':' + self.selected_currency + ' %.3f' % self.selected_rate)
        

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
