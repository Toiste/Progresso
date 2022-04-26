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
    texto = str("")

    
    a = int(input())
    b = int(input())
    c = int(input())

    
    if a > b and a > c:
        maior = a

    if b > c and b > a:
        maior = b

    if c > b and c > a:
        maior = c
    
    if a == b  == c :
        maior = a
    
    if a == b and a != c and a > c :
        maior = a
    
    if a == c and a != b and a > b :
        maior = a
    
    if b == a and b != c and b > c  :
        maior = b

    if b == c and b != a and b > a :
        maior = b

    if c == a and c != b and c > b :
        maior = c

    if c == b and c != a and c > a :
        maior = c

    while a != 0 or b != 0 or c != 0:
         
        texto += (f"MAIOR ({a}, {b}, {c}) = {maior}\n")
        
        
        a = int(input())
        b = int(input())
        c = int(input())
        
        
        if a > b and a > c:
            maior = a

        if b > c and b > a:
            maior = b
    
        if c > b and c > a:
            maior = c
        
        if a == b  == c :
            maior = a
        
        if a == b and a != c and a > c :
            maior = a
        
        if a == c and a != b and a > b :
            maior = a
        
        if b == a and b != c and b > c  :
            maior = b

        if b == c and b != a and b > a :
            maior = b

        if c == a and c != b and c > b :
            maior = c

        if c == b and c != a and c > a :
            maior = c


    print (texto);


if __name__ == "__main__":
    main()