accounts = {
    "checking": 1958.00,
    "saving": 3695.50
}


def add_balnce(amount: float, name: str = "checking"):
    accounts[name] += amount
    return accounts[name]


add_balnce(500.00)
print(accounts["checking"])
