# Syntax if variable - condition age:

# weather = "sunny"
#
# if weather == "sunny":  # If this condition is true, the code below if statement will execute
#     print("Enjoy the weather")
# elif weather == "rainy":  # Else, if the weather is "rainy" run the code below
#     print("Take an umbrella")
# else:  # If other statements are false, run else block of code
#     print("Thank you for checking the weather")
#
# # Ticket age example
#
# age = 17
#
# if age < 18:  # Check the condition
#     print("You are not eligible to watch this movie, you need to be 18")

# For and While Loops
# Loops help us iterate through our data, such as Lists, Dicts, etc

# shopping_list = ["eggs", "apples", "milk", "bread", "butter"]
# #                    0       1        2         3        4
# # Instead of printing each item on the list ourselves with 'print(shopping_list[x])'
# # First iteration
# for items in shopping_list:
#     print(items)
#
# # Second iteration with if conditions and control flow of program
# shopping_list = ["eggs", "apples", "milk", "bread", "butter"]
# for items in shopping_list:
#     if items == "bread":  # If this condition is true
#         break  # stop the loop when above condition is met
#     print(items)

# Third iteration with dict
student_data = {
    "student_name": "James",  # string
    "course": "DevOps",  # string
    "course_topics": 4,  # int
    "topic_names": ["Business Week", "Python", "Virtualisation with Vagrant", "AWS"]  # list
}
# print(student_data)
# Let's iterate through dict
# for data in student_data.values():
#     if data == "DevOps":  # if condition is True, the loop exits
#         break
#     print(data)

# # First Iteration of while loop
# num = 0
# while num < 10:  # while num value is less than 10
#     print(f"it's working -> {num}")  # print this
#     num += 1  # and add 1 to num

# # Second Iteration of while loop
# num = 0
# while num < 10:
#     print(f"it's working {num}")
#     if num == 5:  # if this condition is true, exit loop
#         break
#     num += 1

# Third Iteration (interacting with users)
# prompt the user to input age and restrict to enter in digits only
# check if the data is in digits display it back to the user
# if not in digits prompt the user with message to enter in digits
# Hint: you can use method called isdigit()

while True:
    age = input("Please input your age:  ")
    if age.isdigit() and int(age) < 150:
        print(f"You are years {age} old.")
        break
    else:
        print("Please only use valid numbers.")
