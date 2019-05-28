'''
Created on May 28, 2019

@author: AA
'''
class Bus:
    def __init__(self, passengers = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
            
    def pick(self,name):
        self.passengers.append(name)
        
    def drop(self,name):
        self.passengers.remove(name)
        
if __name__ == '__main__':
    import copy
    bus1 = Bus(['Alice','Bill','Clair','David'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    bus1.drop('Bill')
    print(bus2.passengers)
    print(bus3.passengers)