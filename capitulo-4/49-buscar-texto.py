email = "usuario@academiafibonacci.com.gt"

print(email.find("@"))
print(email.find("xyz"))

print(email.index("@"))
#print(email.index("xyz"))

arroba = email.find("@")
dominio = email[arroba+1: ]
print(dominio)