# Nombre: Edgar Negrin
# Email: alu0101210964@ull.edu.es
#
# Practica: Sistemas de recomendación. Modelos Basados en el Contenido
#
# Ejemplo de uso: python3 main.py documents\documents-01.txt
#
# main.py
#

import argparse
from recomendador import recomendador

parser = argparse.ArgumentParser(description='Recomendador')
parser.add_argument('file', help='Load the file')

args = parser.parse_args()

recomendador(args.file)
