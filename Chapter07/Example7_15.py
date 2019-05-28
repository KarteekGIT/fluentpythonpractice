'''
Created on May 28, 2019

@author: AA
A simple decorator to output the running time of functions
'''
import time
from Chapter07.clockdeco import clock

@clock
def snooze(seconds):
    time.sleep(seconds)
    
@clock
def fact(n):
    return 1 if n < 2 else n * fact(n-1)

if __name__ == '__main__':
    print('*'*40, 'Calling snooze(0.123)')
    snooze(0.123)
    print('*'*40,'Calling fact(6)')
    print('6! = ' ,fact(6))