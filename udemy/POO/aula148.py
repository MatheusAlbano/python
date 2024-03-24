# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Cria uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricantes na tela

class Carro:

    def __init__(self, nome_carro):
        self.nome_carro = nome_carro
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor    

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor       

class Motor:
    def __init__(self, nome_motor):
        self.nome_motor = nome_motor



class Fabricante:
    def __init__(self, nome_fabricante):
        self.nome_fabricante = nome_fabricante


hb20s = Carro('HB20S')
motor_1_6 = Motor('1.6 Flex Turbo')
hb20s.motor = motor_1_6
hyundai = Fabricante('Hyundai')
hb20s.fabricante = hyundai
print(hb20s.nome_carro, hb20s.motor.nome_motor, hb20s.fabricante.nome_fabricante)

fastback = Carro('Fastback')
motor_1_8 = Motor('1.8 Flex Turbo V8')
fastback.motor = motor_1_8
fiat = Fabricante('Fiat')
fastback.fabricante = fiat
print(fastback.nome_carro, fastback.motor.nome_motor, fastback.fabricante.nome_fabricante)

civic = Carro('Civic')
civic.motor = motor_1_8
honda = Fabricante('Honda')
civic.fabricante = honda
print(civic.nome_carro, civic.motor.nome_motor, civic.fabricante.nome_fabricante)

pulse = Carro('Pulse')
pulse.motor = motor_1_6
pulse.fabricante = fiat
print(pulse.nome_carro, pulse.motor.nome_motor,pulse.fabricante.nome_fabricante)
