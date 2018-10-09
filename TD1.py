#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 16:16:14 2018

@author: clemcsweeny
"""
#### PROBLEM 16: Power digit sum ####

def problem16(n):
    k=0
    while n!=0:
        k+=(n%10)
        n=n//10
    return k

#### PROBLEM 22: Names scores ####


def problem22():
    f=open('p022_names.txt','r')
    
    for line in f:
        l=line.split(",")
        
    L=sorted(l)
    
    S=0 ### S est le score total de la liste
    alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for nom in L:
        s=0  ### s est le score d'un nom de la liste
        
        for j in range(len(nom)): ### calcul du score grace aux lettres du nom
            for i in range(len(alpha)):
                if alpha[i]==nom[j]:
                    s+=i+1
            
        for k in range(len(L)): ### recherche du placement du nom dans la liste
            if L[k]==nom:
                c=k+1
        S+=(s*c)
        
    return S



##### PROBLEM 55: Nombre de Lychrel #####
 
# Fonction qui inverse les chiffres d'un nombre :

def reverse(n):
    N=str(n)
    L=''
    for k in N:
        L=k+L
    return int(L)

# Fonction qui verifie si un nombre est palyndrome :

def palyndrome(n):
    return n==reverse(n)

# Fonction qui verifie si un nombre est un nombre de Lychrel :

def lychrel(n):
    for k in range(50):
           if palyndrome(n+reverse(n)):
               return False
           else:
               n+=reverse(n)
    return True
   

# Fonction qui compte les nombres de Lychrel inferieurs a 10 000 :
    
def problem55():
    k=0
    for j in range(10**4):
        if lychrel(j):
            k+=1
    return k


### Resultat: 249