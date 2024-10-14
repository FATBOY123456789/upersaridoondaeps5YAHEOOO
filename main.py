class IOString:
    def __init__(self):
        self.str1=''
    def getstring(self):
        self.str1=input('Enter any string :) : ')
    def showstring(self):
        print('Given string in capitilazation is: ',self.str1.upper())
c1=IOString()
c1.getstring()
c1.showstring()