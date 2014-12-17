'''
Baby Gene
PSIT Project
By Tharathip Malaimarn(57070054)
    Pawarisa Thong-ngoen(57070068)
This Program show you about
- probability of gene's your baby
--Blood Group
--Genetic Diseases
************it only probability************
'''

import Tkinter as tk
from PIL import ImageTk, Image
import tkMessageBox

class Home(object):
    '''main window'''
    def __init__(self,root):
        self.root = root
        self.main()

    def main(self):
        self.root.geometry("430x650")
        self.root.resizable(width='false', height='false')
        self.root.title('Baby Gene')
        image = Image.open('bg.jpg')
        tkimage = ImageTk.PhotoImage(image)
        bg = tk.Label(self.root, image = tkimage)
        bg.place(x=0, y=0, relwidth=1, relheight=1)
        bdg = lambda : Family(self.root,'Blood Group', 'BD')
        bloodgroup = tk.Button(self.root, text='Blood Group', command=bdg, bg='white').place(x=180, y=112)

        ar = tk.Label(self.root, text='AUTOSOME RECESSIVE').place(x=150, y=145)
        semia = lambda : Family(self.root,'Thalassemia', 'AR')
        thalas = tk.Button(self.root, text='Thalassemia', command=semia, bg='white').place(x=177, y=165)
        tose = lambda : Family(self.root, 'Galactosemia', 'AR')
        galac = tk.Button(self.root, text='Galactosemia', command=tose, bg='white').place(x=173, y=191)
        sis = lambda : Family(self.root, 'Cystic Fibrosis', 'AR')
        cystic = tk.Button(self.root, text='Cystic Fibrosis', command=sis, bg='white').place(x=171, y=217)
        alb = lambda : Family(self.root, 'Albinism', 'AR')
        albin = tk.Button(self.root, text='Albinism', command=alb, bg='white').place(x=185, y=243)

        ad = tk.Label(self.root, text='AUTOSOME DOMINANT').place(x=150, y=280)
        asia = lambda : Family(self.root, 'Achondroplasia', 'AD')
        acon = tk.Button(self.root, text='Achondroplasia', command=asia, bg='white').place(x=173, y=302)
        ome = lambda : Family(self.root, 'Marfan Syndrome', 'AD')
        marfan = tk.Button(self.root, text='Marfan Syndrome', command=ome, bg='white').place(x=163, y=328)
        mato = lambda : Family(self.root, 'Neurofibromatosis', 'AD')
        neuro = tk.Button(self.root, text='Neurofibromatosis', command=mato, bg='white').place(x=161, y=354)
        rea = lambda : Family(self.root, "Huntingron's chorea", 'AD')
        hunti = tk.Button(self.root, text="Huntingron's chorea", command=rea, bg='white').place(x=156, y=380)
        
        xlink = tk.Label(self.root, text='X-LINKED RECESSIVE').place(x=160, y=417)
        ness = lambda : Family(self.root, 'Color Blindness', 'XL')
        color = tk.Button(self.root, text='Color Blindness', command=ness, bg='white').place(x=172, y=439)
        lia = lambda : Family(self.root, 'Hemophilia', 'XL')
        hemo = tk.Button(self.root, text='Hemophilia', command=lia, bg='white').place(x=180, y=465)
        pd = lambda : Family(self.root, 'G-6-PD deficiency', 'XL')
        g6 = tk.Button(self.root, text='G-6-PD deficiency', command=pd, bg='white').place(x=166, y=491)
        nne = lambda : Family(self.root, "Duchenne's muscular dystrophy", 'XL')
        duch = tk.Button(self.root, text="Duchenne's muscular dystrophy", command=nne, bg='white').place(x=126, y=517)
        dro = lambda : Family(self.root, "Hypohidrotic ectodermal dysplasia", 'XL')
        hypo = tk.Button(self.root, text="Hypohidrotic ectodermal dysplasia", command=dro, bg='white').place(x=118, y=543)
        
        quit_image = ImageTk.PhotoImage(Image.open('quitbutton.png'))
        quit_button = tk.Button(self.root,command=self.end,image=quit_image,border=0,highlightthickness=0)
        quit_button.place(x=170, y=600)

        self.root.mainloop()

    def end(self):
        self.root.destroy()
        
class Family(object):
    '''
    Pedigree of family and Genetic inheritance
    '''
    def __init__(self, root, name, code):
        self.keep = dict()
        self.name = name
        self.root = root
        self.code = code
        self.poo = tk.StringVar(self.root)
        self.yaa = tk.StringVar(self.root)
        self.taa = tk.StringVar(self.root)
        self.yay = tk.StringVar(self.root)
        self.dad = tk.StringVar(self.root)
        self.mom = tk.StringVar(self.root)
        self.tree()

    def choice(self, lst, status):
        fatherfam =  tk.Label(self.root, text="-----------Father's Family-----------").place(relx=0.5, rely=0.42, anchor='center')
        motherfam =  tk.Label(self.root, text="-----------Mother's Family-----------").place(relx=0.5, rely=0.63, anchor='center')
        
        pooshow = tk.Label(self.root, text='Grandfather(Father)').place(x=54, y=280)
        self.poo.set(status)
        poo_type = tk.OptionMenu(self.root, self.poo, *lst)
        poo_type.config(bg='white')
        poo_type.place(x=60, y=300)

        yaashow = tk.Label(self.root, text='Grandmother(Father)').place(x=259, y=280)
        self.yaa.set(status)
        yaa_type = tk.OptionMenu(self.root, self.yaa, *lst)
        yaa_type.config(bg='white')
        yaa_type.place(x=270, y=300)

        taashow = tk.Label(self.root, text='Grandfather(Mother)').place(x=54, y=430)
        self.taa.set(status)
        taa_type = tk.OptionMenu(self.root, self.taa, *lst)
        taa_type.config(bg='white')
        taa_type.place(x=60, y=450)

        yayshow = tk.Label(self.root, text='Grandmother(Mother)').place(x=259, y=430)
        self.yay.set(status)
        yay_type = tk.OptionMenu(self.root, self.yay, *lst)
        yay_type.config(bg='white')
        yay_type.place(x=270, y=450)

        dadshow = tk.Label(self.root, text='Father').place(x=194, y=330)
        self.dad.set(status)
        dad_type = tk.OptionMenu(self.root, self.dad, *lst)
        dad_type.config(bg='white')
        dad_type.place(x=169, y=350)

        momshow = tk.Label(self.root, text='Mother').place(x=190, y=470)
        self.mom.set(status)
        mom_type = tk.OptionMenu(self.root, self.mom, *lst)
        mom_type.config(bg='white')
        mom_type.place(x=165, y=500)

    def tree(self):
        self.root.geometry("430x650")
        self.root.resizable(width='false', height='false')
        image = Image.open('win1.jpg')
        tkimage = ImageTk.PhotoImage(image)
        bg = tk.Label(self.root, image = tkimage)
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        diseasedname = tk.Label(self.root, text=self.name.upper()).place(relx=0.5, rely=0.03, anchor='center')

        self.head = tk.Label(self.root, text=self.name.upper()).place(relx=0.5, rely=0.03, anchor='center')
        picdisease = {'Thalassemia':"thalassemia.png", 'Galactosemia':"galac.png",
                      'Cystic Fibrosis':"cystic.png", 'Albinism':"albinism.png",
                      'Achondroplasia':"achondro.png", 'Marfan Syndrome':"marfan.png",
                      'Neurofibromatosis':"neuro.png", "Huntingron's chorea":"hunting.png",
                      'Color Blindness':"color.png", 'Hemophilia':"hemophilia.png",
                      'G-6-PD deficiency':"g6pd.png", "Duchenne's muscular dystrophy":"duchen.png",
                      "Hypohidrotic ectodermal dysplasia":"hypo.png", "Blood Group":"blood.jpg"}
        imagee = Image.open(picdisease[self.name])
        photo = ImageTk.PhotoImage(imagee)
        label = tk.Label(image=photo)
        label.image = photo 
        label.place(x=20, y=50)
        
        global poo, yaa, taa, yay, dad, mom

        if self.code == 'AR':
            status = 'NORMAL'
            lst = ['NORMAL', 'DISEASED', 'CARRIER']
        elif self.code == 'AD' or self.code == 'XL':
            status = 'NORMAL'
            lst = ['NORMAL', 'DISEASED']
        else:
            status = 'O'
            lst = ['O', 'A', 'B', 'AB']
            
        way = self.choice(lst, status)
     
        process_image = ImageTk.PhotoImage(Image.open('processbutton.png'))
        process_button = tk.Button(self.root,command=self.bus,image=process_image,border=0,highlightthickness=0)
        process_button.place(x=140, y=550)
        self.root.mainloop()
        
    def bus(self):
        st = {'DISEASED':'D', 'NORMAL':'N', 'CARRIER':'C', 'A':['AA','AO'], 'B':['BB', 'BO'],
              'AB':['AB'], 'O':['OO']}
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

    def cross(self, male, female, code):
        genotype = dict()
        male, female = male, female
        for s in male:
            for e in female:
                geno = [s, e]
                geno.sort()
                geno = geno[0] + geno[1]
                if geno in genotype:
                    genotype[geno] += 1
                else:
                    genotype[geno] = 1
        else:
            return genotype

    def testloop(self, test, comp):
        pool = dict()
        for i in test:
            if i in comp:
                if i in pool:
                    pool[i] += 1
                else:
                    pool[i] = 1
        print 'pool', pool.keys()
        return pool.keys()

    def allcase(self, alldad, allmom, code, re):
        sumcross = []
        for i in alldad:
            for j in allmom:
                if re == 'P':
                    sumcross.extend(self.cross(i, j, code).keys())
                else:
                    sumcross.append([[i, j], self.cross(i, j, code)])
        print 'sumcross', sumcross
        return sumcross
            
    def blood(self, root):
        print 'input', self.poo, self.yaa, self.dad, self.taa, self.yay, self.mom, self.code
        if self.dad == 'AB' or self.dad == 'OO' :
            self.alldad = self.dad
        else:
            self.alldad = self.allcase(self.poo, self.yaa, self.code, 'P')
            self.alldad = self.testloop(self.alldad, self.dad)
        print 'self.alldad', self.alldad 
        if self.mom == 'AB' or self.mom == 'OO':
            self.allmom = self.mom
        else:
            self.allmom =  self.allcase(self.taa, self.yay, self.code, 'P')
            self.allmom = self.testloop(self.allmom, self.mom)
        print 'self.allmom', self.allmom
        baby = self.allcase(self.alldad, self.allmom, self.code, 'B')
        print 'baby', baby
        print_result = Result(root, baby, self.name, self.code)
           
    def autosomerecessive(self, root):
        tran = {'D':['aa'], 'N':['AA', 'Aa'], 'C':['Aa']}
        self.poo, self.yaa, self.dad = tran[self.poo], tran[self.yaa], tran[self.dad]
        self.taa, self.yay, self.mom = tran[self.taa], tran[self.yay], tran[self.mom]
        print 'input', self.poo, self.yaa, self.dad, self.taa, self.yay, self.mom, self.code
        if self.dad == 'aa':
            self.alldad = self.dad
        else:
            self.alldad = self.allcase(self.poo, self.yaa, self.code, 'P')
            self.alldad = self.testloop(self.alldad, self.dad)
        print 'self.alldad', self.alldad
        if self.mom == 'aa':
            self.allmom = self.mom
        else:
            self.allmom = self.allcase(self.taa, self.yay, self.code, 'P')
            self.allmom = self.testloop(self.allmom, self.mom)
        print 'self.allmom', self.allmom
        baby = self.allcase(self.alldad, self.allmom, self.code, 'B')
        print 'baby', baby
        print_result = Result(root, baby, self.name, self.code)

    def autosomedominant(self, root):
        tran = {'D':['AA', 'Aa'], 'N':['aa']}
        self.poo, self.yaa, self.dad = tran[self.poo], tran[self.yaa], tran[self.dad]
        self.taa, self.yay, self.mom = tran[self.taa], tran[self.yay], tran[self.mom]
        print 'input', self.poo, self.yaa, self.dad, self.taa, self.yay, self.mom, self.code
        if self.dad == 'aa':
            self.alldad = self.dad
        else:
            self.alldad = self.allcase(self.poo, self.yaa, self.code, 'P')
            self.alldad = self.testloop(self.alldad, self.dad)
        print 'self.alldad', self.alldad
        if self.mom == 'aa':
            self.allmom = self.mom
        else:
            self.allmom = self.allcase(self.taa, self.yay, self.code, 'P')
            self.allmom = self.testloop(self.allmom, self.mom)
        print 'self.allmom', self.allmom
        baby = self.allcase(self.alldad, self.allmom, self.code, 'B')
        print 'baby', baby
        print_result = Result(root, baby, self.name, self.code)

    def xlink(self, root):
        tran_m = {'N':['XY'], 'D':['Yx']}
        tran_w = {'N':['XX', 'Xx'], 'D':['xx']}
        self.poo, self.yaa, self.dad = tran_m[self.poo], tran_w[self.yaa], tran_m[self.dad]
        self.taa, self.yay, self.mom = tran_m[self.taa], tran_w[self.yay], tran_w[self.mom]
        print 'input', self.poo, self.yaa, self.dad, self.taa, self.yay, self.mom, self.code
        self.alldad = self.dad
        print 'self.alldad', self.alldad
        if self.mom == 'xx':
            self.allmom = self.mom
        else:
            self.allmom = self.allcase(self.taa, self.yay, self.code, 'P')
            self.allmom = self.testloop(self.allmom, self.mom)
        print 'self.allmom', self.allmom
        baby = self.allcase(self.alldad, self.allmom, self.code, 'B')
        print 'baby', baby
        print_result = Result(root, baby, self.name, self.code)

class Result(object):
    def __init__(self, root ,baby, name, code):
        self.root = root
        self.baby = baby
        self.name = name
        self.code = code
        self.print_gene()
    def print_gene(self):

        self.root.geometry("430x650")
        self.root.resizable(width='false', height='false')
        image = Image.open('win1.jpg')
        tkimage = ImageTk.PhotoImage(image)
        bg = tk.Label(self.root, image = tkimage)
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        yourbaby = tk.Label(self.root, text=self.printallcase()).place(relx=0.5, rely=0.45, anchor='center')

        image = Image.open('backbutton.png')
        back_image = ImageTk.PhotoImage(image)
        back_button = tk.Button(self.root,command=self.back,image=back_image,border=0,highlightthickness=0)
        
        back_button.place(x=160,y=600)
        self.root.mainloop()

    def printallcase(self):
        if len(self.baby) == 0:
            data =  '********************  Your PEDIGREE is invalid  ********************\n\n'
            data += 'Please check your Pedigree again :=]'
            return data
        data = '====================================================='+'\n' + self.name.upper() + \
               '\n' + '====================================================='+'\n\n'
        data += 'TOTAL CASE : ' + str(len(self.baby)) + '\n\n\n Your baby gene is \n\n'
        for i in xrange(len(self.baby)):
            data += '\n------------------------ CASE ' + str(i + 1) + ' ------------------------\n'
            data += self.predict(self.baby[i][0], self.baby[i][1])
        data += '\n***it only probability***'
        return data
    
    def predict(self, namecase, thiscase):
        if self.code == 'AR':
            didic = {'aa':' Diseased', 'Aa':' Carrier', 'AA':' Normal'}
        elif self.code == 'AD':
            didic = {'aa':' Normal', 'Aa':' Diseased(heterozygous)', 'AA':' Diseased(homozygous)'}
        elif self.code == 'XL':
            didic = {'Yx':' Diseased', 'XY':' Normal',
                    'XX':' Normal', 'Xx':' Normal(carrier)',
                    'xx':' Diseased Daughter'}
        elif self.code == 'BD':
            didic = {'AA':'A Homozygous(AA)', 'AO':'A Heterozygous(AO)',
                     'BB':'B Homozygous(BB)', 'BO':'B Heterozygous(BO)',
                     'AB':'AB Homozygous', 'OO':'O Homozygous'}
        string = '\nFather : ' + didic[namecase[0]] + '           Mother : ' + didic[namecase[1]] + '\n\n'
        if self.code == 'XL':
            son, daughter = list(), list()
            for item in thiscase:
                if 'Y' in item:
                    son.append(item)
                else:
                    daughter.append(item)
            string += 'SON\n'
            for item in son:
                string += didic[item] + '     ' + str(thiscase[item] * 50) + '%' + '\n'
            string += '\n\nDAUGHTER\n'
            for item in daughter:
                string += didic[item] + '     ' + str(thiscase[item] * 50) + '%' + '\n'
            return string
        else:
            for item in thiscase:
                string += didic[item] + '     ' + str(thiscase[item] * 25) + '%' + '\n'
        return string

    def back(self):
        self.name = ''
        app = Home(self.root)
            
root = tk.Tk()
app = Home(root)
root.mainloop()
