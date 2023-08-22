waiting_list = ["sen", "ben", "john"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
    list_members = f"{int(index) + 1}. {item.capitalize()}"
    print(list_members)