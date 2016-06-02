class simple_arithmetic:
    '''This object takes two arguments at initialization. there are four methods that will return 
    simple arithmetic operations'''
    def __init__(self,arg1,arg2):
        self.arg1 = arg1
        self.arg2 = arg2
    def add(self):
        return self.arg1+self.arg2
    def sub(self):
        return self.arg1-self.arg2
    def div(self):
        return float(self.arg1)/float(self.arg2)
    def mult(self):
        return self.arg1*self.arg2
