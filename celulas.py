class celula:
    """docstring for celula"""

    def __init__(self, valor, x, y):
        self.valor = valor
        self.x = x
        self.y = y

    def __getitem__(self):
    	return iter(self)
