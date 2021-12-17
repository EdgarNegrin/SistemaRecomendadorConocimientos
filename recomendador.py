import math

class recomendador:
  def __init__(self, fileName):
    self.documents = []
    self.items = []
    self.tf = []
    self.idf = []
    self.tf_idf = []
    self.loadFile(fileName)
    self.calculateTF()
    self.calculateIDF()
    self.calculateTFIDF()
    self.showInfo()
  
  # Cargar documentos
  def loadFile(self, fileName):
    textFile = open(fileName, 'r')
    self.documents = (textFile.readlines()) ## almacena los saltos de linea / hay que eliminarlos
    for i in range(len(self.documents)):
      self.documents[i] = self.documents[i].replace(".", "").replace(",", "").lower()
      self.items.append(self.documents[i].split())
  
  
  def calculateTF(self):
    for doc in range(len(self.items)):
      frecuenci = [self.items[doc].count(i) for i in self.items[doc]]
      self.tf.append(list(zip(set(self.items[doc]), frecuenci)))
      
  def calculateIDF(self):
    # Documentos que pueden ser recomendados
    N = len(self.documents)
    # Creacion de diccionario
    items = []
    for i in range(len(self.documents)):
      items += self.items[i]
    items = set(items)
    self.idf = dict.fromkeys(items, 0.)
    # Numero de documentos en donde la palabra aparece
    for item in self.idf:
      for docSearch in range(len(self.items)):
        if item in self.items[docSearch]:
          self.idf[item] += 1
    
    for item in self.idf:
      self.idf[item] = math.log10(N / self.idf[item])
    
    # tf/raiz(suma tfs al cuadrado) -> para hacer la similitud
  
  def calculateTFIDF(self): ## No almacena el orden correctamente, repite los mismos items
    tf_idf = []
    for doc in range(len(self.documents)):
      for item in range(len(self.tf[doc])):
        cal = self.tf[doc][item][1] * self.idf[self.tf[doc][item][0]]
        tf_idf.append((self.tf[doc][item][0], cal))
      self.tf_idf.append(tf_idf)
    
  
  # Muestra por pantalla los resultados
  def showInfo(self):
    for doc in range(len(self.documents)):
      print('{5}{0:6s}{5} {5}{1:30s}{5} {5}{2:3s}{5} {5}{3:3s}{5} {5}{4:3s}{5}'.format('Indice', 'Termino', 'TF', 'IDF', 'TF-IDF', '|'))
      print()
      for item in range(len(self.tf[doc])):
        print('{5}{0:6d}{5} {5}{1:30s}{5} {5}{2:3d}{5} {5}{3:3f}{5} {5}{4:3s}{5}'.format(item, self.tf[doc][item][0], self.tf[doc][item][1], self.idf[self.tf[doc][item][0]], self.tf_idf[doc][item][0], '|'))
      print("\n\n")
  