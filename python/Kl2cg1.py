#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Kl2cg1.html
#  
#  Copyright 2018  <>
 
import turtle


def figura(bok, kat, ile):
    for i in range(ile):
        turtle.forward(bok)
        turtle.right(kat)
        
def figura_rek(bok, kat, ile):
    turtle.forward(bok)
    turtle.right(kat)
    if ile > 0: 
        figura_rek(bok ,kat, ile)
        
        
    








def main(args):
    turtle.setup(800,600)
    turtle.color('red', 'blue')
    turtle.begin_fill()
    turtle.speed(0)
  
    figura_rek(10,99, 100000)
    
    
    
    
    turtle.end_fill()
    turtle.done()
    
    
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
