#-*- coding: utf-8 -*-

####### PROGRAMME DE GESTION DE ENZYMES #######

##### LES LISTES #####

'''
Un dictionnaire c'est une clé qui permet d'accéder rapidement à ce qu'on recherche
Basic manipulation
Declaration :
dict ={ }or dict={’jambon’:2,’oeufs’:3,’pain’:1}
Number of elements : len(dict)
Pay attention ! dict[2]return error.
Access to elements dict[’jambon’]return 2.
Test if exist : dict.has_key(’pain’) return 1 for True
Getting the key list : dict.keys()
dict.values
Getting dictionary content as tuples dict.items()


'''

'''
Enzyme program : Write a program allowing to
— type a name and weight of an enzyme
— store in 1 or 2 lists
— display the values
— compute mean, min and max values of weight
— display name of enzyme with a weight greater than mean value
— display information about enzyme with a name given by the user
'''

import sys

#ajouter une enzyme

def ajouter_une_enzyme(L1): # gestion d'erreur
    name = raw_input("entrer le nom d'une enzyme : \n")
    L1[name] = input("entrer le poid de l'enzyme: \n")
    return L1

#afficher les enzymes en banque

def afficher_les_enzymes(L1): #améliorer pour voir les poids aussi
   for i in L1:
       print i


#mean value of weight

def mean(L1):
    somme=0
    for i in L1.values():
        somme = somme + i
    return  somme

#min value of weight

def min(L):
  size = len(L)
  if size ==0:
    return None
  list=L.values()
  min=list[0]
  for i in list:
    if i < min:
      min=i
  return min

#max value of weight

def max(L):
  size = len(L)
  if size ==0:
    return None
  list=L.values()
  max=list[0]
  for i in list:
    if i > max:
      max=i
  return max

#afficher les informations d'une enzyme

def info(L):
    name=raw_input("entrer le nom de l'enzyme que vous recherchez : \n")
    if name in L:
        print "le poids de l'enzyme est : ", L[name]
    else:
        print "Cette enzyme n'est pas en banque"
        
#display name of enzyme with a weight greater than mean value

def supp(L,M):
    e=0
    for i in L.values():
        list=L.keys()
        if i >= M:
            print list[e]
            e=e+1
        else:
            e=e+1
            
            
       


######## MENU ########

def menu(lol):
    print "======================================== MENU ========================================="
    print "\n"
    print "taper 1 pour ajouter une enzyme"
    print "taper 2 pour afficher les enzymes de la banque"
    print "taper 3 pour afficher la moyenne des poids des enzymes"
    print "taper 4 pour afficher le poids le plus petit"
    print "taper 5 pour afficher le poids le plus grand"
    print "taper 6 pour afficher les informations d'une enzyme"
    print "taper 7 pour afficher les enzyme dont le poids est suppérieur à la moyenne des enzymes"
    print "taper 0 pour quitter"
    print "\n"
    print "======================================================================================="


 
def commandes(nb): 
    while nb != 0:
        menu(0)
        nb=raw_input() 
        if nb == "1":
            ajouter_une_enzyme(enzyme)
        elif nb == "2":
            if len(enzyme) == 0:
                print "Pas d'enzyme en banque"
            else:
                afficher_les_enzymes(enzyme)
        elif nb == "3":
            if len(enzyme) == 0:
                print "Pas d'enzyme en banque"
            else:
                print mean(enzyme)/len(enzyme) , ",", mean(enzyme)%len(enzyme)
        elif nb == "4":
            if len(enzyme) == 0:
                print "Pas d'enzyme en banque"
            else:
                print min(enzyme)
        elif nb == "5":
            if len(enzyme) == 0:
                print "Pas d'enzyme en banque"
            else:
                print max(enzyme)
        elif nb == "6":
            if len(enzyme) == 0:
                print "Pas d'enzyme en banque"
            else:
                info(enzyme)
        elif nb == "7":
            if len(enzyme) == 0:
                print "Pas d'enzyme en banque"
            else :
                moy = mean(enzyme)/len(enzyme)
                supp(enzyme,moy)
        elif nb == "0":
            print "Bye"
            sys.exit()
        else:
            print "ERREUR : mauvaise valeur"
    

######## MAIN ########

enzyme={"lol":10,"war":5,"cry":15}

print "start ------>", 1 #faire la boucle avec la sortie
print "stop  ------>", 0

rep=input()
commandes(rep)

#moyennes 3 et 7 qui fonctionnent pas
