

def sumuj(a, b):
    """
    Funckja zwraca sumę dwóch podanych liczb 
    
    """
    
    return a + b
    
def roznica(a, b):
      
     return a - b 
    
    
def iloraz(a, b):
    """
    Funckja zwraca iloraz dwóch podanych liczb 
    
    """
    
    return a / b
    
    
def iloczyn(a, b):
    """
    Funckja zwraca iloczyn dwóch podanych liczb 
    
    """
    
    return a * b  
    
    
    
def main(args):
    #Zmienne lokalne, o zasięgu lokalnym
    
    a = int(input("Podaj 1. liczbę: ")) 
    b = int(input ("Podaj 2. liczbę: "))
    
    print(a) 
    print (b)
    
    print("Wynik wynosi=",sumuj(a, b))
    print(roznica(a, b))
    print(iloczyn(a, b))
    print(iloraz(a, b))
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

