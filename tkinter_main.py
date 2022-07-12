from cProfile import label
from dataclasses import field
from email.mime import image
from tkinter import *


from db_estoque import *


from setuptools import Command
from img import *
import posiciona

entrywhite = '#F4F4F4'


Estq = Db_estoque()


def saveEmp():
    f2.forget()
    f1.pack()


def saveProd():
    f3.forget()
    f1.pack()
    


def cadProd():
    f1.forget()
    f3.pack()


def cadEmp():
    f1.forget()
    f2.pack()


def buySell():
    f1.forget()
    f4.pack()

def returnMenu():
    f4.forget()
    f1.pack()


def view():
    f1.forget()
    f5.pack()

def returnview():
    f5.forget()
    f1.pack()

def search():
    Estq = Db_estoque()
    a = searchCode.get()
    unityinfo['text'] = Estq.listar_unidade(a)
    #unityinfo['text'] = Estq.listar_unidade.i



entrycolor = '#0E0D0D'

app = Tk()
app.geometry('700x700+350+150')
app.resizable(width=False, height=False)
app.title('Banco sem nome...')
app.configure(bg='black')



#========================= -= = ==========- =-=--= -==========------

app.bind('<Button-1>', posiciona.inicio_place)
app.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, app))
app.bind('<Button-2>', lambda arg: posiciona.para_geometry(app))



#====== = = -------------======================= = == ===================
#+=================  MENU PRINCIPAL  -------------=======================
#-------------======================= -------------======================

f1 = Frame(app)
f1.pack()
f2 = Frame(app)
f3 = Frame(app)
f4 = Frame(app)
f5 = Frame(app)

#====== = = -------------======================= = == ===================
#+=================  FRAME 1  -------------=======================
#-------------======================= -------------======================

backg1 = PhotoImage(file = 'img/principal.png')
btemp1 = PhotoImage(file= 'img/btEmp.png')
btprod1 = PhotoImage(file='img/btProd.png')
btmain = PhotoImage(file='img/menu_bt.png')

bthistory = PhotoImage(file='img/historybt.png')
btview = PhotoImage(file='img/viewbt.png')



back = Label(f1,image = backg1)

back.pack()


BTemp = Button(f1,image = btemp1,command=cadEmp)
BTemp.place(width=224, height=222, x=42, y=408)


BTprod = Button(f1,image = btprod1,command=cadProd)
BTprod.place(width=224, height=220, x=432, y=407)


history = Button(f1,image=bthistory,bd=0,activebackground='black')
history.place(width=44, height=46, x=645, y=5)



view = Button(f1,image=btview,bd=0,command=view)
view.place(width=51, height=46, x=579, y=5)



bt_main = Button(f1,image = btmain,bd=0,command=buySell)
bt_main.place(width=61, height=64, x=317, y=483)

#====     == = = -------------======================= = == ===================
#+=================  FRAME 2  -------------=======================
#-------------======================= -------------======================



back2 = PhotoImage (file='img/empresa_cad.png')


backg2 = Label(f2,image=back2)


empEntry = Entry(f2,foreground='white',background=entrycolor,font='Arial 40',justify=CENTER,bd=0)
empEntry.place(width=474, height=90, x=116, y=148)

backg2.pack()

saveBYT = Button(f2,image=btmain,bd=0,command=saveEmp)
saveBYT.place(width=68, height=65, x=315, y=317)

#====     == = = -------------======================= = == ===================
#+=================  FRAME 3  -------------=======================
#-------------======================= -------------======================



back3 = PhotoImage(file='img/cad_prod.png')


backg3 = Label(f3,image=back3)
backg3.pack()

BTprod = Button(f3,image=btmain,bd=0,command=saveProd)
BTprod.place(width=64, height=57, x=321, y=641)

entrynom = Entry(f3,foreground='white',background=entrycolor,bd=0,justify=CENTER,font='Arial 25')
entrynom.place(width=290, height=42, x=198, y=346)

entryEmp = Entry(f3,foreground='white',background=entrycolor,bd=0,justify=CENTER,font='Arial 25')
entryEmp.place(width=290, height=38, x=199, y=492)



#====     == = = -------------======================= = == ===================
#+=================  FRAME 4  -------------=======================
#-------------======================= -------------======================



back4 = PhotoImage(file='img/buysell.png')

backg4 = Label (f4,image=back4)
backg4.pack()


main_bt = Button(f4,image = btmain,bd=0,command=returnMenu)
main_bt.place(width=66, height=61, x=313, y=628)



#====     == = = -------------======================= = == ===================
#+=================  FRAME 5  -------------=======================
#-------------======================= -------------======================



back5 = PhotoImage(file='img/unityView.png')
buttonsea = PhotoImage(file='img/search.png')


backg5 = Label (f5,image=back5)
backg5.pack()

#Copiado! .place(width=71, height=65, x=316, y=629)
returnUnity  = Button(f5,image=btmain,bd=0,activebackground='black',command=returnview)
returnUnity.place(width=71, height=65, x=316, y=629)


searchCode = Entry(f5,bd=0,foreground='black',background=entrywhite,font='Arial 25',justify=CENTER)
searchCode.place(width=358, height=41, x=141, y=183)


searchButton = Button(f5,image=buttonsea,bd=0,command=search)
searchButton.place(width=26, height=26, x=517, y=190)

unityinfo = Label(f5,background='black',foreground=entrywhite,font='Arial 12',text=f'')
unityinfo.place(width=260, height=253, x=218, y=292)











app.mainloop()