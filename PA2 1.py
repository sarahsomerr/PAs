# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 13:46:52 2024

@author: Joe, Noah, Max, Sarah
"""
import random
SECS_PER_ITEM = 4
INTERVAL_OF_CUSTOMER_CREATION = 30

class Queue: 
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def getCurrentCustomer(self): #returns the first item originally entered into the list 
        return self.items[len(self.items)-1] #returns the current customer being treated (it will be the last in the list since the enque adds the new customer in the zero spot)
    
    def getList(self):
        return self.items
    #
      

class customer():
    def __init__(self):
        self.items = random.randint(6,20)
        self.timePerThisCustomer = (SECS_PER_ITEM*self.items)+45 #the time to checkout for that customer
        
    def getItems(self):
        return self.items
    
    
    def updateTime(self): #this is essentially a countdown that subtracts one from the checkout time 
        self.timePerThisCustomer = self.timePerThisCustomer - 1
    
    def getCustomerTime(self): #returns the checkout time
        return self.timePerThisCustomer

class register(customer):
    
    def __init__(self,name):
        self.name = name
        self.line = Queue()
        self.hasACustomer = False
        self.checkOutTimeRemaining = 0
        self.totItems = 0
        self.totCustomers = 0
        self.idleTime = 0
        self.waitTime = 0
    
    def moveThroughLineOneSec(self): #this is the function that runs every second in the simulation, it decreases the checkout time of the current customer by one 
        if self.hasACustomer == True:
            checkOutTimeRemaining = self.line.getCurrentCustomer().getCustomerTime()
            if checkOutTimeRemaining > 0:
                self.line.getCurrentCustomer().updateTime()#decreases the time by one 
                if self.line.size()>=2:
                    self.waitTime = self.waitTime + 1 #increases wait time if the line is greater than or equal to 2 meaning there is one other person other than the current customer 
            elif checkOutTimeRemaining == 0: #they are done  checking out 
                removedCustomer = self.line.dequeue()
                self.totItems = self.totItems + removedCustomer.getItems()
                if self.line.size() == 0:
                    self.hasACustomer = False
                    self.idleTime = self.idleTime+1 #adds to the idle time (no one is in the line)
            
    def checkCustomer(self):
        return self.hasACustomer
    
    def getIdleTime(self):
        return self.idleTime
    
    def getWaitTime(self):
        return self.waitTime
            
    def printCustomerList(self):
        if self.line.size() == 1: #if only one customer 
            string = f'  {self.line.getCurrentCustomer().getItems()} | '
            return string
        if self.line.size() >=2: #if one of more customers, adds the items next the |, the next customer will be on far right 
            string = f'  {self.line.getCurrentCustomer().getItems()} | ' #initial string
            for i in range(self.line.size()-1):
                string = string + f'  {self.line.getList()[i].getItems()}  '#adds the next customer items 
           # return (f'  {self.line.getCurrentCustomer().getItems()} |{self.line.getList()[len(self.line.getList())-2].getItems()}')
            return string 
    
        else:
            return ("  --") #if no customers in the line 
        
    def addCustomer(self,customer): #adds customer to the register
        self.line.enqueue(customer)
        self.totCustomers = self.totCustomers + 1
        self.hasACustomer = True
              
    def getTotItems(self):
        return self.totItems
    
    def getTotCustomers(self):
        return str(self.totCustomers)
    
def simulation():
    # set up lines
    line1 = register('one')
    line2 = register('two')
    line3 = register('three')
    line4 = register('four')
    line5 = register('five') #IF you want five non expresslines, uncomment 
    express = register('express')
    #the possible lines a customer can go in if they have less than or greater than 10 items 
    possibleLinesLess10 = [line1,line2,line3,line4,line5,express]
    possibleLinesGreater10 = [line1,line2,line3,line4,line5]
    #the time of the simulation is 2 hours of 7200 seconds
    for time in range(7200):
        #checks the line every single second
        express.moveThroughLineOneSec()
        line1.moveThroughLineOneSec() 
        line2.moveThroughLineOneSec() 
        line3.moveThroughLineOneSec() 
        line4.moveThroughLineOneSec() 
        line5.moveThroughLineOneSec() 

        #adds new customer every 30 sec
        if time>0 and time%INTERVAL_OF_CUSTOMER_CREATION == 0:
            newCustomer = customer() #creates new customer

            
            if newCustomer.getItems() < 10: #if they have less than 10 items 
                if express.checkCustomer() == False: #if express is empty
                    express.addCustomer(newCustomer)
                else: #express is not empty
                    smallest = express.line.size() #smallest is currently express
                    emptiestLines = []
                    for i in possibleLinesLess10: #checks all lines to find smalles num
                        temp = i.line.size()
                        if temp <= smallest: #if the temp is smaller than the smallest
                            smallest = temp
                    for i in possibleLinesLess10:  #run it again to create a list of the smallest registers     
                        if i.line.size() == smallest:
                            emptiestLines.append(i)
                    if len(emptiestLines) == 1: #if one line is smallest
                        emptiestLines[0].addCustomer(newCustomer)
                    else: #if greater than one, randomly choose the line
                        num = random.randint(0, len(emptiestLines)-1)
                        emptiestLines[num].addCustomer(newCustomer)
            else: #greater than 10 
                   lowestNum = line1.line.size() #smallest is currently express
                   emptiestLines = []
                   for i in possibleLinesGreater10: #checks all lines to find the smallest number 
                       temp = i.line.size()
                       if temp <= lowestNum: #if the temp is smaller than the smallest
                           lowestNum = temp
                   for i in possibleLinesGreater10:#creates a list of the smallest lines 
                       if i.line.size() == lowestNum:
                           emptiestLines.append(i)
                   if len(emptiestLines) == 1: #if one line is smaller
                       emptiestLines[0].addCustomer(newCustomer)
                   else: #greater than one, randomly choose the line
                       num = random.randint(0, len(emptiestLines)-1)
                       emptiestLines[num].addCustomer(newCustomer)
                  
            
        if time%50 == 0: #prints of the data every 50 secs
            
            print(f'time={time}')
            print(f'reg#   customers')
            print('    0.' + line1.printCustomerList())
            print('    1.' + line2.printCustomerList())
            print('    2.' + line3.printCustomerList())
            print('    3.' + line4.printCustomerList())
            print('    4.' + line5.printCustomerList())
            print('    5.' + express.printCustomerList())
            print('\n')
    #return statement of all data needed in the table at the very end 
    return (line1.getTotItems(),line1.getTotCustomers(), line1.getIdleTime(), line1.getWaitTime(), 
            line2.getTotItems(),line2.getTotCustomers(), line2.getIdleTime(), line2.getWaitTime(), 
            line3.getTotItems(),line3.getTotCustomers(),line3.getIdleTime(), line3.getWaitTime(),
            line4.getTotItems(),line4.getTotCustomers(),line4.getIdleTime(), line4.getWaitTime(),
            line5.getTotItems(),line5.getTotCustomers(),line5.getIdleTime(), line5.getWaitTime(),
            express.getTotItems(),express.getTotCustomers(),express.getIdleTime(), express.getWaitTime())

    
def main():#runs the simulation and creates the table 
    line1Items = 0
    line1Customers = 0
    line1Idle = 0
    line1Wait = 0

    line2Items = 0 
    line2Customers = 0 
    line2Idle = 0
    line2Wait = 0
    
    line3Items = 0 
    line3Customers = 0 
    line3Idle = 0
    line3Wait = 0
    
    line4Items = 0
    line4Customers = 0 
    line4Idle = 0
    line4Wait = 0
    
    line5Items = 0
    line5Customers = 0 
    line5Idle = 0
    line5Wait = 0
    
    expressItems = 0
    expressCustomers = 0
    expressIdle = 0
    expressWait = 0
    
    for i in range(12):#runs simulation 12 times 
        line1totItems, line1totCustomers, line1IdleTime, line1WaitTime, line2totItems, line2totCustomers, line2IdleTime, line2WaitTime, line3totItems, line3totCustomers, line3IdleTime, line3WaitTime, line4totItems, line4totCustomers, line4IdleTime,line4WaitTime,line5totItems, line5totCustomers, line5IdleTime,line5WaitTime, expresstotItems, expresstotCustomers, expressIdleTime,expressWaitTime = simulation()    
        
        #adds the returned data to the varaibles 
        line1Items = line1Items + int(line1totItems)
        line1Customers = line1Customers + int(line1totCustomers)
        line1Idle = line1Idle + int(line1IdleTime)
        line1Wait = line1Wait + int(line1WaitTime)
        
        line2Items = line2Items + int(line2totItems)
        line2Customers = line2Customers + int(line2totCustomers)
        line2Idle = line2Idle + int(line2IdleTime)
        line2Wait = line2Wait + int(line2WaitTime)
        
        line3Items =  line3Items + int(line3totItems)
        line3Customers = line3Customers + int(line3totCustomers)
        line3Idle = line3Idle + int(line3IdleTime)
        line3Wait = line3Wait + int(line3WaitTime)
        
        line4Items = line4Items + int(line4totItems)
        line4Customers = line4Customers + int(line4totCustomers)
        line4Idle = line4Idle + int(line4IdleTime)
        line4Wait = line4Wait + int(line4WaitTime)
        
        line5Items = line5Items + int(line5totItems)
        line5Customers = line5Customers + int(line5totCustomers)
        line5Idle = line5Idle + int(line5IdleTime)
        line5Wait = line5Wait + int(line5WaitTime)
        
        expressItems = expressItems + int(expresstotItems)
        expressCustomers = expressCustomers + int(expresstotCustomers)
        expressIdle = expressIdle + int(expressIdleTime)
        expressWait = expressWait + int(expressWaitTime)
    
    totCust = line1Customers + line2Customers + line3Customers + line4Customers + line5Customers + expressCustomers

    totItem = line1Items + line2Items + line3Items + line4Items + line5Items + expressItems

    totidle = line1Idle + line2Idle + line3Idle + line4Idle + line5Idle + expressIdle

    totwait = line1Wait + line2Wait + line3Wait + line4Wait + line5Wait + expressWait


    
    
    #prints out the table of the data over the course of the 12 simulations 
    print('TOTAL OF ALL SIMULATIONS:')
    print(f'Register   Total Customers   Total Items   Total Idle Time(min)   Total Wait Time(sec)')
    print(f'{1:^10} {line1Customers:^12} {line1Items:^15}   {line1Idle/60:^17.2f} {line1Wait:^30}')
    print(f'{2:^10} {line2Customers:^12} {line2Items:^15}  {line2Idle/60:^18.2f} {line2Wait:^30}')
    print(f'{3:^10} {line3Customers:^12}{ line3Items:^16}   {line3Idle/60:^17.2f} {line3Wait:^30}')
    print(f'{4:^10} {line4Customers:^12} {line4Items:^15}   {line4Idle/60:^17.2f} {line4Wait:^30}')
    print(f'{5:^10} {line5Customers:^12} {line5Items:^15}   {line5Idle/60:^17.2f} {line5Wait:^30}')
    print(f'{6:^10} {expressCustomers:^12} {expressItems :^15}   {expressIdle/60:^17.2f} {expressWait:^30}')   
    
    print('_____________________________________________________________________________')

    print(f'TOTAL     {totCust:^12}  {totItem:^15} {totidle/60:^19.2f} {totwait:^30}')

#%%
main()
        
        