# Grupo: R2-D2 e C-3PO
"""
alunos: 
Paulo Henrique Mendonça Leite, 
Luiz Gustavo Paredes Delgado, 
Gabriel Silveira de Oliveira, 
Israel Ribeiro ALencar
Davi Mortari Vargas
"""
from lexer import CalcLexer
from parser import CalcParser
import sys
import pprint


class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR


if __name__ == "__main__":

    # pegando nome do arquivo
    filename = sys.argv[-1]

    f = open(filename)
    data = f.read()

    lexer = CalcLexer()
    parser = CalcParser()

    # Para imprimir os tokens entregados pelo Analisador Léxico descomente

    # print(f"<Numero da linha do token, Token, Atributo (quando possuir atributo)>")
    # for tok in lexer.tokenize(data):
    #     print(tok)
    # print(f"{bcolors.OK}<line:{tok.lineno}, {bcolors.FAIL}type:{tok.type}, {bcolors.WARNING}value:{tok.value}>")
    # print(bcolors.RESET)

    result = parser.parse(lexer.tokenize(data))

    # Para ver a árvore sintática (sem polimento) descomente

    # pprint.pprint(result)

    if result:
        print('Nenhum erro de sintaxe encontrado!')

    f.close()
