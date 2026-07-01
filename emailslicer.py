email = input("enter your email : ")
username = email[:email.index("@")]
domain = email[email.index("@"):]
print("your username is",username,"your domain is",domain)