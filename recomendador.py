
class recomendador:
  def __init__(self, fileName):
    self.documents = []
    self.items = []
    self.tf = []
    self.loadFile(fileName)
    self.calculateTF()
    self.showInfo()
  
  # Cargar documentos
  def loadFile(self, fileName):
    textFile = open(fileName, 'r')
    self.documents = (textFile.readlines()) ## almacena los saltos de linea / hay que eliminarlos
    for i in range(len(self.documents)):
      self.documents[i] = self.documents[i].replace(".", "").replace(",", "")
      self.items.append(self.documents[i].split())
  
  
  def calculateTF(self):
    for doc in range(len(self.items)):
      frecuenci = [self.items[doc].count(i) for i in self.items[doc]]
      self.tf.append(list(zip(set(self.items[doc]), frecuenci)))
      
  def calculateIDF(self):
    frecuenci = [self.items[doc].count(i) for i in self.items[doc]]
  
  # Muestra por pantalla los resultados
  def showInfo(self):
    for doc in range(len(self.documents)):
      print('{4}{0:6s}{4} {4}{1:24s}{4} {4}{2:3s}{4} {4}{3:3s}{4}'.format('Indice', 'Termino', 'TF', 'IDF', '|'))
      print()
      for item in range(len(self.tf[doc])):
        print('{4}{0:6d}{4} {4}{1:30s}{4} {4}{2:3f}{4} {4}{3:3s}{4}'.format(item, self.tf[doc][item][0], self.tf[doc][item][1], 'IDF', '|'))
      print("\n\n")
  
  