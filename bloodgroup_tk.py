import Tkinter as tk

class Print(object):
    '''
    input
    Print(text, row, column)
    '''
    def __init__(self, root, text, row, column):
        self.text = text
        self.message = tk.Message(root, text=text)
        self.message.grid(row=row, column=column)

class Built_Button(object):
    '''
    input
    Built_Button(text, value, row, column)
    '''
    def __init__(self, root, text, value, row, column):
        self.root = root
        dic = {'bloodgroup':self.bloodgroup, 'thalassemia':self.thalassemia}
        if value in dic:
            self.value = dic[value]
            self.button = tk.Button(self.root, text=text, command=self.value)
        else:
            self.value = value
            self.button = tk.Button(self.root, text=text)
        self.button.grid(row=row, column=column)
##    
##    def bloodgroup(self):
##        self.root.destroy()
##        self.root = tk.Tk()
##        papa_a = Built_Button(self.root, 'A', 'A', row=2, column=1)
##        self.root = Bloodgroup(self.root, 'A', 'B')
##        print 'pass1'
##
##    def thalassemia(self):
##        print 'pass2'
##
##class Bloodgroup(object):
##    '''input
##        Bloodgroup()
##    '''
##    def __init__(self, root, dad, mom):
##        self.root = root
##        self.dad = dad
##        self.mom = mom
##        self.baby_blood()
##        
##    def baby_blood(self):
##        
##        head = Print(self.root, 'GG', 1, 1)
    
def main():
    '''screen'''
    welcome = Print(root, 'BABY GENE', row=0, column=1)
    bloodgroup = Built_Button(root, 'Blood Group', 'bloodgroup', row=1, column=1)
    thalassemia = Built_Button(root, 'Thalassemia', 'thalassemia', 2, 1)

root = tk.Tk()

main()

root.mainloop()
