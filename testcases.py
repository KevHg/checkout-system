from models import Item, Checkout
from rules import pricingRules

# Test case 1
cc = Checkout(pricingRules)
cc.scan(Item("atv"))
cc.scan(Item("atv"))
cc.scan(Item("atv"))
cc.scan(Item("vga"))
cc.get_total()

# Test case 2
cc = Checkout(pricingRules)
cc.scan(Item("atv"))
cc.scan(Item("ipd"))
cc.scan(Item("ipd"))
cc.scan(Item("atv"))
cc.scan(Item("ipd"))
cc.scan(Item("ipd"))
cc.scan(Item("ipd"))
cc.get_total()

# Test case 3
cc = Checkout(pricingRules)
cc.scan(Item("mbp"))
cc.scan(Item("vga"))
cc.scan(Item("ipd"))
cc.get_total()