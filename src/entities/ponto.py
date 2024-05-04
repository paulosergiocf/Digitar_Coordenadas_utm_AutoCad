
class Ponto:
    def __init__(self, descricao: str, coordenada_x: float, coordenada_y: float):
        self.descricao: str = descricao
        self.coordenada_x: str = coordenada_x
        self.coordenada_y: str = coordenada_y
        
    def __str__(self) -> str:
        return(f"{self.descricao} - X: {self.coordenada_x} - Y: {self.coordenada_y}")