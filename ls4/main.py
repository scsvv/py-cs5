usr = "admin"
psw = "1234"

typing_user = input("Enter \"admin\": ")
typing_password = input("Enter: \"1234\": ")

print(f"user: {typing_user}, password: {typing_password}")

if usr==typing_user and typing_password:
    print("Login")
else: 
    print("Inccorect password or login")
