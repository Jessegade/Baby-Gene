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

import Tkinter as tk
from PIL import ImageTk, Image
import tkMessageBox

class Print(object):
    '''
    input
    Print(root, text, row, column)
    '''
    def __init__(self, root, text, row, column):
        self.text = text
        self.row = row
        self.column = column
        self.message = tk.Message(root, text=text)
        self.message.grid(row=self.row, column=self.column)

class Built_Button(object):
    '''
    input
    Built_Button(root, text, value, row, column)
    '''
    def __init__(self, root, text, value, row, column):
        self.root = root
        dic = {'bloodgroup':bloodtype, 'thalassemia':thalassemia,
               'galactosemia':galactosemia, 'cysticfibrosis':cysticfibrosis,
               'phenylketoneuria':phenylketoneuria, 'glycogen':glycogen,
               'acondroplasia':acondroplasia,
               'colorblindness':colorblindness}
        if value in dic:
            self.value = dic[value]
        else:
            self.value = value
        self.button = tk.Button(self.root, text=text, command=self.value)
        self.button.grid(row=row, column=column)

class Family(object):
    '''
    input
    Family(root, name)
    '''
    def __init__(self, root, name, code):
        self.name = name
        self.root = root
        self.code = code
        self.tree()
    def tree(self):
        self.root.destroy()
        self.root = tk.Tk()
        diseasedname = Print(self.root, self.name, row=0, column=4)

        global poo, yaa, taa, yay, dad, mom
       
        poo_show = Print(self.root, "Grandfather", row=4, column=1)
        self.poo = tk.StringVar(self.root)
        self.poo.set('NORMAL')
        poo_type = tk.OptionMenu(self.root, self.poo, 'NORMAL', 'DISEASED', 'CARRIER').grid(row=5, column=1)

        yaa_show = Print(self.root, "Grandmother", row=4, column=3)
        self.yaa = tk.StringVar(self.root)
        self.yaa.set('NORMAL')
        yaa_type = tk.OptionMenu(self.root, self.yaa, 'NORMAL', 'DISEASED', 'CARRIER').grid(row=5, column=3)

        taa_show = Print(self.root, "Grandfather", row=4, column=6)
        self.taa = tk.StringVar(self.root)
        self.taa.set('NORMAL')
        taa_type = tk.OptionMenu(self.root, self.taa, 'NORMAL', 'DISEASED', 'CARRIER').grid(row=5, column=6)

        yay_show = Print(self.root, "Grandmother", row=4, column=8)
        self.yay = tk.StringVar(self.root)
        self.yay.set('NORMAL')
        yay_type = tk.OptionMenu(self.root, self.yay, 'NORMAL', 'DISEASED', 'CARRIER').grid(row=5, column=8)

        dad_show = Print(self.root, "DADDY", row=7, column=2)
        self.dad = tk.StringVar(self.root)
        self.dad.set('NORMAL')
        dad_type = tk.OptionMenu(self.root, self.dad, 'NORMAL', 'DISEASED', 'CARRIER').grid(row=8, column=2)

        mom_show = Print(self.root, "MOMMY", row=7, column=7)
        self.mom = tk.StringVar(self.root)
        self.mom.set('NORMAL')
        mom_type = tk.OptionMenu(self.root, self.mom, 'NORMAL', 'DISEASED', 'CARRIER').grid(row=8, column=7)

        process = tk.Button(self.root, text='PROCESS',command=self.bus).grid(row=10, column=4)

    def bus(self):
        st = {'DISEASED':'D', 'NORMAL':'N', 'CARRIER':'C'}
        poo, yaa, dad = st[self.poo.get()], st[self.yaa.get()], st[self.dad.get()]
        taa, yay, mom = st[self.taa.get()], st[self.yay.get()], st[self.mom.get()]
        if self.code == 'AR':
            autosomerecessive(self.root, poo, yaa, taa, yay, dad, mom, self.code, self.name)
        elif self.code == 'AD':
            autosomedominant(self.root, poo, yaa, taa, yay, dad, mom, self.code, self.name)
        else:
            print 'h'

class Result(object):
    def __init__(self, root ,baby, name, code):
        self.root = root
        self.baby = baby
        self.name = name
        self.code = code
        self.print_gene()
    def print_gene(self):
        self.root.destroy()
        self.root = tk.Tk()

        head = Print(self.root, self.name, row=0, column=0)
    
        yourbaby = Print(self.root, self.predict(), row=1, column=0)

    def predict(self):
        if self.code == 'AR':
            didic = {'aa':self.name+' Diseased', 'Aa':self.name+' Carrier', 'AA':'Normal'}
        string = "your baby's gene is \n"
        for item in self.baby:
            string += didic[item] + '     ' + str(self.baby[item] * 25) + '%' + '\n'
        string += '***it only probability***'
        return string
        
def bloodtype():
    print 'error'
##    win1 = tk.Tk()
##    win1.title('Blood Type')
##    #win1.configure(background = "white")
##    global mom, dad
##    
##    mom_text = tk.Label(win1, text='Mother Blood Type: ').grid(row=0, column=0)
##
##    mom = tk.StringVar(win1)
##    mom.set('A')
##    mom_type = tk.OptionMenu(win1, mom, 'A', 'B', 'AB', 'O').grid(row=0, column=1)
##
##    dad_text = tk.Label(win1, text='Father Blood Type: ').grid(row=2, column=0)
##    
##    dad = tk.StringVar(win1)
##    dad.set('A')
##    dad_type = tk.OptionMenu(win1, dad, 'A', 'B', 'AB', 'O').grid(row=2, column=1)
##    ok_button = tk.Button(win1, text='ok',command=ok).grid(row=3, column=1)
##def ok():
##    mom_and_dad = str(mom.get())+str(dad.get())
##    group = {'AA': ['A 50%', 'O 50%'], \
##             'BB': ['B 50%', 'O 50%'], \
##             'ABAB': ['A 33.33%', 'B 33.33%' ,'AB 33.33%'], \
##             'OO': ['O 100%'], \
##             'AB': ['A 25%', 'B 25%', 'AB 25%', 'O 25%'], \
##             'BA': ['A 25%', 'B 25%', 'AB 25%', 'O 25%'], \
##             'AAB': ['A 33.33%', 'B 33.33%' ,'AB 33.33%'], \
##             'ABA': ['A 33.33%', 'B 33.33%' ,'AB 33.33%'], \
##             'BAB': ['A 33.33%', 'B 33.33%' ,'AB 33.33%'], \
##             'ABB': ['A 33.33%', 'B 33.33%' ,'AB 33.33%'], \
##             'ABO': ['A 50%', 'B 50%'], \
##             'OAB': ['A 50%', 'B 50%'], \
##             'AO': ['A 50%', 'O 50%'], \
##             'OA': ['A 50%', 'O 50%'], \
##             'BO': ['B 50%', 'O 50%'], \
##             'OB': ['B 50%', 'O 50%']}
##    tk.ACTIVEtkMessageBox.showinfo('Result',' or '.join(group[mom_and_dad]))

def cross(male, female, code, re):
    if code == 'AR':
        gtab = {'D':'aa', 'C':'Aa', 'N': 'AA'}
    #edit
    elif code == 'AD':
        gtab = {'N':'aa', 'D':'Aa', 'D': 'AA'}
    else:
        'wait'
    genotype = dict()
    male, female = gtab[male], gtab[female]
    for s in male:
        for e in female:
            geno = [s, e]
            geno.sort()
            geno = geno[0] + geno[1]
            if geno in genotype:
                genotype[geno] += 1
            else:
                genotype[geno] = 1
    print genotype
    if code == 'AR':
        if re == 'check':
            if 'aa' in genotype:
                return 'D'
            elif 'Aa' in genotype:
                return 'C'
            else:
                return 'N'
        else:
            return genotype
def autosomerecessive(root, poo, yaa, taa, yay, dad, mom, code, name):
    print poo, yaa, taa, yay, dad, mom, code
    if dad == 'N':
        dad = cross(poo, yaa, code, 'check')
        if dad == 'D':
            dad = 'C'
    print dad
    if mom == 'N':
        mom = cross(taa, yay, code, 'check')
        if mom == 'D':
            mom = 'C'
    print mom
    baby = cross(dad, mom, code, 'baby')
    print_result = Result(root, baby, name, code)

def autosomedominant(root, poo, yaa, taa, yay, dad, mom, code, name):
    print poo, yaa, taa, yay, dad, mom, code
    if dad == 'N':
        dad = cross(poo, yaa, code, 'check')
        if dad == 'D':
            dad = 'C'
    print dad
    if mom == 'N':
        mom = cross(taa, yay, code, 'check')
        if mom == 'D':
            mom = 'C'
    print mom
    baby = cross(dad, mom, code, 'baby')
    print_result = Result(root, baby, name, code)
#Autosome Recessive Disease  
def thalassemia():
    thala = Family(root, 'Thalassemia', 'AR')

def galactosemia():
    galac = Family(root, 'Galactosemia', 'AR')

def cysticfibrosis():
    cystic = Family(root, 'Galactosemia', 'AR')

def phenylketoneuria():
    phenyl = Family(root, 'Phenylketoneuria', 'AR')

def glycogen():
    glyco = Family(root, 'Glycogen Storage Disease', 'AR')

#Autosome Dominant Disease

def acondroplasia():
    acon = Family(root, 'Acondroplasia', 'AD')
def colorblindness():
    color = Family(root, 'Color Blindness', 'XL')
    
root = tk.Tk()

def main():
    '''screen'''
    welcome = Print(root, 'BABY GENE', row=0, column=1)
    bloodgroup = Built_Button(root, 'Blood Group', 'bloodgroup', row=1, column=1)
    
    ar = Print(root, 'Autosome Recessive', row=2,column=1)
    thalassemia = Built_Button(root, 'Thalassemia', 'thalassemia', row=3, column=1)
    galac = Built_Button(root, 'Galactosemia', 'galactosemia', row=4, column=1)
    cystic = Built_Button(root, 'Cystic Fibrosis', 'cysticfibrosis', row=5, column=1)
    phenyl = Built_Button(root, 'Phenylketoneuria', 'phenylketoneuria', row=6, column=1)
    glyco = Built_Button(root, 'Glycogen Storage Disease', 'glycogen', row=6, column=1)

    ad = ar = Print(root, 'Autosome Dominant', row=7,column=1)
    acon = Built_Button(root, 'Acondroplasia', 'acondroplasia', row=8, column=1)
    xlink = Print(root, 'X-link Recessive', row=10,column=1)
    color = Built_Button(root, 'Color Blindness', 'colorblindness', row=11, column=1)

main()

root.mainloop()
        