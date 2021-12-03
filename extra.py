class Celular:
  def __init__(self, bateria, saldo):
    self.bateria = bateria
    self.saldo = saldo

  def tiene_bateria_maxima(self):
    return self.bateria == 100

  def necesita_saldo(self):
    return self.saldo == 0