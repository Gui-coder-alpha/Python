#POO básico

class carro:
    def __init__(self, marca, modelo, ano, documentos):
        self._marca = marca
        self._modelo = modelo
        self.ano = ano
        self.documento = documentos

    def __str__(self):
        return f"marca:{self.marca}, modelo:{self._modelo}, ano:{self.ano}, documento:{self.documento}"

informacao = carro("chevrolet", "camaro", 2017, "aosdnaniaodj dnqwije eqiejqdamlmd qi12931ikma dadkl")

print(informacao)