#This program will be used to display an invoice
#i begin by defining the function
def display_invoice(username, amount, due_date):
    #first greet the client
    print(f"Hello {username}")

    #give the exact amount and the due date
    print(f"Your bill of ${amount} is due; {due_date}")
display_invoice("Michele Timma", 50, "31/08")
