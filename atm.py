class atm:
    def __init__(self,pin):
        self.pin = pin

    def balance(self):
        print("Your balance is 4389276")

    def withdrawl(self,amount):
        new_amount = 4389276 - amount
        print("Amount Withdrawn: "+str(amount) +". Remaining Balance: "+ str(new_amount))

def main():
    pin_number  = input("Enter your PIN Number: ")
    new_user =  atm(pin_number)

    print("Choose your activity ")
    print("1. Check Balance")
    print("2. Withdraw")
    activity = int(input("Enter Activity Number: "))

    if (activity == 1):
        new_user.balance()
    elif (activity == 2):
        amount = int(input("Enter the Amount to Withdraw: "))
        new_user.withdrawl(amount)
    else:
        print("Enter a Valide Number from the List")

if __name__ == "__main__":
    main()

