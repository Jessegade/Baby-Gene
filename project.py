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

class Home(object):
    def __init__(self,root):
        self.root = root
        self.main()

    def main(self):
        self.root.geometry("430x650")
        image = Image.open('bg.jpg')
        tkimage = ImageTk.PhotoImage(image)
        bg = tk.Label(self.root, image = tkimage)
        bg.place(x=0, y=0, relwidth=1, relheight=1)
        bdg = semia = lambda : Family(self.root,'Blood Group', 'BD')
        bloodgroup = tk.Button(self.root, text='Blood Group', command=bdg).place(x=180,y=112)

        ar = tk.Label(self.root, text='AUTOSOME RECESSIVE').place(x=150,y=145)
        semia = lambda : Family(self.root,'Thalassemia', 'AR')
        thalas = tk.Button(self.root, text='Thalassemia', command=semia).place(x=177,y=165)
        tose = lambda : Family(self.root, 'Galactosemia', 'AR')
        galac = tk.Button(self.root, text='Galactosemia', command=tose).place(x=173,y=191)
        sis = lambda : Family(self.root, 'Cystic Fibrosis', 'AR')
        cystic = tk.Button(self.root, text='Cystic Fibrosis', command=sis).place(x=171,y=217)
        #phenyl = tk.Button(self.root, text='Phenylketoneuria', command=phenylketoneuria).place(x=163,y=243)
        #glyco = tk.Button(self.root, text='Glycogen Storage Disease', command=glycogen).place(x=144,y=269)
        alb = lambda : Family(self.root, 'Albinism', 'AR')
        albin = tk.Button(self.root, text='Albinism', command=alb).place(x=188,y=243)

        ad = tk.Label(self.root, text='AUTOSOME DOMINANT').place(x=150,y=276)
        asia = lambda : Family(self.root, 'Acondroplasia', 'AD')
        acon = tk.Button(self.root, text='Acondroplasia', command=asia).place(x=173,y=302)
        ome = lambda : Family(self.root, 'Marfan Syndrome', 'AD')
        marfan = tk.Button(self.root, text='Marfan Syndrome', command=ome).place(x=163,y=328)
        mato = lambda : Family(self.root, 'Neurofibromatosis', 'AD')
        neuro = tk.Button(self.root, text='Neurofibromatosis', command=mato).place(x=161,y=354)
        rea = lambda : Family(self.root, "Huntingron's chorea", 'AD')
        hunti = tk.Button(self.root, text="Huntingron's chorea", command=rea).place(x=156,y=380)
        #osteo = tk.Button(self.root, text='Osteogenesis imperfecta(OI)', command=osteogenesis).place(x=136,y=452)
        #peut = tk.Button(self.root, text='Peutz syndrome', command=peutzsd).place(x=170,y=478)
        
        xlink = tk.Label(self.root, text='X-LINKED RECESSIVE').place(x=160,y=413)
        ness = lambda : Family(self.root, 'Color Blindness', 'XL')
        color = tk.Button(self.root, text='Color Blindness', command=ness).place(x=172,y=439)
        lia = lambda : Family(self.root, 'Hemophilia', 'XL')
        hemo = tk.Button(self.root, text='Hemophilia', command=lia).place(x=180,y=465)
        pd = lambda : Family(self.root, 'G-6-PD deficieccy', 'XL')
        g6 = tk.Button(self.root, text='G-6-PD deficieccy', command=pd).place(x=166,y=491)
        nne = lambda : Family(self.root, "Duchenne's muscular dystrophy", 'XL')
        duch = tk.Button(self.root, text="Duchenne's muscular dystrophy", command=nne).place(x=126,y=517)
        dro = lambda : Family(self.root, "Hypohidrotic ectodermal dysplasia", 'XL')
        hypo = tk.Button(self.root, text="Hypohidrotic ectodermal dysplasia", command=dro).place(x=118,y=543)
        
        self.root.mainloop()
        
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
        #self.root.destroy()
        #self.root = tk.Tk()
        self.root.geometry("430x650")
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

        elif self.code == 'BD':
            poo_show = tk.Label(self.root, text="Grandfather").grid(row=4, column=1)
            self.poo = tk.StringVar(self.root)
            self.poo.set('A')
            poo_type = tk.OptionMenu(self.root, self.poo, 'A', 'B', 'AB', 'O').grid(row=5, column=1)

            yaa_show = tk.Label(self.root, text="Grandmother").grid(row=4, column=3)
            self.yaa = tk.StringVar(self.root)
            self.yaa.set('A')
            yaa_type = tk.OptionMenu(self.root, self.yaa, 'A', 'B', 'AB', 'O').grid(row=5, column=3)

            taa_show = tk.Label(self.root, text="Grandfather").grid(row=10, column=1)
            self.taa = tk.StringVar(self.root)
            self.taa.set('A')
            taa_type = tk.OptionMenu(self.root, self.taa, 'A', 'B', 'AB', 'O').grid(row=11, column=1)

            yay_show = tk.Label(self.root, text="Grandmother").grid(row=10, column=3)
            self.yay = tk.StringVar(self.root)
            self.yay.set('A')
            yay_type = tk.OptionMenu(self.root, self.yay, 'A', 'B', 'AB', 'O').grid(row=11, column=3)

            dad_show = tk.Label(self.root, text="Father").grid(row=7, column=2)
            self.dad = tk.StringVar(self.root)
            self.dad.set('A')
            dad_type = tk.OptionMenu(self.root, self.dad, 'A', 'B', 'AB', 'O').grid(row=8, column=2)

            mom_show = tk.Label(self.root, text="Mother").grid(row=12, column=2)
            self.mom = tk.StringVar(self.root)
            self.mom.set('A')
            mom_type = tk.OptionMenu(self.root, self.mom, 'A', 'B', 'AB', 'O').grid(row=13, column=2)
            
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

##        image = Image.open('processbutton.png')
##        process_image = ImageTk.PhotoImage(image)
##        process_button = tk.Button(win1,command=process,image=process_image,border=0).grid(row=3, column=1)
##        process_button.place()

    
        process_image = ImageTk.PhotoImage(Image.open('processbutton.png'))
        process_button = tk.Button(self.root,command=self.bus,image=process_image,border=2)#
        process_button.grid(row=14, column=2)
        process_button.place()
        self.root.mainloop()
        
    def bus(self):
        st = {'DISEASED':'D', 'NORMAL':'N', 'CARRIER':'C', 'A':'AA', 'B':'BB', 'AB':'AB', 'O':'ii'}
        self.poo, self.yaa, self.dad = st[self.poo.get()], st[self.yaa.get()], st[self.dad.get()]
        self.taa, self.yay, self.mom = st[self.taa.get()], st[self.yay.get()], st[self.mom.get()]
        if self.code == 'AR':
            self.autosomerecessive(self.root)
        elif self.code == 'AD':
            self.autosomedominant(self.root)
        elif self.code == 'XL':
            self.xlink(self.root)
        elif self.code == 'BD':
            self.blood(self.root)     

    def cross(self, male, female, code, re):
        if code == 'AR':
            gtab = {'D':'aa', 'C':'Aa', 'N': 'AA'}
        elif code == 'AD':
            gtab = {'N':'aa', 'D': 'AA', 'C':'Aa'}
        elif code == 'XL':
            gtabmale = {'N':'XY', 'D':'Yx'}
            gtabfemale = {'N':'XX', 'C':'Xx', 'D':'xx'}
        elif code == 'BD':
            gtab = {'AA':'AA', 'Ai':'Ai', 'BB':'BB', 'Bi':'Bi', 'AB':'AB', 'ii':'ii'}
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
        elif code == 'BD':
            if re == 'check':
                if 'Ai' in genotype:
                    return 'Ai'
                elif 'Bi' in genotype:
                    return 'Bi'
                elif 'AA' or 'BB' in genotype:
                    return genotype.keys()[0]
            else:
                return genotype
    def blood(self, root):
        print self.poo, self.yaa, self.taa, self.yay, self.dad, self.mom, self.code
        if (self.dad == 'AA' and (self.poo != 'AB' and self.yaa != 'AB')) or \
            (self.dad == 'BB' and (self.poo != 'AB' and self.yaa != 'AB')):
            self.dad = self.cross(self.poo, self.yaa, self.code, 'check')
            
        print self.dad
        if (self.mom == 'AA' and (self.taa != 'AB' and self.yay != 'AB')) or \
            (self.mom == 'BB' and (self.taa != 'AB' and self.yay != 'AB')):
            self.mom =  self.cross(self.taa, self.yay, self.code, 'check')
        print self.mom
        baby = baby = self.cross(self.dad, self.mom, self.code, 'baby')
        print_result = Result(root, baby, self.name, self.code)
        
    def autosomerecessive(self, root):
        print self.poo, self.yaa, self.taa, self.yay, self.dad, self.mom, self.code
        if self.dad == 'N':
            self.dad = self.cross(self.poo, self.yaa, self.code, 'check')
            if self.dad == 'D':
                self.dad = 'C'
        print self.dad
        if self.mom == 'N':
            self.mom = self.cross(self.taa, self.yay, self.code, 'check')
            if self.mom == 'D':
                self.mom = 'C'
        print self.mom
        baby = self.cross(self.dad, self.mom, self.code, 'baby')
        print_result = Result(root, baby, self.name, self.code)

    def autosomedominant(self, root):
        print self.poo, self.yaa, self.taa, self.yay, self.dad, self.mom, self.code
        if self.dad == 'D':
            self.dad = self.cross(self.poo, self.yaa, self.code, 'check')
        print self.dad
        if self.mom == 'D':
            self.mom = self.cross(self.taa, self.yay, self.code, 'check')
        print self.mom
        baby = self.cross(self.dad, self.mom, self.code, 'baby')
        print_result = Result(root, baby, self.name, self.code)

    def xlink(self, root):
        print self.poo, self.yaa, self.taa, self.yay, self.dad, self.mom, self.code
        if self.mom == 'N':
            self.mom = self.cross(self.taa, self.yay, self.code, 'check')
        print self.dad
        print self.mom
        baby = self.cross(self.dad, self.mom, self.code, 'baby')
        print_result = Result(root, baby, self.name, self.code)

class Result(object):
    def __init__(self, root ,baby, name, code):
        self.root = root
        self.baby = baby
        self.name = name
        self.code = code
        self.print_gene()
    def print_gene(self):
##        self.root.destroy()
##        self.root = tk.Tk()
        #edit error
        self.root.geometry("430x650")
        image = Image.open('win1.jpg')
        tkimage = ImageTk.PhotoImage(image)
        bg = tk.Label(self.root, image = tkimage)
        bg.place(x=0, y=0, relwidth=1, relheight=1)
        
        head = tk.Label(self.root, text=self.name.upper()).grid(row=0, column=0)
    
        yourbaby = tk.Label(self.root, text=self.predict()).grid(row=1, column=0)

        image = Image.open('backbutton.png')
        back_image = ImageTk.PhotoImage(image)
        back_button = tk.Button(self.root,command=self.back,image=back_image,border=2)
        
        back_button.grid(row=2, column=0)
        back_button.place()
        self.root.mainloop()
    def predict(self):
        if self.code == 'AR':
            didic = {'aa':self.name+' Diseased', 'Aa':self.name+' Carrier', 'AA':' Normal'}
        elif self.code == 'AD':
            didic = {'aa':' Normal', 'Aa':self.name+' Diseased(hetero)', 'AA':self.name+' Diseased(homo)'}
        elif self.code == 'XL':
            didic = {'Yx':self.name +' Diseased Son', 'XY':' Normal Son',
                    'XX':' Normal Daughter', 'Xx':' Normal(carrier) Daughter',
                    'xx':self.name +' Diseased Daughter'}
        elif self.code == 'BD':
            didic = {'AA':'A Homozygous(pure)', 'Ai':'A Heterozygous(hybrid)',
                     'BB':'B Homozygous(pure)', 'Bi':'B Heterozygous(hybrid)',
                     'AB':'AB Homozygous(pure)', 'ii':'O Homozygous(pure)'}
        string = "\nyour baby's gene is \n\n"
        if self.code == 'XL':
            son, daughter = list(), list()
            for item in self.baby:
                if 'Y' in item:
                    son.append(item)
                else:
                    daughter.append(item)
            string += 'SON\n'
            for item in son:
                string += didic[item] + '     ' + str(self.baby[item] * 50) + '%' + '\n'
            string += '\n\nDAUGHTER\n'
            for item in daughter:
                string += didic[item] + '     ' + str(self.baby[item] * 50) + '%' + '\n'
            return string
        else:
            for item in self.baby:
                string += didic[item] + '     ' + str(self.baby[item] * 25) + '%' + '\n'
        string += '***it only probability***'
        return string

    def back(self):
        #self.root.destroy()
        app = Home(self.root)
        
def bloodtype():
    root.destroy()
    win1 = tk.Tk()
    win1.title('Blood Type')
    win1.geometry("430x650")
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
    ############
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
    
root = tk.Tk()
root.title("Baby Gene")
app = Home(root)
root.mainloop()
