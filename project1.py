'''
Baby Gene
PSIT Project
By Tharathip Malaimarn(tharamalai=>nam)
    Pawarisa Thong-ngoen(Jessegade=>gade)
APPLICATION to tell you
- chance of gene's your baby
--Blood Group
--Genetic Diseases
------Autosome Recessive
--------Thalassemia
--------Cystic fibrosis
--------Phenylketonuria(PKU)
--------Albinism
------Autosome Dominant
--------Achondroplasia
------Sex-linked Gene
--------X-linked gene
----------Color blindness
----------Glocose-6-phosphate dehydrogenase(G-6-PD)
----------Hemophilia
----------Duchennne's muscular dystrophy
----------Hypohidrotic Ectodermal Dysplasia
-----Sickle cell anemia
************this is only chance************
'''

from Tkinter import *
from PIL import ImageTk, Image
import tkMessageBox
root = Tk()
root.title('Baby Gene')                  

def bloodtype():
    win1 = Toplevel(root)
    win1.title('Blood Type')
    #win1.configure(background = "white")
    global mom, dad
    
    mom_text = Label(win1, text='Mother Blood Type: ').grid(row=0, column=0)

    mom = StringVar(win1)
    mom.set('A')
    mom_type = OptionMenu(win1, mom, 'A', 'B', 'AB', 'O').grid(row=0, column=1)

    dad_text = Label(win1, text='Father Blood Type: ').grid(row=2, column=0)
    
    dad = StringVar(win1)
    dad.set('A')
    dad_type = OptionMenu(win1, dad, 'A', 'B', 'AB', 'O').grid(row=2, column=1)
    ok_button = Button(win1, text='ok',command=ok).grid(row=3, column=1)
def ok():
    mom_and_dad = str(mom.get())+str(dad.get())
    group = {'AA': ['A 50%', 'O 50%'], \
             'BB': ['B 50%', 'O 50%'], \
             'ABAB': ['A 33.33%', 'B 33.33%' ,'AB 33.33%'], \
             'OO': ['O 100%'], \
             'AB': ['A 25%', 'B 25%', 'AB 25%', 'O 25%'], \
             'BA': ['A 25%', 'B 25%', 'AB 25%', 'O 25%'], \
             'AAB': ['A 33.33%', 'B 33.33%' ,'AB 33.33%'], \
             'ABA': ['A 33.33%', 'B 33.33%' ,'AB 33.33%'], \
             'BAB': ['A 33.33%', 'B 33.33%' ,'AB 33.33%'], \
             'ABB': ['A 33.33%', 'B 33.33%' ,'AB 33.33%'], \
             'ABO': ['A 50%', 'B 50%'], \
             'OAB': ['A 50%', 'B 50%'], \
             'AO': ['A 50%', 'O 50%'], \
             'OA': ['A 50%', 'O 50%'], \
             'BO': ['B 50%', 'O 50%'], \
             'OB': ['B 50%', 'O 50%']}
    tkMessageBox.showinfo('Result',' or '.join(group[mom_and_dad]))
    


bldgrp = Button(root, text = 'Blood Group' , command = bloodtype).pack()

root.mainloop()
