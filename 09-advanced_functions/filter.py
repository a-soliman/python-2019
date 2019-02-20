friends = ["Jose", "Rolf", "Randy", "Anna", "Mary"]

starts_with_r = (f for f in friends if f.startswith("R"))

friends_lower = map(lambda x: x.lower(), friends)
friends_lower2 = (f.lower() for f in friends)
