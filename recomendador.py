# Nombre: Edgar Negrin
# Email: alu0101210964@ull.edu.es
#
# Practica: Sistemas de recomendación. Modelos Basados en el Contenido
#
# recomendador.py
#
import math

# Clase recomendador que recibe el nombre del fichero del que se extraeran los documentos
class recomendador:
  def __init__(self, fileName):
    self.documents = []
    self.items = []
    self.tf = []
    self.idf = []
    self.tf_idf = []
    self.similitud = []
    self.loadFile(fileName)
    self.calculateTF()
    self.calculateIDF()
    self.calculateTFIDF()
    self.similitudCoseno()
    self.showInfo()
    self.showSimilitud()
  
  # Cargar documentos
  def loadFile(self, fileName):
    textFile = open(fileName, 'r')
    self.documents = (textFile.readlines())
    for i in range(len(self.documents)):
      self.documents[i] = self.documents[i].replace(".", "").replace(",", "").replace("'", "").lower()
      self.items.append(self.documents[i].split())
  
  # Calculo de TF
  def calculateTF(self):
    for doc in range(len(self.items)):
      tf = []
      for item1 in self.items[doc]:
        frecuencia = 0
        for item2 in self.items[doc]:
          if item1 == item2:
            frecuencia += 1
        tf.append((item1, frecuencia))
      self.tf.append(list(set(tf)))
  
  # Calculo de IDF
  def calculateIDF(self):
    N = len(self.documents)
    items = []
    for i in range(len(self.documents)):
      items += self.items[i]
    items = set(items)
    self.idf = dict.fromkeys(items, 0.)
    
    for item in self.idf:
      for docSearch in range(len(self.items)):
        if item in self.items[docSearch]:
          self.idf[item] += 1
    
    for item in self.idf:
      self.idf[item] = math.log10(N / self.idf[item])
    
  # Calculo de TF-IDF
  def calculateTFIDF(self): 
    for doc in range(len(self.documents)):
      tf_idf = []
      for item in range(len(self.tf[doc])):
        cal = self.tf[doc][item][1] * self.idf[self.tf[doc][item][0]]
        tf_idf.append((self.tf[doc][item][0], cal))
      self.tf_idf.append(tf_idf)
    
  # Calculo de similitud
  def similitudCoseno(self):
    for doc1 in range(len(self.documents)):
      tfDoc1 = [i[1]**2 for i in self.tf[doc1]] 
      similitud = []
      for doc2 in range(len(self.documents)):
        tfDoc2 = [] 
        suma = 0
        for item2 in range(len(self.tf[doc2])):
          tfDoc2.append(self.tf[doc2][item2][1]**2)
          for item1 in range(len(self.tf[doc1])):
            if self.tf[doc2][item2][0] == self.tf[doc1][item1][0]:
              suma += self.tf[doc1][item1][1] * self.tf[doc2][item2][1]
        denominador = math.sqrt(sum(tfDoc1)) * math.sqrt(sum(tfDoc2))
        similitud.append(suma / denominador) 
      self.similitud.append(similitud)
    
  
  # Muestra por pantalla los resultados
  def showInfo(self):
    for doc in range(len(self.documents)):
      print('Documento ', doc)
      print()
      print('{5}{0:6s}{5} {5}{1:20s}{5} {5}{2:3s}{5} {5}{3:5s}{5} {5}{4:3s}{5}'.format('Indice', 'Termino', 'TF', 'IDF', 'TF-IDF', '|'))
      print()
      for item in range(len(self.tf[doc])):
        print('{5}{0:6d}{5} {5}{1:20s}{5} {5}{2:3d}{5} {5}{3:.3f}{5} {5}{4:.3f}{5}'.format(item, self.tf[doc][item][0], self.tf[doc][item][1], round(self.idf[self.tf[doc][item][0]], 3), round(self.tf_idf[doc][item][1], 3), '|'))
      print("\n\n")

  # Muestra por pantalla los resultados del calculo de la similitud
  def showSimilitud(self):
    for doc1 in range(len(self.documents)):
      print('Documento ', doc1)
      print()
      for doc2 in range(len(self.documents)):
        print('Documento ', doc2, ': ', round(self.similitud[doc1][doc2], 3))
      print()        
  