#username validator
#username should be of 12 characters
#username must not contain spaces
#username must not contain digits

username = input("enter username : ")

if len(username) > 12:
    print("userame can not have 12 characters")
elif not username.find(" ")==-1:
    print("username can not have spaces")
elif not username.isalpha():
    print("username can not have digits")
else:
    print("welcome",username)