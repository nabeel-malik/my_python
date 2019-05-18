def fishstore(fish, price):
    info_str = "Fish Type: " + fish + " costs $" + price
    return info_str

fishname = input("enter fish name: ")
fishprice = input("enter the fish price (no symbols): ")

print(fishstore(fishname, fishprice))