text = open("data.txt", "r")
file_content = text.read()
print(file_content)
text.close()

name = input("What's your name")
if name:
    writable_file = open("data.txt", "w")
    writable_file.write(name)
    writable_file.close()
    readable_file = open("data.txt", "r")
    print(readable_file.read())
    readable_file.close()
