'''
Baby Gene
PSIT Project
By Tharathip Malaimarn(tharamalai=>nam)
    Pawarisa Thong-ngoen(Jessegade=>gade)
APPLICATION to tell you
- probability of gene's your baby
--Blood Group
--Genetic Diseases
************it only probability************
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
        self.label = tk.Label(root, text=text)
        self.label.grid(row=self.row, column=self.column)

class Built_Button(object):
    '''
    input
    Built_Button(root, text, value, row, column)
    '''
    def __init__(self, root, text, value, row, column):
        self.root = root
        dic = {'bloodtype':bloodtype, 'thalassemia':thalassemia,
               'galactosemia':galactosemia, 'cysticfibrosis':cysticfibrosis,
               'phenylketoneuria':phenylketoneuria, 'glycogen':glycogen,
               'albinism':albinism, 'acondroplasia':acondroplasia,
               'marfansd':marfansd, 'neurofibro':neurofibro,
               'huntingron':huntingron, 'osteogenesis':osteogenesis,
               'peutzsd':peutzsd,'hemophilia':hemophilia,
               'g6pd':g6pd, 'duchenne':duchenne,
               'hypohidro':hypohidro, 'colorblindness':colorblindness}
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
        self.root.geometry("430x430+300+300")
        image = Image.open('win1.jpg')
        tkimage = ImageTk.PhotoImage(image)
        bg = tk.Label(self.root, image = tkimage)
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        diseasedname = tk.Label(self.root, text=self.name.upper()).grid(row=0, column=2)

        global poo, yaa, taa, yay, dad, mom

        if self.code == 'AR':
            
            poo_show = tk.Label(self.root, text="Grandfather").grid(row=4, column=1)
            self.poo = tk.StringVar(self.root)
            self.poo.set('NORMAL')
            poo_type = tk.OptionMenu(self.root, self.poo, 'NORMAL', 'DISEASED', 'CARRIER').grid(row=5, column=1)

            yaa_show = tk.Label(self.root, text="Grandmother").grid(row=4, column=3)
            self.yaa = tk.StringVar(self.root)
            self.yaa.set('NORMAL')
            yaa_type = tk.OptionMenu(self.root, self.yaa, 'NORMAL', 'DISEASED', 'CARRIER').grid(row=5, column=3)

            taa_show = tk.Label(self.root, text="Grandfather").grid(row=10, column=1)
            self.taa = tk.StringVar(self.root)
            self.taa.set('NORMAL')
            taa_type = tk.OptionMenu(self.root, self.taa, 'NORMAL', 'DISEASED', 'CARRIER').grid(row=11, column=1)

            yay_show = tk.Label(self.root, text="Grandmother").grid(row=10, column=3)
            self.yay = tk.StringVar(self.root)
            self.yay.set('NORMAL')
            yay_type = tk.OptionMenu(self.root, self.yay, 'NORMAL', 'DISEASED', 'CARRIER').grid(row=11, column=3)

            dad_show = tk.Label(self.root, text="Father").grid(row=7, column=2)
            self.dad = tk.StringVar(self.root)
            self.dad.set('NORMAL')
            dad_type = tk.OptionMenu(self.root, self.dad, 'NORMAL', 'DISEASED', 'CARRIER').grid(row=8, column=2)

            mom_show = tk.Label(self.root, text="Mother").grid(row=12, column=2)
            self.mom = tk.StringVar(self.root)
            self.mom.set('NORMAL')
            mom_type = tk.OptionMenu(self.root, self.mom, 'NORMAL', 'DISEASED', 'CARRIER').grid(row=13, column=2)

        else:
            poo_show = tk.Label(self.root, text="Grandfather").grid(row=4, column=1)
            self.poo = tk.StringVar(self.root)
            self.poo.set('NORMAL')
            poo_type = tk.OptionMenu(self.root, self.poo, 'NORMAL', 'DISEASED').grid(row=5, column=1)

            yaa_show = tk.Label(self.root, text="Grandmother").grid(row=4, column=3)
            self.yaa = tk.StringVar(self.root)
            self.yaa.set('NORMAL')
            yaa_type = tk.OptionMenu(self.root, self.yaa, 'NORMAL', 'DISEASED').grid(row=5, column=3)

            taa_show = tk.Label(self.root, text="Grandfather").grid(row=10, column=1)
            self.taa = tk.StringVar(self.root)
            self.taa.set('NORMAL')
            taa_type = tk.OptionMenu(self.root, self.taa, 'NORMAL', 'DISEASED').grid(row=11, column=1)

            yay_show = tk.Label(self.root, text="Grandmother").grid(row=10, column=3)
            self.yay = tk.StringVar(self.root)
            self.yay.set('NORMAL')
            yay_type = tk.OptionMenu(self.root, self.yay, 'NORMAL', 'DISEASED').grid(row=11, column=3)

            dad_show = tk.Label(self.root, text="Father").grid(row=7, column=2)
            self.dad = tk.StringVar(self.root)
            self.dad.set('NORMAL')
            dad_type = tk.OptionMenu(self.root, self.dad, 'NORMAL', 'DISEASED').grid(row=8, column=2)

            mom_show = tk.Label(self.root, text="Mother").grid(row=12, column=2)
            self.mom = tk.StringVar(self.root)
            self.mom.set('NORMAL')
            mom_type = tk.OptionMenu(self.root, self.mom, 'NORMAL', 'DISEASED').grid(row=13, column=2)
    
        image = Image.open('processbutton.png')
        process_image = ImageTk.PhotoImage(image)
        process_button = tk.Button(self.root,command=self.bus,image=process_image,border=2).grid(row=14, column=2)
        process_button.place()
        
    def bus(self):
        st = {'DISEASED':'D', 'NORMAL':'N', 'CARRIER':'C'}
        poo, yaa, dad = st[self.poo.get()], st[self.yaa.get()], st[self.dad.get()]
        taa, yay, mom = st[self.taa.get()], st[self.yay.get()], st[self.mom.get()]
        if self.code == 'AR':
            autosomerecessive(self.root, poo, yaa, taa, yay, dad, mom, self.code, self.name)
        elif self.code == 'AD':
            autosomedominant(self.root, poo, yaa, taa, yay, dad, mom, self.code, self.name)
        elif self.code == 'XL':
            xlink(self.root, poo, yaa, taa, yay, dad, mom, self.code, self.name)

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
        #edit error
        self.root.geometry("430x430+300+300")
        image = Image.open('win1.jpg')
        tkimage = ImageTk.PhotoImage(image)
        bg = tk.Label(self.root, image = tkimage)
        bg.place(x=0, y=0, relwidth=1, relheight=1)
        
        head = Print(self.root, self.name, row=0, column=0)
    
        yourbaby = Print(self.root, self.predict(), row=1, column=0)

        image = Image.open('backbutton.png')
        back_image = ImageTk.PhotoImage(image)
        back_button = tk.Button(self.root,command=self.back,image=back_image,border=2).grid(row=2, column=0)
        back_button.place()

    def predict(self, per=25):
        if self.code == 'AR':
            didic = {'aa':self.name+' Diseased', 'Aa':self.name+' Carrier', 'AA':' Normal'}
        elif self.code == 'AD':
            didic = {'aa':' Normal', 'Aa':self.name+' Diseased(hetero)', 'AA':self.name+' Diseased(homo)'}

        elif self.code == 'XL':
            didic= {'Yx':self.name +' Diseased Son', 'XY':' Normal Son',
                    'XX':' Normal Daughter', 'Xx':self.name +' Normal(carrier) Daughter',
                    'xx':self.name +' Diseased Daughter'}
            per = 50
        string = "your baby's gene is \n"
        for item in self.baby:
            string += didic[item] + '     ' + str(self.baby[item] * per) + '%' + '\n'
        string += '***it only probability***'
        return string

    def back(self):
        self.root.destroy()
        self.root = tk.Tk()
        app = App()
        
def bloodtype():
    root.destroy()
    win1 = tk.Tk()
    win1.title('Blood Type')
    win1.geometry("430x430+300+300")
    image = Image.open('win1.jpg')
    tkimage = ImageTk.PhotoImage(image)
    bg = tk.Label(win1, image = tkimage)
    bg.place(x=0, y=0, relwidth=1, relheight=1)
    
    global mom, dad
    
    mom_text = tk.Label(win1, text='Mother Blood Type: ').grid(row=0, column=0)
    mom = tk.StringVar(win1)
    mom.set('A')
    mom_type = tk.OptionMenu(win1, mom, 'A', 'B', 'AB', 'O').grid(row=0, column=1)

    dad_text = tk.Label(win1, text='Father Blood Type: ').grid(row=2, column=0)  
    dad = tk.StringVar(win1)
    dad.set('A')
    dad_type = tk.OptionMenu(win1, dad, 'A', 'B', 'AB', 'O').grid(row=2, column=1)
    
    image = Image.open('processbutton.png')
    process_image = ImageTk.PhotoImage(image)
    process_button = tk.Button(win1,command=process,image=process_image,border=0).grid(row=3, column=1)
    process_button.place()
    
def process():
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

def cross(male, female, code, re):
    if code == 'AR':
        gtab = {'D':'aa', 'C':'Aa', 'N': 'AA'}
    elif code == 'AD':
        gtab = {'N':'aa', 'D': 'AA', 'C':'Aa'}
    elif code == 'XL':
        gtabmale = {'N':'XY', 'D':'Yx'}
        gtabfemale = {'N':'XX', 'C':'Xx', 'D':'xx'}
    genotype = dict()
    if code == 'XL':
        male, female = gtabmale[male], gtabfemale[female]
    else:
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
    elif code == 'AD':
        if re == 'check':
            if 'AA' in genotype:
                return 'D'
            else:
                return 'C'
        else:
            return genotype
    elif code == 'XL':
        if re == 'check':
            if 'Xx' in genotype:
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
    if dad == 'D':
        dad = cross(poo, yaa, code, 'check')
    print dad
    if mom == 'D':
        mom = cross(taa, yay, code, 'check')
    print mom
    baby = cross(dad, mom, code, 'baby')
    print_result = Result(root, baby, name, code)

def xlink(root, poo, yaa, taa, yay, dad, mom, code, name):
    print poo, yaa, taa, yay, dad, mom, code
    if mom == 'N':
        mom = cross(taa, yay, code, 'check')
    print dad
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

def albinism():
    albinism = Family(root, 'Albinism', 'AR')

#Autosome Dominant Disease
def acondroplasia():
    acon = Family(root, 'Acondroplasia', 'AD')

def marfansd():
    marfan = Family(root, 'Marfan Syndrome', 'AD')

def neurofibro():
    neuro = Family(root, 'Neurofibromatosis', 'AD')

def huntingron():
    hunti = Family(root, "Huntingron's chorea", 'AD')

def osteogenesis():
    osteo = Family(root, 'Osteogenesis imperfecta(OI)', 'AD')

def peutzsd():
    peut = (root, 'Peutz syndrome', 'AD')

#X-linked recessive
def colorblindness():
    color = Family(root, 'Color Blindness', 'XL')

def hemophilia():
    hemo = Family(root, 'Hemophilia', 'XL')

def g6pd():
    g6pd = Family(root, 'G-6-PD deficieccy', 'XL')

def duchenne():
    duch = Family(root, "Duchenne's muscular dystrophy", 'XL')

def hypohidro():
    hypo = Family(root, "Hypohidrotic ectodermal dysplasia", 'XL')

root = tk.Tk()
root.geometry("430x600+300+300")
image = Image.open('bg.jpg')
tkimage = ImageTk.PhotoImage(image)
bg = tk.Label(root, image = tkimage)
bg.place(x=0, y=0, relwidth=1, relheight=1)

class App():
    def __init__(self):
        self.root = root
        self.main()
    def main(self):
        '''screen'''
        bloodgroup = Built_Button(self.root, 'Blood Type', 'bloodtype', row=1, column=7)
        
        ar = tk.Label(self.root, text='AUTOSOME RECESSIVE').grid(row=2, column=7)
        thalassemia = Built_Button(self.root, 'Thalassemia', 'thalassemia', row=3, column=7)
        galac = Built_Button(self.root, 'Galactosemia', 'galactosemia', row=4, column=7)
        cystic = Built_Button(self.root, 'Cystic Fibrosis', 'cysticfibrosis', row=5, column=7)
        phenyl = Built_Button(self.root, 'Phenylketoneuria', 'phenylketoneuria', row=6, column=7)
        glyco = Built_Button(self.root, 'Glycogen Storage Disease', 'glycogen', row=7, column=7)
        albinism = Built_Button(self.root, 'Albinism', 'albinism', row=8, column=7)

        ad = tk.Label(self.root, text='AUTOSOME DOMINANT').grid(row=9, column=7)
        acon = Built_Button(self.root, 'Acondroplasia', 'acondroplasia', row=10, column=7)
        marfan = Built_Button(self.root, 'Marfan Syndrome', 'marfansd', row=11, column=7)
        neuro = Built_Button(self.root, 'Neurofibromatosis', 'neurofibro', row=12, column=7)
        hunti = Built_Button(self.root, "Huntingron's chorea", 'huntingron', row=13, column=7)
        osteo = Built_Button(self.root, 'Osteogenesis imperfecta(OI)', 'osteogenesis', row=14, column=7)
        peut = Built_Button(self.root, 'Peutz syndrome', 'peutzsd', row=15, column=7)
        
        xlink = tk.Label(self.root, text='X-LINKED RECESSIVE').grid(row=16, column=7)
        color = Built_Button(self.root, 'Color Blindness', 'colorblindness', row=17, column=7)
        hemo = Built_Button(self.root, 'Hemophilia', 'hemophilia', row=18, column=7)
        g6pd = Built_Button(self.root, 'G-6-PD deficieccy', 'g6pd', row=19, column=7)
        duch = Built_Button(self.root, "Duchenne's muscular dystrophy", 'duchenne', row=20, column=7)
        hypo = Built_Button(self.root, "Hypohidrotic ectodermal dysplasia", 'hypohidro', row=21, column=7)
root = App()
root.mainloop()

        
