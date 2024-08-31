#this program will collect data from a patient visiting the healthcare center

def patient_register(name, residence, sex, age):
    #register the patient's name
    print(f"What is your name? {name}")

    #get the patient's residence
    print(f"where do you live? {residence}")

    #Get patient's gender
    print(f"are you male or female? {sex}")

    #get patient's age
    print(f"How old are you? {age}")

#Recall the function
patient_register("Michele Timma", "Texas", "Female", "32")


