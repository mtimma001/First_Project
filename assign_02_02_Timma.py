#This program will help to get reviews from customers on our product

#here i define the function
def give_reviews (name, age, opinion, recommend, rating):
    #the client gives their name
    print(f"What is your name? {name}")

    #the client enters their age
    print(f"How old are you now? {age}")

    #client gives opinion on the product
    print(f"Do you like our product? {opinion}")

    #asks client the likelihood to recommend product
    print(f"Will you refer friends to our product? {recommend}")

    #client gives a rating for the product
    print(f"Kindly rate our services. {rating}")

give_reviews("Timma", 32, "yes", "yes", 5)
