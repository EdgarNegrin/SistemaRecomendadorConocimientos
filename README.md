Practica: Sistemas de recomendación. Modelos Basados en el Contenido  

Nombre: Edgar Negrin Gonzalez  
Email: alu0101210964@ull.edu.es  

**Ejemplo de uso** 

$ python3 main.py documents\documents-02.txt  

Documento  0

|Indice| |Termino             | |TF | |IDF  | |TF-IDF|  
  
|     0| |spicy               | |  1| |1.000| |1.000|  
|     1| |a                   | |  3| |0.097| |0.291|  
|     2| |and                 | |  1| |0.000| |0.000|  
|     3| |its                 | |  2| |0.699| |1.398|  
|     4| |aftertaste          | |  1| |1.000| |1.000|  
|     5| |very                | |  1| |1.000| |1.000|  
|     6| |pepper              | |  1| |0.523| |0.523|   
|     7| |with                | |  3| |0.097| |0.291|  
|     8| |as                  | |  2| |1.000| |2.000|   
|     9| |wine                | |  2| |0.523| |1.046|    
|    10| |strongly            | |  1| |1.000| |1.000|   
|    11| |layered             | |  1| |1.000| |1.000|  
|    12| |almost              | |  1| |1.000| |1.000|  
|    13| |dry                 | |  1| |0.699| |0.699|  
|    14| |character           | |  1| |0.699| |0.699|  
|    15| |food                | |  1| |1.000| |1.000|  
|    16| |is                  | |  1| |0.301| |0.301|  
|    17| |crisp               | |  1| |1.000| |1.000|  
|    18| |tight               | |  1| |1.000| |1.000|  
|    19| |citrus              | |  1| |1.000| |1.000|  
|    20| |well                | |  1| |1.000| |1.000|  
|    21| |this                | |  1| |0.097| |0.097|    
|    22| |texture             | |  1| |1.000| |1.000|  
|    23| |taut                | |  1| |1.000| |1.000|  
|    24| |mineral             | |  1| |1.000| |1.000|  

.  
.  
.  
 
Documento  0  
  
Documento  0 :  1.0  
Documento  1 :  0.187  
Documento  2 :  0.232  
Documento  3 :  0.2  
Documento  4 :  0.305  
Documento  5 :  0.289  
Documento  6 :  0.275  
Documento  7 :  0.088  
Documento  8 :  0.212  
Documento  9 :  0.18  
  
.  
.  
.  


**DESCRIPCIÓN DEL CÓDIGO**

Para la realizacion de esta practica se han creado dos ficheros, el main.py el cual ejecuta el recomendador y recomendador.py donde se encuentra la clase recomendador que contiene todo lo necesario para la mostrar la información requerida. 
El fichero *main.py* solo extrae el nombre del fichero que se desea abrir, crea el objeto recomendador y le pasa el nombre del fichero. 


**Clase recomendador**

Comenzamos explicando los diferentes atributos que se usan para almacenar la información que se va extraendo de los documentos.

* documents: array con cada documento.
* items: array de documentos con un array de las palabras del documento (array de arrays).
* tf: array de documentos con un array de tuplas con la palabra y su frecuencia en el documento(array de arrays).
* idf: diccionario de palabras con el numero de documentos en el que aparece.
* tf_idf: array de documentos con un array de tuplas con la palabra y su tf-idf (array de arrays).
* similitud: array de arrays con las similitudes entre cada par de documentos.


* **LoadFile**

Al crear un objeto de esta clase solo sera necesario pasarle por parametro el nombre del fichero del que se desean extraer los documentos. Para extraer la informacion necesaria del fichero se ha creado un metodo denominado *loadFile*, este recibe el nombre del fichero del cual extraeremos los documentos y haciendo uso de los metodos *replace* y *split* eliminaremos los signos de puntuación y separaremos cada documento por palabras que deberemos almacenar para poder operar con ello. Como resultado tendremos un atributo *documents* array con los documentos del fichero y otro atributo *items* array de arrays con las palabras de cada documento.


* **calculateTF**

Sera necesario otro metodo para realizar el calculo de la frecuencia de cada palabra en cada documento. En este realizaremos un conteo de todas las palabras, una vez tenemos el conteo debemos eliminar los duplicados por lo que hacemos uso de *set()* y volvemos a transformarlo a una lista. Con esto tenemos como resultado en el atributo *tf* un array de arrays con la fracuencia de cada palabra en cada documentos sin repeticiones.

* **calculateIDF**

Es necesario saber la frecuencia inversa de cada una de las palabras, por lo que se ha creado otro metodo para este proposito. Para almacenar esta información que se va a calcular será necesario un diccionario ya que esta información es generica para todos los documentos, debemos identificar por palabra. Primero generamos un array con todas las palabras de los documentos sin repeticion, con ello generamos un diccionario y lo rellenamos con 0. Teniendo el diccionario solo restaria calcular la cantidad de documentos en los que aparece cada palabra y con este resultado realizariamos el logaritmo en base 10 de la división entre el número de documentos y la cantidad de documentos en los que aparece cada palabra. El resultado es un atributo *idf* con un diccionario donde la clave es la palabra y el elemento es el idf calculado.

* **calculateTFIDF**

Por último será necesario calcular el TF-IDF el cual se extrae de la multiplicación del tf de cada palabra con su idf. Este metodo realiza esta operación para cada una de las palabras de cada documento. El resultado es un atributo *tf_idf* array de array de tuplas donde se almacena la palabra y su tf-idf con una forma muy parecida al anterior atributo *tf*.

* **similitudCoseno**

Una vez tenemos todos los datos calculados solo restaria el calculo de la similitud entre cada par de documentos haciendo uso del coseno. Este metodo comienza con la extracción de todos los tf del documento a comparar para elevarlo al cuadrado.

```tfDoc1 = [i[1]**2 for i in self.tf[doc1]] ``` 

Una vez tenemos uno de los documentoa, extraemos el del otro documento al que se va a comparar.

```tfDoc2.append(self.tf[doc2][item2][1]**2)```

Tambien será necesario multiplicar el tf de cada una de las palabras que contengan los dos documentos que se estan comparando, por lo que recorremos las palabras de uno de los documentos y las vamos comparando con el otro.

```
for item2 in range(len(self.tf[doc2])):
  for item1 in range(len(self.tf[doc1])):
    if self.tf[doc2][item2][0] == self.tf[doc1][item1][0]:
```

En caso de que exista esa palabra en los dos documentos, reazizamos la multiplicación de los tf y lo vamos acumulando. (Nota: recordar que *tf* es una tupla, el primer elemento tiene la palabra y el segundo el valor)

```
suma += self.tf[doc1][item1][1] * self.tf[doc2][item2][1]
```

Por último quedaría calcular la raiz cuadrada de cada una de las sumas de los tf al cuadrado de cada documento, multiplicarlos entre sí. Con este resultado ya podemos hacer la división entre lo acumulado anteriormente y este ultimo calculo, dando lugar a la similitud entre cada par de documentos. 

```
denominador = math.sqrt(sum(tfDoc1)) * math.sqrt(sum(tfDoc2))
similitud.append(suma / denominador) 
```

Como resultado tendremos un array de arrays con cada uno de los valores de la similitud entre documentos.


* **showInfo y showSimilitud**

Estos dos metodos son los encargados de mostrar la información obtenida de forma visual por consola.
