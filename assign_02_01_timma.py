#This program is for use to verify users signing into the system
#it lets users give their password and security questions

def username(name, password, security, year):
    #customer gives their name
    print(f"What is your name? {name}")

    #enter the required password
    print(f"Enter your password {password}")

    #if forgotten password, the client can activate the security question
    print(f"What city were you born in? {security}")

    #the client can also use the year of birth as security question
    print(f"When were you born? {year}")

username("Michele Timma", "Timma@123", "Texas", 1999)



