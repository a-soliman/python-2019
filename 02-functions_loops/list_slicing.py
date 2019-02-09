friends = ["rolf", "jose", "anna", "charlie", "mary"]
print(friends[-3:])


# Comprehension
numbers = list(range(10))
d_numbers = [n*2 for n in numbers]

print(d_numbers)

phrases = [f"I am {age} yo." for age in d_numbers if age > 2]
print(phrases)


names_list = ["John", "Rolf", "Anne"]
lowercase_names = [name.lower() for name in names_list]

print(lowercase_names)


friends = ["rolf", "anna", "charlie"]
guests = ["Jose", "rolf", "ruth", "Charlie", "michael"]

friends_in_party = [
    friend.capitalize() for friend in friends if friend.lower() in [guest.lower() for guest in guests]]

print(friends_in_party)
