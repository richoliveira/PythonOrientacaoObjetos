class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    # Metodo nome com property
    @property
    def nome (self):
        print("Acessou o metodo property nome().")
        return self.__nome.title()

    # Metodo setter para alterar o nome sem a necessidade de chamar como um Metodo
    @nome.setter
    def nome (self, nome):
        print("Chamou o metodo setter nome().")
        self.__nome = nome