import os
import logging
from datetime import datetime

class Logger(logging.Logger):
    DIRETORIO_LOG = 'logs'
    
    def __init__(self, nome: str, nivel=logging.INFO):
        """Descrição
            Classe para padronizar a gravação de logs na aplicação.

        Args:
            nome (str): nome da classe em que está sendo instanciada.
            nivel (opcional): tipo do log conforme lib logging. padrão logging.INFO.
        """
        super().__init__(name=nome, level=nivel)
        self.__criar_diretorio_log(self.DIRETORIO_LOG)
        self.diretorio = os.path.join(os.getcwd(), self.DIRETORIO_LOG)
        self.nome = nome
        self.arquivo_log = os.path.join(self.diretorio, f"{str(datetime.now().strftime('%Y-%m-%d'))}.log")
        self.__configuracao()
        
    def __configuracao(self):
        """
        Descrição.
            Define configuração do logger.
        """
        manipulador_arquivo = logging.FileHandler(self.arquivo_log, mode='a', encoding='utf-8')
        formato = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        manipulador_arquivo.setFormatter(formato)
        self.addHandler(manipulador_arquivo)
    
    def log_info(self, mensagem):
        """
        Descrição
            tipo INFO: log informativo sobre fluxo normal da aplicação.
        Args:
            mensagem (str): mensagem referente ao conteudo que quer logar.
        """
        self.info(f"{self.nome} - {mensagem}.")
        
    def log_warn(self, mensagem):
        """
        Descrição
            tipo WARN: log de aviso sobre aspectos da aplicação.
        Args:
            mensagem (str): mensagem referente ao conteudo que quer logar.
        """
        self.warning(f"{self.nome} - {mensagem}.")

    def log_error(self, mensagem):
        """
        Descrição
            ipo ERROR: log para relatar exceções da aplicaçõa,
            é importante logar o maximo de informações para o problema
            possa ser identificado mais facílmente.
        Args:
            mensagem (str): mensagem referente ao conteudo que quer logar.
        """
        self.error(f"{self.nome} - {mensagem}.")
        
    def __criar_diretorio_log(self, diretorio: str):
        """Descrição

        Args:
            diretorio (str): diretorio
        """
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
