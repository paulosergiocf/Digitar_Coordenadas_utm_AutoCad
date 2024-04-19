import os
import tkinter as tk
from tkinter import font, filedialog, ttk
from src.usecases.logger import Logger
from src.usecases.util import Util
from src.services.service import Service
from src.entities.ponto import Ponto

class App(tk.Frame):
    # ------- Cores --------
    FUNDO = "#23272B" 
    ROSA_CLARO = "#7E3735"
    LARANJA_MOSTARDA = "#8C3F23"
    CINZA_CLARO = "#F2F2F2"
    ERRO_CAMPO = "#F2BFBB"
    # ------- Texto -------
    FONTE_REGULAR = (None, 11)
    FONTE_TITULO = (None, 12)
    
    #
    CASAS_DECIMAIS = 2
    
    def __init__(self, janela):
        super().__init__(janela)
        self.__logger = Logger(nome='App')
        self.janela = janela
        self.service = None
        self.coordenada_anterior = '>'
        self.__config()
        self.inicio()
        
    
    def __config(self):
        """
        Descrição
            Configurações da interface.
        """ 
        self.janela.geometry("400x300")
        self.janela.title("Dig. coordenadas UTM")
        self.janela["bg"] = self.FUNDO
        estilo = ttk.Style()
        estilo.theme_use('default')
        estilo.configure('Custom.TButton', background=self.FUNDO) 
    
        photo = tk.PhotoImage(file ='src/icon/icon.png')
        self.janela.iconphoto(False, photo)
        self.__logger.log_info("carregada as configurações da interface")
    def iniciar_service(self):
        self.service = Service()
    def atualizar_tela(self):
        self.container_principal.forget()
        self.inicio()
        
    def inicio(self):
        """
        Descrição:
            Tela inicial da aplicação.
        """
        
        self.container_principal = self.container(self.janela, margem_vertical=15)
        self.container_principal.pack(anchor='center')
        
        container_titulo = self.container(self.container_principal, margem_vertical=10)
        container_titulo.pack()
        texto = tk.Label(container_titulo, text="Digitar Coordenadas UTM AutoCad",font=self.FONTE_TITULO, bg=self.FUNDO, fg=self.CINZA_CLARO)
        texto.pack()
        
        container_desc = self.container(self.container_principal)
        container_desc.pack()
        descricao = tk.Label(container_desc, text="       Descrição",font=self.FONTE_REGULAR, bg=self.FUNDO, fg=self.CINZA_CLARO, padx=5)
        descricao.pack(side='left')
        self.ent_descricao = tk.Entry(container_desc, width=15)
        self.ent_descricao.pack()
        
        container_coordy = self.container(self.container_principal)
        container_coordy.pack()
        coordy = tk.Label(container_coordy, text="Coordenada Y",font=self.FONTE_REGULAR, bg=self.FUNDO, fg=self.CINZA_CLARO, padx=5)
        coordy.pack(side='left')
        self.ent_coordy = tk.Entry(container_coordy, width=15)
        self.ent_coordy.pack()
        
        container_coordx = self.container(self.container_principal)
        container_coordx.pack()
        coordx = tk.Label(container_coordx, text="Coordenada X",font=self.FONTE_REGULAR, bg=self.FUNDO, fg=self.CINZA_CLARO, padx=5)
        coordx.pack(side='left')
        self.ent_coordx = tk.Entry(container_coordx, width=15)
        self.ent_coordx.pack()
        
        
        container_texto = self.container(self.container_principal)
        container_texto.pack()
        coordx = tk.Label(container_texto, text=f"{self.coordenada_anterior}",font=self.FONTE_REGULAR, bg=self.FUNDO, fg=self.LARANJA_MOSTARDA)
        coordx.pack()
        
        container_botao = self.container(self.container_principal)
        container_botao.pack()
        bt_inserir = tk.Button(container_botao,text="Inserir", relief="flat",font=self.FONTE_REGULAR, border=0, bg=self.FUNDO, fg=self.CINZA_CLARO, width=10, height=1, command=self.adicionar_ponto)
        bt_inserir.pack()
        
    def adicionar_ponto(self):
        numero_erro = 0
        
        try:
            descricao = self.formatarTextoEntrada(self.ent_descricao.get())
            self.ent_descricao["bg"] = "White"
        except Exception as erro:
            self.__logger.log_error(f"{self.ent_descricao} - {erro}")
            self.ent_descricao["bg"] = self.ERRO_CAMPO
            numero_erro += 1
            
        try:
            coordy = self.formatarCoordenadaEntrada(self.ent_coordy.get())
            self.ent_coordy["bg"] = "White"
        except Exception as erro:
            self.__logger.log_error(f"{self.ent_coordy} - {erro}")
            self.ent_coordy["bg"] = self.ERRO_CAMPO
            numero_erro += 1
            
        try:
            coordx = self.formatarCoordenadaEntrada(self.ent_coordx.get())
            self.ent_coordx["bg"] = "White"
        except Exception as erro:
            self.__logger.log_error(f"{self.ent_coordx} - {erro}")
            self.ent_coordx["bg"] = self.ERRO_CAMPO
            numero_erro += 1
        
        if numero_erro <= 0:
            ponto = Ponto(descricao, coordx, coordy)
            self.coordenada_anterior = f"{ponto.descricao} - X:{ponto.coordenada_x} - Y:{ponto.coordenada_y}"
            self.__logger.log_info(self.coordenada_anterior)
            self.ent_descricao.delete(0, tk.END)
            self.ent_coordy.delete(0, tk.END)
            self.ent_coordx.delete(0, tk.END)
            self.atualizar_tela()
            
        
    def container(self, janela, fundo=FUNDO, margem_horizontal=5, margem_vertical=5):
        """
        Descrição
        
            Modelo de tk.Frame pré configurado.
        Args:
            janela (tk.Frame): janela mãe
            fundo (str, optional): cor rgb. Defaults to CINZA_ESCURO.
            margem_horizontal (int, optional): tamanho da margem horizontal em pixel. Defaults to 5.
            margem_vertical (int, optional): tamanho da margem vertical em pixel. Defaults to 5.

        Returns:
            tk.Frame: container configurado.
        """
        container = tk.Frame(janela, background=fundo, padx=margem_horizontal, pady=margem_vertical)
        return container
    
    def formatarTextoEntrada(self, texto):
        """
        Args:
            texto (str): descrição do texto

        Returns:
            str: se for numero adicionar prefixo P - retorna descrição tradada.
        """
        texto = texto.strip().upper()
        if len(texto) == 0:
            raise ValueError("É necessário digitar um valor no campo descrição.")
        
        if texto.isnumeric():
            return f"P-{texto}"

        return texto
    
    def formatarCoordenadaEntrada(self, coordenada):
        """
        Args:
            coordenada (str): coordenada

        Raises:
            ValueError: coordenada sem preenchimento

        Returns:
            float: coordenada formatada
        """
        if len(coordenada) == 0:
            raise ValueError("É necessário digitar um valor no campo coordenada")
    
        coordenada: float = float(coordenada.replace(",",".").strip())
        coordenada = round(coordenada, self.CASAS_DECIMAIS)
        
        return coordenada