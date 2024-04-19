from src.entities.ponto import Ponto
from pyautocad import Autocad, APoint

class AutoCad():
    QUEBRA_LINHA = '\n'
    TAMANHO_TXT = 2.5
    RAIO_CIRCLE = 10
    
    def __init__(self):
        self.__logger = Logger(nome='AutoCad')
        self.acad = Autocad()
        self.__iniciar()
    
    def __iniciar(self):
        acad.prompt(f"Ferramenta de inserção de coordenadas iniciada{self.QUEBRA_LINHA}")
        self.__logger.log_info("Ferramenta de inserção de coordenadas iniciada")
        
    def prompt(self, msg: str):
        acad.prompt(f"{msg}{self.QUEBRA_LINHA}")
    
    def inserir_ponto(self,ponto: Ponto):
        ponto_text = self.acad.model.AddText('%s' % ponto.descricao, APoint(ponto.coordenada_x, ponto.coordenada_y), self.TAMANHO_TXT)
        
