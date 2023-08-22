import json
import math
import time

with open("cricket_quiz.json", "r") as file:
    content = file.read()

data = json.loads(content)

score = 0

for question in data:
    print(question["question_text"])
    time.sleep(2)
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1}: {alternative}")
        time.sleep(1)
    user_choice = int(input("Enter the number of your answer here: "))
    question["user_answer"] = user_choice
    time.sleep(1.5)


for index, question in enumerate(data):
    if question["user_answer"] == question["question_answer"]:
        score = score + 1

print(f"Your score is {score}/{len(data)}")
time.sleep(1)
print(f"That is {math.ceil(float(score / len(data)) * 100)}%!")
print("CONGRATULATIONS!!!")
time.sleep(1)
print()
print("Here is the answer key:")
time.sleep(1)
print()

for index, question in enumerate(data):
    if question["user_answer"] == question["question_answer"]:
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{result} for {index + 1}: Your Answer: {question['user_answer']}, " \
              f"Right Answer: {question['question_answer']}"
    print(message)
    time.sleep(1.5)
    print()
