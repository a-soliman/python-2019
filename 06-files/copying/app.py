
def get_friends():
    friends = input("provide three name: ")
    return [friend.strip() for friend in friends.split(",")]


def is_near_by(friends, people):
    peopleMap = create_map(people)
    near_by = []

    for friend in friends:
        if friend in peopleMap:
            print(f"{friend} is near by!")
            near_by.append(friend)

    write_file(near_by)


def create_map(filename):
    readable_file = open(filename, "r")
    content = readable_file.readlines()
    striped_content = {person.strip("\r\n"): person.strip(
        "\r\n") for person in content}
    readable_file.close()
    return striped_content


def write_file(content):
    file = open("nearby.txt", "w")
    file.writelines([f"{name}\n" for name in content])
    file.close()


is_near_by(get_friends(), "people.txt")
