class Notebook:
  def __init__(self, bateria):
    self.bateria = bateria

  def tiene_bateria_maxima(self):
    return self.bateria == 100

notebook_de_ro = Notebook(80)