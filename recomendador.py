
class recomendador:
  def __init__(self, fileName):
    self.documents = []
    self.items = []
    self.loadFile(fileName)
      
  def loadFile(self, fileName):
    textFile = open(fileName, 'r')
    self.documents = (textFile.readlines()) ## almacena los saltos de linea / hay que eliminarlos
    for i in range(len(self.documents)):
      self.documents[i] = self.documents[i].replace(".", "").replace(",", "")
      self.items.append(self.documents[i].split())
    print(self.items[0])
    
  
  