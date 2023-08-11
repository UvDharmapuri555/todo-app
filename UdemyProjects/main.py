import time
import sys
from UdemyProjects.functions import get_todos, write_todos

new_todos = []

todos = get_todos()

date = time.strftime("%B %d, %Y - %T")
print(f"It is {date}")

for letter in "Hello!!!":
    sys.stdout.write(letter), time.sleep(0.22)
print()

for letter in "This application is used to list todo items to complete throughout the day.":
    sys.stdout.write(letter), time.sleep(0.01)
print()
time.sleep(1)

for letter in "In this application, you may add todos, complete todos, and change an item in your list through the " \
              "edit function, view your list, or exit the application.":
    sys.stdout.write(letter), time.sleep(0.01)
print()
print()
time.sleep(1)

print("User,")
time.sleep(2)
print("Let's begin!!!")
print()
time.sleep(1.5)

while True:
    user_action = input("Type add, to add a todo, view, to check your list, or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            todos = get_todos()

            todos.append(todo.title())

            write_todos(todos)
            print()

            while True:
                user_action = input("Type edit, view, or exit: ")
                user_action = user_action.strip()
                user_action = user_action.lower()

                match user_action:
                    case "edit":
                        user_action2 = input(
                            "Type add, to add a todo, change, to change an item, or complete, "
                            "to delete a todo: ")
                        user_action2 = user_action2.strip()
                        user_action2 = user_action2.lower()
                        match user_action2:
                            case "change":
                                print()
                                print("Here are existing todos: ")
                                new_todos = [items.strip("\n") for items in todos]
                                for index, item in enumerate(new_todos):
                                    number_items = f"{int(index) + 1}. {item}"
                                    print(number_items)

                                print()

                                while True:
                                    try:
                                        number = input("Number of todo item to change: ")
                                        if number == 0:
                                            print()
                                            print("No todo item exists with that number in your list")
                                            print("Please enter a different number.")
                                            print()
                                            continue
                                        number = int(number) - 1
                                        print()

                                        todos = get_todos()

                                        print("Selected todo -", todos[number])

                                        print()
                                        print("Is this the todo you needed to change???")
                                        user_change = input("Type yes or no: ")

                                        match user_change:
                                            case "no":
                                                while True:
                                                    print(
                                                        "User, please check cautiously at todo requested to be "
                                                        "edited.")
                                                    print()
                                                    edit_number = int(
                                                        input(
                                                            "Number of todo item to change: ")) - 1
                                                    print()

                                                    if edit_number == 0:
                                                        print("No todo item exists with that number in your list")
                                                        print("Please enter a different number.")
                                                        print()
                                                        continue

                                                    print("Todo finished - ", todos[edit_number])
                                                    print("Is this the todo you finished???")
                                                    user_editing = input("Type yes or no: ")
                                                    print()

                                                    match user_editing:
                                                        case "yes":
                                                            print("List updated!!!")

                                                            todos = get_todos()

                                                            todos.pop(int(edit_number)) + "\n"

                                                            write_todos(todos)

                                                            time.sleep(2)
                                                            new_todos = [items.strip("\n") for items in todos]
                                                            for index, item in enumerate(new_todos):
                                                                number_items = f"{int(index) + 1}. {item}"
                                                                print(number_items)
                                                            print()
                                                            break
                                                    break
                                            case "yes":
                                                print("List updated!!!")

                                                todos = get_todos()

                                                todos.pop(int(number)) + "\n"

                                                write_todos(todos)

                                                time.sleep(2)
                                                new_todos = [items.strip("\n") for items in todos]
                                                for index, item in enumerate(new_todos):
                                                    number_items = f"{int(index) + 1}. {item}"
                                                    print(number_items)
                                                print()
                                                break
                                            case x:
                                                print("Please enter one of the options.")
                                                print()
                                                continue

                                        new_todo = input("Enter new todo to replace this one: ")
                                        todos[number] = new_todo.title() + "\n"
                                        todos.append(new_todo.title())
                                        del (todos[-1])

                                        write_todos(todos)

                                        print()

                                        print("Todo successfully changed!")
                                        time.sleep(2)
                                        print()
                                        print("Here is new list:")
                                        time.sleep(2)
                                        new_todos = [items.strip("\n") for items in todos]
                                        for index, item in enumerate(new_todos):
                                            number_items = f"{int(index) + 1}. {item}"
                                            print(number_items)
                                        print()
                                        break
                                    except ValueError:
                                        print()
                                        print("Please enter a number.")
                                        print()
                                        continue
                                    except IndexError:
                                        print("No todo item exists with that number in your list.")
                                        print("Please enter a different number.")
                                        print()
                            case "add":
                                todo = input("Enter a todo: ") + "\n"

                                todos = get_todos()

                                todos.append(todo.title())

                                write_todos(todos)

                                print()

                            case "complete":
                                print()

                                new_todos = [items.strip("\n") for items in todos]
                                for index, item in enumerate(new_todos):
                                    number_items = f"{int(index) + 1}. {item}"
                                    print(number_items)

                                print()

                                while True:
                                    try:
                                        print("Which todo has been completed???")
                                        completed_number = int(input("Enter number of todo which has been completed: "))

                                        if completed_number == 0:
                                            print()
                                            print("No todo item exists with that number in your list")
                                            print("Please enter a different number.")
                                            print()
                                            continue

                                        completed_number = completed_number - 1
                                        print()
                                        print("Todo finished - ", todos[completed_number])
                                        print("Is this the todo you finished???")
                                        user_finish = input("Type yes or no: ")
                                        print()

                                        match user_finish:
                                            case "no":
                                                while True:
                                                    print(
                                                        "User, please check cautiously at todo requested to be "
                                                        "complete.")
                                                    print()
                                                    print("Which todo has been completed???")
                                                    finish_number = int(
                                                        input(
                                                            "Enter number of todo which has been completed: ")) - 1
                                                    print()

                                                    if finish_number == 0:
                                                        print("No todo item exists with that number in your list")
                                                        print()
                                                        continue

                                                    print("Todo finished - ", todos[finish_number])
                                                    print("Is this the todo you finished???")
                                                    user_finish = input("Type yes or no: ")
                                                    print()

                                                    match user_finish:
                                                        case "yes":
                                                            print("List updated!!!")

                                                            todos = get_todos()

                                                            todos.pop(int(finish_number)) + "\n"

                                                            write_todos(todos)

                                                            time.sleep(2)
                                                            new_todos = [items.strip("\n") for items in todos]
                                                            for index, item in enumerate(new_todos):
                                                                number_items = f"{int(index) + 1}. {item}"
                                                                print(number_items)
                                                            print()
                                                            break
                                                    break
                                            case "yes":
                                                print("List updated!!!")

                                                todos = get_todos()

                                                todos.pop(int(completed_number)) + "\n"

                                                write_todos(todos)

                                                time.sleep(2)
                                                new_todos = [items.strip("\n") for items in todos]
                                                for index, item in enumerate(new_todos):
                                                    number_items = f"{int(index) + 1}. {item}"
                                                    print(number_items)
                                                print()
                                                break
                                            case x:
                                                print("Please enter one of the options.")
                                                print()
                                                continue

                                    except ValueError:
                                        print()
                                        print("Please enter a number only.")
                                        print()
                                        continue
                                    except IndexError:
                                        print("No todo item exists with that number in your list.")
                                        print("Please enter a different number.")
                                        print()
                            case x:
                                print("Please enter one of the options.")
                    case "view":
                        new_todos = [items.strip("\n") for items in todos]
                        for index, item in enumerate(new_todos):
                            number_items = f"{int(index) + 1}. {item}"
                            print(number_items)
                        print()
                    case "exit":
                        print()
                        for letter in "Bye!!!":
                            sys.stdout.write(letter), time.sleep(0.22)
                        exit()
        case "view":
            new_todos = [items.strip("\n") for items in todos]
            for index, item in enumerate(new_todos):
                number_items = f"{int(index) + 1}. {item}"
                print(number_items)
            print()

            while True:
                user_action = input("Type edit, view, or exit: ")
                user_action = user_action.strip()
                user_action = user_action.lower()

                match user_action:
                    case "edit":
                        user_action2 = input(
                            "Type add, to add a todo, change, to change an item, or complete, "
                            "to delete a todo: ")
                        user_action2 = user_action2.strip()
                        user_action2 = user_action2.lower()
                        match user_action2:
                            case "change":
                                print()
                                print("Here are existing todos: ")
                                new_todos = [items.strip("\n") for items in todos]
                                for index, item in enumerate(new_todos):
                                    number_items = f"{int(index) + 1}. {item}"
                                    print(number_items)

                                print()

                                while True:
                                    try:
                                        number = input("Number of todo item to change: ")
                                        number = int(number) - 1
                                        print()

                                        if number == -1:
                                            print("No todo item exists with that number in your list")
                                            print("Please enter a different number.")
                                            print()
                                            continue

                                        todos = get_todos()

                                        print("Selected todo -", todos[number])

                                        new_todo = input("Enter new todo to replace this one: ")
                                        todos[number] = new_todo.title() + "\n"
                                        todos.append(new_todo.title())
                                        del (todos[-1])

                                        write_todos(todos)

                                        print()

                                        print("Todo successfully changed!")
                                        time.sleep(2)
                                        print()
                                        print("Here is new list:")
                                        time.sleep(2)
                                        new_todos = [items.strip("\n") for items in todos]
                                        for index, item in enumerate(new_todos):
                                            number_items = f"{int(index) + 1}. {item}"
                                            print(number_items)
                                        print()
                                        break
                                    except ValueError:
                                        print()
                                        print("Please enter a number.")
                                        print()
                                        continue
                                    except IndexError:
                                        print("No todo item exists with that number in your list.")
                                        print("Please enter a different number.")
                                        print()
                            case "add":
                                todo = input("Enter a todo: ") + "\n"

                                todos = get_todos()

                                todos.append(todo.title())

                                write_todos("todos.txt", todos)

                                print()

                            case "complete":
                                print()

                                new_todos = [items.strip("\n") for items in todos]
                                for index, item in enumerate(new_todos):
                                    number_items = f"{int(index) + 1}. {item}"
                                    print(number_items)

                                print()

                                while True:
                                    try:
                                        print("Which todo has been completed???")
                                        completed_number = int(input("Enter number of todo which has been completed: "))

                                        if completed_number == 0:
                                            print("No todo item exists with that number in your list")
                                            print("Please enter a different number.")
                                            print()
                                            continue

                                        completed_number = completed_number - 1
                                        print()
                                        print("Todo finished - ", todos[completed_number])
                                        print("Is this the todo you finished???")
                                        user_finish = input("Type yes or no: ")
                                        print()

                                        match user_finish:
                                            case "no":
                                                while True:
                                                    print(
                                                        "User, please check cautiously at todo requested to be "
                                                        "complete.")
                                                    print()
                                                    print("Which todo has been completed???")
                                                    finish_number = int(
                                                        input(
                                                            "Enter number of todo which has been completed: ")) - 1
                                                    print()

                                                    if finish_number == 0:
                                                        print("No todo item exists with that number in your list")
                                                        print()
                                                        continue

                                                    print("Todo finished - ", todos[finish_number])
                                                    print("Is this the todo you finished???")
                                                    user_finish = input("Type yes or no: ")
                                                    print()

                                                    match user_finish:
                                                        case "yes":
                                                            print("List updated!!!")

                                                            todos = get_todos()

                                                            todos.pop(int(finish_number)) + "\n"

                                                            write_todos("todos.txt", todos)

                                                            time.sleep(2)
                                                            new_todos = [items.strip("\n") for items in todos]
                                                            for index, item in enumerate(new_todos):
                                                                number_items = f"{int(index) + 1}. {item}"
                                                                print(number_items)
                                                            print()
                                                            break
                                                    break
                                            case "yes":
                                                print("List updated!!!")

                                                todos = get_todos()

                                                todos.pop(int(completed_number)) + "\n"

                                                write_todos("todos.txt", todos)

                                                time.sleep(2)
                                                new_todos = [items.strip("\n") for items in todos]
                                                for index, item in enumerate(new_todos):
                                                    number_items = f"{int(index) + 1}. {item}"
                                                    print(number_items)
                                                print()
                                                break
                                            case x:
                                                print("Please enter one of the options.")
                                                print()
                                                continue

                                    except ValueError:
                                        print()
                                        print("Please enter a number only.")
                                        print()
                                        continue
                                    except IndexError:
                                        print("No todo item exists with that number in your list.")
                                        print("Please enter a different number.")
                                        print()
                            case x:
                                print("Please enter one of the options.")
                    case "view":
                        new_todos = [items.strip("\n") for items in todos]
                        for index, item in enumerate(new_todos):
                            number_items = f"{int(index) + 1}. {item}"
                            print(number_items)
                        print()
                    case "exit":
                        print()
                        for letter in "Bye!!!":
                            sys.stdout.write(letter), time.sleep(0.22)
                        exit()

        case "exit":
            print()
            for letter in "Bye!!!":
                sys.stdout.write(letter), time.sleep(0.22)
            exit()
        case x:
            print()
            print("Please enter one of the options.")
            print()