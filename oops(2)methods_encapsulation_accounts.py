import datetime
import pytz
# signature is definition of a name and parameters of a function


class Accounts:
    # static method is declared with _method_name and without self keyword and @staticmethod is included at start
    # we don't usually use self. to call static methods, we instead use Class_Name._static_method_name
    # we can use self._static_method to call it as a instance but it is slower and performance suffers
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    """ simple account class with balance """
    def __init__(self, name, balance):
        # assigning attributes
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("account created for {}".format(self.name))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # self is necessary in python contrary to java this keyword
            self.show_balance()
            self.transaction_list.append((Accounts._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("not enough balance")
            self.show_balance()  # we can use method from another method using .self keyword

    def show_balance(self):
        print("balance is {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:  # in deposit method we append amount and date_time to transaction_list
                tran_type = "deposited"
            else:
                tran_type = "withdrawal"
                amount *= -1
            print("{:6} {} on {} local time was {})".format(amount, tran_type, date, date.astimezone()))

# when we import this python file to another python file and run it's function the code after if __name__ == '__main__':
# the lines after it is not executed
# in this file __name__ = __main__
# in a python file that imports this file __name__ = this_file_name(i.e oops(2)methods_encapsulation_accounts.py) so the
# condition is not met


if __name__ == '__main__':
    aashiq = Accounts("aashiq", 0)
    aashiq.show_balance()

    aashiq.deposit(1000)
    aashiq.show_balance()
    aashiq.withdraw(50000)
    aashiq.show_balance()
    aashiq.show_transactions()



