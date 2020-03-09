from models import Rule

price_rules = []
qty_rules = []

# Define catalogue pricing
catalogue = {
    'ipd': 549.99,
    'mbp': 1399.99,
    'atv': 109.50,
    'vga': 30.00
}

# Define special rules here
def apple_tv_discount(items, catalogue):
    new_items = items.copy()
    new_items['atv'] = (items['atv'] // 3 * 2) + (items['atv'] % 3)
    return new_items

def ipad_discount(items, catalogue):
    new_catalogue = catalogue.copy()
    if items['ipd'] > 4:
        new_catalogue['ipd'] = 499.99
    return new_catalogue

def free_vga(items, catalogue):
    new_items = items.copy()
    mbp_count = items['mbp']
    vga_count = items['vga']
    if vga_count < mbp_count:
        new_items['vga'] = 0
    else:
        new_items['vga'] = vga_count - mbp_count

    return new_items


# Append accordingly whether special rule affects price or quantity
qty_rules.append(apple_tv_discount)
price_rules.append(ipad_discount)
qty_rules.append(free_vga)

# Import pricingRules to checkout system
pricingRules = Rule(catalogue, {'price': price_rules, 'qty': qty_rules})