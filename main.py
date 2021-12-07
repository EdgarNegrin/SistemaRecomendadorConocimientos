
import argparse
from recomendador import recomendador

parser = argparse.ArgumentParser(description='Recomendador')
parser.add_argument('file', help='Load the file')

args = parser.parse_args()

recomendador(args.file)