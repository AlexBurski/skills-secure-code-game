'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal, getcontext
getcontext().prec = 28

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = Decimal(0)
    count = 0
    for item in order.items:
        count+= 1
        if item.type == 'payment' :
            net += Decimal(str(item.amount))
        elif item.type == 'product' and net >= Decimal(0.00):
            net -= Decimal(str(item.amount)) * Decimal(item.quantity)
        else:
            return "Invalid item type: %s" % item.type
    if count > 10:
        return "Total amount payable for an order exceeded"
    if net != Decimal(0.00):
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id