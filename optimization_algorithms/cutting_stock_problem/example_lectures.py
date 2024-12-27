import random
from itertools import combinations_with_replacement

from bin_packing_approach import solve_bin_packing_from_orders

class Order:
    def __init__(self, id, w, order_level):
        self.id = id
        self.width = w
        self.order_level = order_level
        self.pending_production = order_level

class Pattern:
    def __init__(self, ord_list, sheet_width):
        self.order_list = ord_list
        tot_width = 0
        for order_tuple in ord_list:
            order_type = order_tuple[0]
            items = order_tuple[1]
            tot_width += order_type.width * items
        self.waste = sheet_width - tot_width
        self.current_waste = self.waste
        self.times_used = 0

def is_dominating_configuration(conf, min_width, sheet_width):
    tot_width = sum(ord.width for ord in conf)
    waste = sheet_width - tot_width
    if waste < min_width:
        return True
    return False


def is_feasible_configuration(conf, sheet_width):
    tot_width = sum(ord.width for ord in conf)
    if tot_width <= sheet_width:
        return True
    return False


def build_patterns_from_configurations(dominating_configurations, sheet_width):
    patterns = []
    for conf in dominating_configurations:
        order_list = []
        unique_orders_in_conf = set(conf)
        for ord in unique_orders_in_conf:
            number_of_ord = conf.count(ord)
            order_list.append((ord, number_of_ord))
        p = Pattern(order_list, sheet_width)
        patterns.append(p)
    return patterns

def term_condition(orders):
    for o in orders:
        if o.pending_production > 0:
            return False
    return True


def find_best_pattern(dominating_patterns):
    min_waste = 10 ** 10
    min_waste_pattern = None
    for p in dominating_patterns:
        if p.current_waste < min_waste:
            min_waste = p.current_waste
            min_waste_pattern = p
    return min_waste_pattern


def update_information(p):
    p.times_used += 1
    for tup in p.order_list:
        order = tup[0]
        quant = tup[1]
        order.pending_production -= quant


def calculate_current_waste_for_patterns(dominating_patterns):
    for p in dominating_patterns:
        extra_waste = 0
        for tup in p.order_list:
            ord = tup[0]
            quant_in_pattern = tup[1]
            if quant_in_pattern > ord.pending_production:
                pend_prod = max(ord.pending_production, 0)
                waste_times = quant_in_pattern - pend_prod
                extra_waste += waste_times * ord.width
        p.current_waste = p.waste + extra_waste


# def build_example_problem():
#     ord1 = Order(0, 9, 145)
#     ord2 = Order(1, 8, 120)
#     ord3 = Order(2, 7, 320)
#     ord4 = Order(3, 6, 480)
#     ord_list = [ord1, ord2, ord3, ord4]
#     sheet_width = 20
#     return ord_list, sheet_width

# 420 120
def build_example_problem():
    ord1 = Order(0, 12, 4)
    ord2 = Order(1, 9, 5)
    ord3 = Order(2, 6, 8)
    ord4 = Order(3, 4, 7)
    ord_list = [ord1, ord2, ord3, ord4]
    sheet_width = 20
    return ord_list, sheet_width

orders, sheet_width = build_example_problem()
widths = [o.width for o in orders]
min_width = min(widths)
max_num_items_in_pattern = int(sheet_width/min_width)
dominating_configurations = []
for i in range(0,max_num_items_in_pattern + 1):
    for conf in combinations_with_replacement(orders, i):
        if is_feasible_configuration(conf, sheet_width) and is_dominating_configuration(conf, min_width, sheet_width):
            dominating_configurations.append(conf)

dominating_patterns = build_patterns_from_configurations(dominating_configurations, sheet_width)
patterns_used = []
while not term_condition(orders):
    calculate_current_waste_for_patterns(dominating_patterns)
    p = find_best_pattern(dominating_patterns)
    update_information(p)
    patterns_used.append(p)
    print(p.current_waste)
    print(orders[0].pending_production, orders[1].pending_production, orders[2].pending_production, orders[3].pending_production)

print('Patterns', len(patterns_used))

solve_bin_packing_from_orders(orders, sheet_width)

