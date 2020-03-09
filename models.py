class Item:
    def __init__(self, sku):
        self.sku = sku


class Rule:
    def __init__(self, catalogue, rules):
        self.catalogue = catalogue
        self.rules = rules


class Checkout:
    def __init__(self, rule):
        self.total = 0
        self.items = {}
        self.catalogue = rule.catalogue
        self.rules = rule.rules

    def scan(self, item):
        try:
            self.items[item.sku] += 1
        except KeyError:
            self.items[item.sku] = 1

    def apply_rules(self):
        for rule in self.rules['price']:
            try:
                self.catalogue = rule(self.items, self.catalogue)
            except KeyError:
                pass

        for rule in self.rules['qty']:
            try:
                self.items = rule(self.items, self.catalogue)
            except KeyError:
                pass

    def calculate_total(self):
        for item in self.items:
            self.total += self.catalogue[item] * self.items[item]

    def get_total(self):
        print('SKUs scanned')
        for item in self.items:
            print(f"{item}: {self.items[item]}x")

        print('-' * 30)
        self.apply_rules()
        self.calculate_total()
        print(f'Total: ${self.total}')
        print('=' * 30)
