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

def bloodgroup():
    win1 = Toplevel(root)
    win1.title('Blood Group')
    #win1.configure(background = "white")
    global mom, dad
    mom = StringVar(win1)
    mom.set('A')
    mom_grp = OptionMenu(win1, mom, 'A', 'B', 'AB', 'O').pack()
    dad = StringVar(win1)
    dad.set('A')
    dad_grp = OptionMenu(win1, dad, 'A', 'B', 'AB', 'O').pack()
    
    ok_button = Button(win1, text='ok',command=ok).pack()
def ok(x):
    '''
    if x == 'A':
        tkMessageBox.showinfo('asdsaf','erwrt')
    '''
    print mom.get()


bldgrp = Button(root, text = 'Blood Group' , command = bloodgroup).pack()

root.mainloop()

