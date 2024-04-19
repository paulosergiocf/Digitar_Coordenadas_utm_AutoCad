from src.usecases.logger import Logger
from src.usecases.autocad import Autocad

class Service:
    def __init__(self):
        self.__logger = Logger(nome='Service')
        self.__logger.log_info("inicio do serviço")
        self.__cad = Autocad()
        
    
    def inserir_coordenada(self):
        pass