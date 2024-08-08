class Bus:
    def __init__(self):
        self.posicion = 0
    
    @staticmethod
    def dibujar_inicio_pista():
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    
    def dibujar_bus(self, desface, nombre):
        self.posicion += desface
        print("                                                                                                                                                 ")
        print(" " * self.posicion + nombre)
        print(" " * self.posicion + "     _____")
        print(" " * self.posicion + " __/__|__\\___")
        print(" " * self.posicion + "|_  _____  __|")
        print(" " * self.posicion + "O O      O O")
    
    @staticmethod
    def dibujar_final_pista():
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    
        
        
        