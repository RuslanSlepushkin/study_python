phone_num = input("Write your phone number correct: ")
if phone_num.isdigit() and len(phone_num) == 10:
    print("This is the correct phone number.")
else:
    print("This is a wrong phone number.")