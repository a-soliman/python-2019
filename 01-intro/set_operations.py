set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

# Intersection
print(set_one.intersection(set_two))

# Union
print(set_one.union(set_two))

# Difference
print(set_one.difference(set_two))
print(set_two.difference(set_one))


nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
friend = input("What's your firend's name? ")

# Add the name to the empty set
user_friends.add(friend)

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.

print(user_friends)
# print(nearby_people.intersection(user_friends))
