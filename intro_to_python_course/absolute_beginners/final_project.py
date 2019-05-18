def adding_report(report_type = "T"):
    items = ""
    total = 0
    while True:
        user_input = input("Enter an integer or \"Q\": ")
        if user_input.isdigit():
            total += int(user_input)
            if report_type == "A":
                items += user_input + '\n'
            else:
                pass
        elif user_input == "Q" or user_input.startswith("Q"):
            if report_type == "A":
                print("Items\n" + items)
                print("Total\n" + str(total))
            else:
                print("Total\n" + str(total))
            break
        else:
            print("Input is invalid")

entry = ""
while entry == "":
    entry = input("Choose report type (\"A\" or \"T\"): ")
    if entry != "":
        if entry == "A":
            adding_report("A")
        elif entry == "T":
            adding_report()
        else:
            print("Invalid entry")
            entry =""



