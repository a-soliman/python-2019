accounts = {
    "checking": 1958.00,
    "savings": 3695.50
}


def add_balance(amount, name):
    accounts[name] += amount
    return accounts[name]


transations = [
    (-180.5, "checking"),
    (-15.5, "savings"),
    (100.5, "checking"),
    (1000.5, "savings"),
    (180.5, "checking"),
    (200, "savings"),
    (300, "checking"),
]

for t in transations:
    add_balance(*t)

print(accounts)
