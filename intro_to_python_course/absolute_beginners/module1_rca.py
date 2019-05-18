user_name = input("Please enter your name: ")

greeting = "Hello"

print(greeting, user_name + "!")

food_cat_str = input("Please enter the food categories you have eaten in the last 24 hours: ")

checklist = ["dairy", "nuts", "seafood", "chocolate"]

for item in checklist:
    print ("It is", item in food_cat_str.lower(), "that", food_cat_str, "contains", item)
