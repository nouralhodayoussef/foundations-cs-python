ID = input("Enter your ID: ")
name = input("Enter your name: ")
dob = input("Enter your date of birth (MM-DD-YYYY): ")
address = input("Enter your address: ")

ID = '0' + ID
name = name.upper()
dob = dob.replace("-", "/")
address = address.strip().lower()
print("Your profile - ID: ",ID," name: ",name, " DOB: ",dob, " Address: ",address)

