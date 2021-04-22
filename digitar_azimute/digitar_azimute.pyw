#   MODULOS
#banco de dados
import sqlite3
#interface
from tkinter import *
#trabalhar com arquivos na interface
from tkinter import filedialog
#mensagem alerta
import tkinter.messagebox as messagebox
import os
#-----------------Carregar configurações do software-------#
#---------------configurações de cores-------------------#
cor_bg ='#111116'
cor_fg ='#aed1e8'
fonte_int = 'Arial'
tam_font_int = 12
botao_cor = '#a7ac93'
#-----------------interface grafica-----------------------#
janela = Tk()
janela.title("Digitar Azimute e Distancia")
janela.geometry("600x400")#configura tamanho em pixel
janela["bg"] = cor_bg #fundo baseado nas configurações do programa
photo = PhotoImage(file ='icon/icon.png')#icone_do_programa
janela.iconphoto(False, photo)

cont_janela = Frame(janela, bg=cor_bg)
cont_janela.pack()
cont_01 = Frame(janela, pady=10, padx=10, bg= cor_bg)
cont_01.pack()
cont_01a = Frame(janela, pady=10, padx=10, bg= cor_bg)
cont_01a.pack()

titulo = Label(cont_01a, bg="#353535",fg=cor_fg, font=(fonte_int,'14','bold'), width=60, text="DIGITAR AZIMUTES")
titulo.pack()
subtitulo = Label(cont_01a, bg=cor_bg,fg='gray', font=(fonte_int, '11'), text="digitar azimute para importar no autocad")
subtitulo.pack()

cont_01file = Frame(janela,pady=10, padx=10, bg= cor_bg)
cont_01file.pack()

lb_mat_numero = Label(cont_01file, bg=cor_bg,fg=cor_fg, font=(fonte_int,tam_font_int), text="N° da Matrícula")
lb_mat_numero.pack(side=LEFT)
en_mat_numero = Entry(cont_01file,  font=(fonte_int,tam_font_int), width=7)
en_mat_numero.pack(side=LEFT, padx=10)
def definir_pasta():
    #adaptar para software
    application_window = Frame(cont_01file)
    my_filetypes = [('all files', '.*'), ('text files', '.txt')]
    global path
    path = filedialog.askdirectory(parent=application_window, initialdir=os.getcwd(), title="Selecione a Pasta:")
    button_bt_01["bg"]=cor_bg
    noma_arquivo = en_mat_numero.get()
    global criar_arquivo
    criar_arquivo = (path+'/matrícula_'+noma_arquivo+'.scr')
    cad = "_PLINE\n0,0\n"
    arq = open(criar_arquivo, 'w')
    arq.write(cad)
    arq.close()

button_bt_01 = Button(cont_01file, bg='#bd1a34',fg=cor_fg, font=(fonte_int,tam_font_int), width=15, text="SALVAR EM", command=definir_pasta)
button_bt_01.pack()

cont_01b = Frame(janela, pady=10, padx=10, bg= cor_bg)
cont_01b.pack()

azimute = Label(cont_01b, bg=cor_bg,fg=cor_fg, font=(fonte_int,tam_font_int), width=15, text="Azimute")
azimute.pack(side=LEFT)
en_01 = Entry(cont_01b, width=10,font=(fonte_int,tam_font_int))
en_01.pack(side=LEFT)

en_02 = Entry(cont_01b, width=10,font=(fonte_int,tam_font_int))
en_02.pack(side=LEFT)

en_03 = Entry(cont_01b,width=10, font=(fonte_int,tam_font_int))
en_03.pack(side=LEFT)

cont_01c = Frame(janela, pady=10, padx=10, bg= cor_bg)
cont_01c.pack()
distancia = Label(cont_01c, bg=cor_bg,fg=cor_fg, font=(fonte_int,tam_font_int), width=15, text="Distancia")
distancia.pack(side=LEFT)

en_04 = Entry(cont_01c,width=10, font=(fonte_int,tam_font_int))
en_04.pack(side=LEFT)

cont_01d = Frame(janela, pady=10, padx=10, bg= cor_bg)
cont_01d.pack()

anterior = Label(cont_01d, bg=cor_bg,fg=cor_fg, font=(fonte_int,tam_font_int), width=15, text="Anterior")
anterior.pack()
anterior_azimute = Label(cont_01d, bg=cor_bg,fg=cor_fg, font=(fonte_int,tam_font_int),  width=25, text="00º00'00,00")
anterior_azimute.pack()

cont_01f = Frame(janela, pady=10, padx=10, bg= cor_bg)
cont_01f.pack()

def proximo():
    grau = en_01.get()
    grau = int(grau.replace(" ",""))
    minuto = en_02.get()
    minuto = int(minuto.replace(" ",""))
    segundo = en_03.get()
    segundo = int(segundo.replace(" ",""))
    distancia = en_04.get()
    distancia = distancia.replace(" ","")
    distancia = float(distancia.replace(",","."))
    line =("@{0:.2f}<{1}d{2}'{3}´´´´\n".format(distancia, grau, minuto, segundo))

    anterior_azimute["text"]=line
    anterior_azimute["fg"]="green"

    arquivo = open(criar_arquivo, 'r')
    conteudo = arquivo.readlines()
    conteudo.append(line)
    arquivo = open(criar_arquivo, 'w')
    arquivo.writelines(conteudo)
    arquivo.close()

    en_01.delete(0,END)
    en_02.delete(0,END)
    en_03.delete(0,END)
    en_04.delete(0,END)

button_bt = Button(cont_01f, bg=cor_bg,fg=cor_fg, font=(fonte_int,tam_font_int), width=15, text="PROXIMO", command=proximo)
button_bt.pack(side=LEFT)
def concluir_text():
    with open(criar_arquivo, 'r') as fd:
        txt = fd.read()  # Ler todo o arquivo

        # ocorrências no texto lido
        txt = txt.replace(r"´´´´",r'"')

    # Abrir o arquivo em modo de escrita
    with open(criar_arquivo, 'w') as fd:
        fd.write(txt)  # Escrever texto modificado
    janela.destroy()
button_bt_03 = Button(cont_01f, bg=cor_bg,fg=cor_fg, font=(fonte_int,tam_font_int), width=15, text="CONCLUIR", command=concluir_text)
button_bt_03.pack(side=LEFT)

mainloop()
