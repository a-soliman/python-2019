# Sets
friends = {"rolf", "anna", "charlie"}
guests = {"jose", "rolf", "ruth", "charlie", "michael"}

present_friends = friends & guests
print(present_friends)


names = [name.capitalize() for name in friends]
last_seen = [10, 15, 8]

friends_last_seen = {names[i]: last_seen[i] for i in range(len(names))}
print(friends_last_seen)
