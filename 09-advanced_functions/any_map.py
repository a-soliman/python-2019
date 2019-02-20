friends = [
    {
        "name": "Rolf",
        "location": "Washington, D.C."
    },
    {
        "name": "Anna",
        "location": "San Francisco"
    },
    {
        "name": "Charlie",
        "location": "San Francisco"
    },
    {
        "name": "Jose",
        "location": "San Francisco"
    }
]

for i, friend in enumerate(friends):
    print(f"My friend N.{i+1}, {friend['name']} lives in {friend['location']}")
