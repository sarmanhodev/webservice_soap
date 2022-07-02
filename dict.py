"""
ARQUIVO dict.py PARA CONVERTER DICIONÁRIOS EM ARQUIVOS XML.
PARA ESSA FUNCIONALIDADE, USEI A DEPENDÊNCIA dicttoxml, PARA EFETUAR A CONVERSÃO DOS DICIONÁRIOS PARA XML

"""


from dicttoxml import dicttoxml
import collections
from xml.dom.minidom import parseString 



#DICIONÁRIO DE LIVROS
livros=[
    {'id':1, 
        'titulo':  "Harry Potter e a Pedra Filosofal",
        'paginaInicial':1,
        'paginaFinal': 309 ,
        'anoPublicacao': 1998 
    },

    {'id':2, 
        'titulo':  "Era dos Extremos: o breve século XX, 1914–1991",
        'paginaInicial':1,
        'paginaFinal': 632,
        'anoPublicacao': 1994 
        },

    {'id':3, 
        'titulo':  "American Sniper: The Autobiography of the Most Lethal Sniper in U.S. Military History",
        'paginaInicial':1,
        'paginaFinal':400,
        'anoPublicacao': 2012
    }
      
]  


#DICIONÁRIO DE AUTORES
autores = [
    {
        'autor':{
            'id':1,
            'cpf':'111.222.333-00',
            'nome': 'J.K. Rowling',
            'livro':livros[0]
            }
    },

     {
        'autor':{
            'id':2,
            'cpf':'222.333.444-11',
            'nome': 'Eric John Ernest Hobsbawm',
            'livro':livros[1]
            }
    },

     {
        'autor': {
            'id':3,
            'cpf':'333.444.777-22',
            'nome': ' Chris Kyle',
            'livro':livros[2]
            }
    },
]
    

#VARIÁVEL X FAZ UMA VARREDURA NA VARIÁVEL AUTORES
for x in autores:
    #VARIÁVEL dictlike RECEBE A COLEÇÃO DE DADOS OBTIDOES NO LAÇO FOR, DE MANEIRA ORDENADA
    dictlike = collections.OrderedDict(x)
    #VARIÁVEL XML RECEBE OS DADOS ORDENADOS
    xml = dicttoxml(dictlike, ids = True, root = False)

    dom = parseString(xml) 
    #MÉTODO toprettyxml() PARA ORGANIZAR TODA A ÁRVORE DO ARQUIVO XML
    print(dom.toprettyxml()) 
    



