from src.entities.ponto import Ponto
from src.entities.logger import Logger
from src.usecases.autocad import AutoCadTool

class Service:
    def __init__(self):
        self.__logger = Logger(nome='Service')
        self.__logger.log_info("inicio do serviço")
        self.__cad = AutoCadTool()
    
    def inserir_coordenada(self, ponto: Ponto):
        """
        Aciona a classe AutoCadTool e insere o ponto.

        Args:
            ponto (Ponto): ponto a ser inserido
        """
        self.__cad.inserir_ponto(ponto=ponto)
        