
"""
PARA ESTE PROJETO, FOI USADO O FRAMEWORK FASTAPI, PARA GERAR OS ENDPOINTS.

PARA CONECTAR AO SERVIDOR: uvicorn main:app --reload

PARA ACESSAR A DOCUMENTAÇÃO SWAGGER, BASTA DIGITAR LOCALHOST/DOCS NA BARRA DE PESQUISA DO NAVEGADOR

"""


from fastapi import FastAPI, Body, Response, status




app = FastAPI() 


#ENDPOINT DE BOAS VINDAS
@app.get("/", status_code=status.HTTP_200_OK)
async def read(): 
    """
    Mensagem de boas vindas!
    """
    return {'Hello Dev!'}
         
    

#ENDPOINT QUE RETORNA TODOS OS LIVROS CADASTRADOS E SEUS RESPECTIVOS AUTORES
@app.get("/livros", status_code=status.HTTP_200_OK)
def all_books():
    """
    RETORNA A LISTA DE TODOS OS LIVROS COM SEUS RESPECTIVOS AUTORES
    """
     
          
    xml = """<?xml version="1.0" encoding="UTF-8" ?>
    <livros>
    <livro id="1" type="dict">
        <id id="1" type="int">1</id>
        <titulo id="1" type="str">Harry Potter e a Pedra Filosofal</titulo>
        <paginaInicial id="1" type="int">1</paginaInicial>
        <paginaFinal id="1" type="int">309</paginaFinal>
        <anoPublicacao id="1" type="int">1998</anoPublicacao>
        <autor id="1" type="dict">
                <id id="1" type="int">1</id>
                <cpf id="1" type="str">111.222.333-00</cpf>
                <nome id="1" type="str">J.K. Rowling</nome>
        </autor>
    </livro>


    <livro id="2" type="dict">
        <id id="2" type="int">2</id>
        <titulo id="2" type="str">Era dos Extremos: o breve século XX, 1914–1991</titulo>
        <paginaInicial id="2" type="int">1</paginaInicial>
        <paginaFinal id="2" type="int">632</paginaFinal>
        <anoPublicacao id="2" type="int">1994</anoPublicacao>
        <autor id="2" type="dict">
                <id id="2" type="int">2</id>
                <cpf id="2" type="str">222.333.444-11</cpf>
                <nome id="2" type="str">Eric John Ernest Hobsbawm</nome>
        </autor>
    </livro>


    <livro id="3" type="dict">
        <id id="3" type="int">3</id>
        <titulo id="3" type="str">American Sniper: The Autobiography of the Most Lethal Sniper in U.S. Military History</titulo>
        <paginaInicial id="3" type="int">1</paginaInicial>
        <paginaFinal id="3" type="int">400</paginaFinal>
        <anoPublicacao id="3" type="int">2012</anoPublicacao>
        <autor id="3" type="dict">
                <id id="3" type="int">3</id>
                <cpf id="3" type="str">333.444.777-22</cpf>
                <nome id="3" type="str"> Chris Kyle</nome>
        </autor>
    </livro>

    </livros>
    """
    return Response(content=xml, media_type="application/xml")


#ENDPOINT QUE RETORNA TODOS OS AUTORES CADASTRADOS E SUAS RESPECTIVAS OBRAS LITERÁRIAS
@app.get("/autores", status_code=status.HTTP_200_OK)
def all_authors():
    """
    RETORNA A LISTA DE TODOS OS AUTORES E SUAS RESPECTIVAS OBRAS LITERÁRIAS
    """
     
          
    xml = """<?xml version="1.0" encoding="UTF-8" ?>
        <autor>

                <autor id="1" type="dict">
                        <id id="1" type="int">1</id>
                        <cpf id="1" type="str">111.222.333-00</cpf>
                        <nome id="1" type="str">J.K. Rowling</nome>
                        <livro id="1" type="dict">
                                <id id="1" type="int">1</id>
                                <titulo id="1" type="str">Harry Potter e a Pedra Filosofal</titulo>
                                <paginaInicial id="1" type="int">1</paginaInicial>
                                <paginaFinal id="1" type="int">309</paginaFinal>
                                <anoPublicacao id="1" type="int">1998</anoPublicacao>
                        </livro>
                </autor>


                <autor id="2" type="dict">
                        <id id="2" type="int">2</id>
                        <cpf id="2" type="str">222.333.444-11</cpf>
                        <nome id="2" type="str">Eric John Ernest Hobsbawm</nome>
                        <livro id="2" type="dict">
                                <id id="2" type="int">2</id>
                                <titulo id="2" type="str">Era dos Extremos: o breve século XX, 1914–1991</titulo>
                                <paginaInicial id="2" type="int">1</paginaInicial>
                                <paginaFinal id="2" type="int">632</paginaFinal>
                                <anoPublicacao id="2" type="int">1994</anoPublicacao>
                        </livro>
                </autor>


                <autor id="2" type="dict">
                        <id id="2" type="int">3</id>
                        <cpf id="2" type="str">333.444.777-22</cpf>
                        <nome id="2" type="str"> Chris Kyle</nome>
                        <livro id="2" type="dict">
                                <id id="2" type="int">3</id>
                                <titulo id="2" type="str">American Sniper: The Autobiography of the Most Lethal Sniper in U.S. Military History</titulo>
                                <paginaInicial id="2" type="int">1</paginaInicial>
                                <paginaFinal id="2" type="int">400</paginaFinal>
                                <anoPublicacao id="2" type="int">2012</anoPublicacao>
                        </livro>
                </autor>

        </autor>
    """
    return Response(content=xml, media_type="application/xml")



if __name__ == "__main__":
    app.run(app, host="0.0.0.0", port=8000)