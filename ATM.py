class ATM:
        
        def __init__(self, username, pin):
                self.username = username
                self.pin = pin
                self.value = 0

        def getPin(self):
                return self.pin

        def getValue(self):
                return self.value
        
        def withDraw(self):
                pin = input("Enter amount: ")
                if (pin = self.pin):
                        monremove = input("Enter amount: ")
                        if (monremove > self.value):
                                print "You don't have enough money to withdraw."
                        else:
                                self.value -= monremove
                                print "Withdrawn ", monremove, ". You now have ", self.value, "left."
                else:
                        print "Wrong pin."

                        
                        
        def addMoney(self):
                return self.pin
