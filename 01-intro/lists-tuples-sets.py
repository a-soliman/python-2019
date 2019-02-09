greetings_list = ["hello", "hi", "nice to meet you"]
greetings_tuple = ("hello", "hi", "nice to meet you")
greeting_set = {"hello", "hi", "nice to meet you"}

short_tuple = ("hello",)

print(greetings_list)
print(greetings_tuple)
print(greeting_set)
print(short_tuple)


print(greetings_list[1])
greetings_list.append("the end!")
greetings_tuple = greetings_tuple + ("the end!",)
print(greetings_tuple)
