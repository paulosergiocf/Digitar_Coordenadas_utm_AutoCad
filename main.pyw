import tkinter as tk
from src.ui import App
from src.entities.logger import Logger

if __name__ == '__main__':
    logger = Logger(nome='Main')
    try:
        logger.log_info("inicio da execução da aplicação")
        janela = tk.Tk() 
        app = App(janela)
        app.mainloop()
    except KeyboardInterrupt as erro:
        logger.log_error("Aplicação abortada pelo usuario.")
        quit()
        
    except Exception as erro:
        logger.log_error(erro)

    finally:
        logger.log_info("fim da execução")
        
    