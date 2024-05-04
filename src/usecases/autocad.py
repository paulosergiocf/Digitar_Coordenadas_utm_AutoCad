from src.entities.ponto import Ponto
from pyautocad import Autocad, APoint
from src.entities.logger import Logger

class AutoCadTool():
    
    # constantes da classe
    
    QUEBRA_LINHA = '\n'
    TAMANHO_TXT = 2.5 # tamanho do texto que sera exibido no DWG.
    RAIO_CIRCLE = 10 # raio do circulo de representara o ponto no DWG.
    
    def __init__(self):
        self.__logger = Logger(nome='AutoCad')
        self.acad = Autocad()
        self.__iniciar()
    
    def __iniciar(self):
        """
        imprime mensagem de inicio no prompt de comando.
        
        Raises:
            FileExistsError: retorna execeção se nenhum arquivo dwg estiver aberto.
        """
        try:
            self.acad.prompt(f"Ferramenta de inserção de coordenadas iniciada{self.QUEBRA_LINHA}")
            self.__logger.log_info("Ferramenta de inserção de coordenadas iniciada")
        except Exception as erro:
            self.__logger.log_error(erro)
            raise FileExistsError("Nenhum arquivo DWG aberto.")
        
    def prompt(self, msg: str):
        """
        Apresenta mensagem no cli autocad.

        Args:
            msg (str): mensagem para cli autocad
        """
        self.acad.prompt(f"{msg}{self.QUEBRA_LINHA}")
    
    def inserir_ponto(self, ponto: Ponto):
        """
        Insere ponto do Autocad.

        Args:
            ponto (Ponto): _description_
        """
        try:
            ponto_tmp = APoint(ponto.coordenada_x, ponto.coordenada_y)
            self.acad.model.AddText('%s' % ponto.descricao, ponto_tmp, self.TAMANHO_TXT)
            self.acad.model.AddCircle(ponto_tmp, 2)
            
            for text in self.acad.iter_objects('Text'):
                text.InsertionPoint = APoint(text.InsertionPoint)
                
        except Exception as erro:
            self.__logger.log_error(erro)
            raise erro