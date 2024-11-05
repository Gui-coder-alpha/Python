#polimorfismo é ter resposta diferentes, tendo vários meios de resposta, por meio
#de um única informação. Como uma variável de valor único, para várias
#respostas simultâneas

class Pato:
    def nadar(self):
        print(f"qual sabe nadar")

class camudongo:
    def nadar(self):
        print(f"camudongo safado não sabe nadar")

class golfinho:
    def nadar(self):
        print(f"Golfinho sabe nadar muito bem")


def fala(obj):
    obj.nadar()

fala(golfinho())
fala(camudongo())

