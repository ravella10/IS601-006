class MyCalcy:

    def __init__(self,ans = 0):
        self.ans = ans
        self.ops = {'+': self.addition,
        '-': self.substraction,
        '*': self.multiplication,
        'x': self.multiplication,
        '/': self.division}

    @staticmethod
    def _is_float(val):
        #id - pr457, date - 2/27/23
        try:
            float(val)
            return True
        except:
            return False

    @staticmethod
    def _is_int(val):
        #id - pr457, date - 2/27/23
        try:
            int(val)
            return True
        except:
            return False

    @staticmethod
    def _as_number(val):
        #id - pr457, date - 2/27/23
        if MyCalcy._is_int(val):
            return int(val)
        elif MyCalcy._is_float(val):
            return float(val)
        else:
            raise Exception("Not a number")

    def addition(self, a, b):
        #id - pr457, date - 2/27/23
        #checks if the first input passed is ans and assigns self.ans to a if it is. _as_number utility function is used to convert string to num
        #Then addition is performed and stored in ans instance variable as string and returns the value
        if a == "ans":
                a = self.ans
        a = self._as_number(a)
        b = self._as_number(b)
        self.ans = str(a+b)
        return self.ans
        
    def substraction(self, a, b):
        #id - pr457, date - 2/27/23
        #checks if the first input passed is ans and assigns self.ans to a if it is. _as_number utility function is used to convert string to num
        #Then substraction is performed and stored in ans instance variable as string and returns the value
        if a == "ans":
                a = self.ans
        a = self._as_number(a)
        b = self._as_number(b)
        self.ans = str(a-b)
        return self.ans

    def multiplication(self, a, b):
        #id - pr457, date - 2/27/23
        #checks if the first input passed is ans and assigns self.ans to a if it is. _as_number utility function is used to convert string to num
        #Then multiplication is performed and stored in ans instance variable as string and returns the value
        if a == "ans":
                a = self.ans
        a = self._as_number(a)
        b = self._as_number(b)
        self.ans = str(a*b)
        return self.ans

    def division(self, a, b):
        #id - pr457, date - 2/27/23
        #checks if the first input passed is ans and assigns self.ans to a if it is. _as_number utility function is used to convert string to num
        #Then division is performed and stored in ans instance variable as string and returns the value
        #Exception handling is used to handle division by zero error. if the error occurs, ans instance variable value remains unchanged
        if a == "ans":
                a = self.ans
        a = self._as_number(a)
        b = self._as_number(b)
        try:
            self.ans = str(a/b)
            return self.ans
        except ZeroDivisionError:
            print("Division with zero. Result remains unchanged from previous value")
            return self.ans
    

def main():
    is_running = True
    iSTR = input("Are you ready?")
    calc = MyCalcy()
    if iSTR == "yes":
        while is_running:
            iSTR = input("What is your eq:")
            if iSTR == "quit" or iSTR == "q":
                is_running = False
            else:
                print("Your eq was " + str(iSTR))
                checks = ["+",  "/", "*", "x", "-"]
                handled = False
                for check in checks:
                    if not handled and check in iSTR:
                        nums = iSTR.split(check)
                        a = nums[0].strip()
                        b = nums[1].strip()
                        r = calc.ops[check](a, b)
                        print("R is " + str(r))
                        handled = True
                if not handled:
                    print("The action you tried is not supported, please try again")
    else:  # exit loop
        print("Good bye")
        is_running = False

if __name__ == '__main__':
    main()


    