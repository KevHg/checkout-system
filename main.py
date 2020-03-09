from models import Item, Checkout
from rules import pricingRules, catalogue

cc = Checkout(pricingRules)

user = None
while True:
    user = input("Enter SKU (or type 'end' to quit): ")
    if user in catalogue:
        cc.scan(Item(user))
    elif user == "end":
        break
    else:
        print("[Error] SKU not found")

cc.get_total()
