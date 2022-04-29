# /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  20221BSI0153.py
#  
#  Copyright 2022 Marllon Christiani dos Santos Ribeiro
#  

def main():

    a = int (0)
    b = int (0)
    c = int (0)
    maior = int (0)

    
    a = int(input())
    b = int(input())
    c = int(input())

    
    if b > a :
        maior = b
    else:
        maior = a
    if c > maior :
        maior = c

    while a != 0 or b != 0 or c != 0:
         
        print(f"MAIOR ({a}, {b}, {c}) = {maior}")

        a = int(input())
        b = int(input())
        c = int(input())


        if b > a :
            maior = b
        else:
            maior = a
        if c > maior :
            maior = c
        

if __name__ == "__main__":
    main()