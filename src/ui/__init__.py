import tkinter as tk
from src.entities.logger import Logger
from src.services.service import Service
from src.entities.ponto import Ponto

class App(tk.Frame):
    # ------- Cores --------
    FUNDO = "#23272B" 
    LARANJA_MOSTARDA = "#8C3F23"
    CINZA_CLARO = "#F2F2F2"
    ERRO_CAMPO = "#F2BFBB"
    # ------- Texto -------
    FONTE_REGULAR = (None, 11)
    FONTE_TITULO = (None, 12)
    
    # parametros
    CASAS_DECIMAIS = 2
    
    def __init__(self, janela):
        super().__init__(janela)
        self.__logger = Logger(nome='App')
        self.janela = janela
        self.service = None
        self.coordenada_anterior = '>'
        self.__config()
        self.inicio()
        self.iniciar_service()
        
    
    def __config(self):
        """
        Descrição
            Configurações da interface.
        """ 
        self.janela.geometry("400x300")
        self.janela.title("Dig. coordenadas UTM")
        self.janela["bg"] = self.FUNDO

    
        photo = tk.PhotoImage(file ='icon/icon.png')
        self.janela.iconphoto(False, photo)
        self.__logger.log_info("carregada as configurações da interface")
    def iniciar_service(self):
        try:
            self.service = Service()
        except Exception as erro:
            self.__logger.log_error(f"{erro}")
            self.caixa_de_mensagem("Erro",erro)
            
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
        
        container_coordx = self.container(self.container_principal)
        container_coordx.pack()
        coordx = tk.Label(container_coordx, text="Coordenada X",font=self.FONTE_REGULAR, bg=self.FUNDO, fg=self.CINZA_CLARO, padx=5)
        coordx.pack(side='left')
        self.ent_coordx = tk.Entry(container_coordx, width=15)
        self.ent_coordx.pack()
        
        container_coordy = self.container(self.container_principal)
        container_coordy.pack()
        coordy = tk.Label(container_coordy, text="Coordenada Y",font=self.FONTE_REGULAR, bg=self.FUNDO, fg=self.CINZA_CLARO, padx=5)
        coordy.pack(side='left')
        self.ent_coordy = tk.Entry(container_coordy, width=15)
        self.ent_coordy.pack()
        
        container_texto = self.container(self.container_principal)
        container_texto.pack()
        coordx = tk.Label(container_texto, text=f"{self.coordenada_anterior}",font=self.FONTE_REGULAR, bg=self.FUNDO, fg=self.LARANJA_MOSTARDA)
        coordx.pack()
        
        container_botao = self.container(self.container_principal)
        container_botao.pack()
        bt_inserir = tk.Button(container_botao,text="Inserir", font=self.FONTE_REGULAR,  border=0.5, bg=self.FUNDO, fg=self.CINZA_CLARO, width=10, height=1, command=self.adicionar_ponto)
        bt_inserir.pack()
        
    def adicionar_ponto(self):
        numero_erro = 0
        
        try:
            descricao = self.formatar_texto_entrada(self.ent_descricao.get())
            self.ent_descricao["bg"] = "White"
        except Exception as erro:
            self.__logger.log_error(f"descrição - {erro}")
            self.ent_descricao["bg"] = self.ERRO_CAMPO
            numero_erro += 1
            
        try:
            coordy = self.formatar_coordenadaEntrada(self.ent_coordy.get())
            self.ent_coordy["bg"] = "White"
        except Exception as erro:
            self.__logger.log_error(f"coordenada y - {erro}")
            self.ent_coordy["bg"] = self.ERRO_CAMPO
            numero_erro += 1
            
        try:
            coordx = self.formatar_coordenadaEntrada(self.ent_coordx.get())
            self.ent_coordx["bg"] = "White"
        except Exception as erro:
            self.__logger.log_error(f" coordenada x - {erro}")
            self.ent_coordx["bg"] = self.ERRO_CAMPO
            numero_erro += 1
            
        try:
            if numero_erro != 0:
                raise ValueError("Corrija os campos indicados.")
            
            ponto = Ponto(descricao, coordx, coordy)
            
            self.ent_descricao.delete(0, tk.END)
            self.ent_coordy.delete(0, tk.END)
            self.ent_coordx.delete(0, tk.END)
            
            if self.service == None:
                self.iniciar_service()
            
            self.service.inserir_coordenada(ponto=ponto)
            
        except ValueError as erro:
            self.__logger.log_error(f"{erro}")
            self.caixa_de_mensagem("Erro de Preenchimento",erro)
            
        except FileExistsError as erro:
            self.__logger.log_error(f"{erro}")
            self.caixa_de_mensagem("Erro arquivo", erro)
            
        except Exception as erro:
            self.__logger.log_error(f"{erro}")
            self.caixa_de_mensagem("Erro",erro)
            
        else:
            self.coordenada_anterior = f"anterior\n {ponto}"
            self.__logger.log_info(self.coordenada_anterior)      
        
        finally:
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
    
    def formatar_texto_entrada(self, texto):
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
    
    def formatar_coordenadaEntrada(self, coordenada):
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
    
    def caixa_de_mensagem(self, title: str, mensagem: str ):
        """
            Cria caixa de mensagem para poupups na tela.
            O tkinter nativamente possui o messagebox para esse tipo de situação,
            mas criar essa implementação permite um grau de custumização mais elevado.
        Args:
            title (str): titulo da janela
            mensagem (str): mensagem.
        """
        caixa_mensagem = tk.Tk()
        caixa_mensagem.title(title)
        caixa_mensagem.geometry("300x100")
        caixa_mensagem["bg"] = self.FUNDO
        
        container = tk.Frame(caixa_mensagem, padx=5, pady=10, bg=self.FUNDO)
        container.pack()
        
        mensagem_label = tk.Label(container, text=mensagem, bg=self.FUNDO, fg=self.CINZA_CLARO )
        mensagem_label.pack()
        mensagem_button = tk.Button(container, text="ok", font=self.FONTE_REGULAR,  border=0.5, bg=self.FUNDO, fg=self.CINZA_CLARO, width=10, height=1, command=caixa_mensagem.destroy)
        mensagem_button.pack()
        
        caixa_mensagem.mainloop()