#!/usr/bin/python
# -*- coding: UTF-8 -*-

#instalar modulos nescessários:
# pip install PyAutocad

#importar Modulos
from pyautocad import Autocad, APoint
from tkinter import *

#executar função.
#para funcionamento correto o ideal é abrir o autocad antes do script e confirmar a inicialização pelo Pront de Comando.
acad = Autocad()
acad.prompt("Ferramenta de inserção de coordenadas iniciada\n")
print (acad.doc.Name)

#Configurações basicas
#----------------Cores------------------
mycolor = '#111116'
cor_fg ='#aed1e8'
botao_cor = '#a7ac93'

#inicio da janela do software
janela = Tk()
janela.title("Inserir pontos UTM")
janela.geometry("500x400")
janela["bg"]=mycolor
photo = PhotoImage(file ='icon/icon.png')#icone_do_programa
janela.iconphoto(False, photo)
#containers
#GERAL -----------#--------------#-----
containerprincipaljanela = Frame(janela)
containerprincipaljanela ["padx"] =20
containerprincipaljanela ["pady"] =20
containerprincipaljanela ["bg"]=mycolor
containerprincipaljanela.pack()

#container #01-------------------------------
container01 = Frame(containerprincipaljanela)
container01["bg"]=mycolor
container01.pack()

container00 = Frame(container01)
container00["padx"]=5
container00["pady"]=5
container00["bg"]=mycolor
container00.pack()

titulo = Label(container00, font= 'Arial 14 bold',text = 'DIGITAR COORDENADAS UTM NO AUTOCAD', fg =cor_fg, bg = mycolor)
titulo.pack()

container02 = Frame(container01)
container02["padx"]=10
container02["pady"]=10
container02["bg"]=mycolor
container02.pack()

container03 = Frame(container01)
container03["padx"]=10
container03["pady"]=10
container03["bg"]=mycolor
container03.pack()

container04 = Frame(container01)
container04["padx"]=10
container04["pady"]=10
container04["bg"]=mycolor
container04.pack()

container05 = Frame(container01)
container05["padx"]=15
container05["pady"]=15
container05["bg"]=mycolor
container05.pack()

container06 = Frame(container01)
container06["padx"]=15
container06["pady"]=15
container06["bg"]=mycolor
container06.pack()

def bt01_click():
    x = ent02.get()
    x = x.replace(" ","")
    x = x.replace(",",".")
    xn = float(x)
    y = ent03.get()
    y = y.replace(" ","")
    y = y.replace(",",".")
    yn =float(y)
    name01 = ent01.get()
    name01 = name01.replace(" ","")
    name01 = name01.upper()
    name = (name01 + " ")
    lb04["text"]=('Coordenada anterior:\n   '+name01+'    X: '+x+'    Y: '+y)
    lb04["fg"]='Green'
    p1 = APoint(xn, yn)
    p2 = APoint(1)
    for i in range(1):
        text = acad.model.AddText('%s' % name, p1, 2.5)
        acad.model.AddCircle(p1, 10)

    for text in acad.iter_objects('Text'):
        print('text: %s at: %s' % (text.TextString, text.InsertionPoint))
        text.InsertionPoint = APoint(text.InsertionPoint)
    ent02.delete(0, END)
    ent03.delete(0, END)
    ent01.delete(0, END)

#interfaces - Left --------------#-------------------------#------------------------------
lb01 = Label(container02,width=15, font= 'Arial 12',text = 'Descrição:    ', fg =cor_fg, bg = mycolor)
lb01.pack(side=LEFT)
ent01 = Entry(container02,width=25)
ent01.pack(side=LEFT)
lb02 = Label(container03, width=15,font= 'Arial 12',text = 'Coordenada X:', fg =cor_fg, bg = mycolor)
lb02.pack(side=LEFT)
ent02 = Entry(container03,width=25)
ent02.pack(side=LEFT)
lb03 = Label(container04,width=15, font= 'Arial 12',text = 'Coordenada Y:', fg =cor_fg, bg = mycolor)
lb03.pack(side=LEFT)
ent03 = Entry(container04,width=25)
ent03.pack(side=LEFT)
#---------------botões-------------------
bt01 = Button(container05, width=15, height=1, font='Arial 10 bold', bg =botao_cor, fg='black', text='Inserir', command=bt01_click)
bt01.pack()
bt01.focus_force()
bt01.bind("<Return>", bt01_click)

lb04 = Label(container06, font= 'Arial 12',text = 'Sem coordenadas anteriores!', fg = 'red', bg = mycolor)
lb04.pack()

mainloop()
