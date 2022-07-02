# webservice_soap

Para executar o projeto, é necessário criar um ambiente virtual: abrir o terminal do VSCODE e dar o seguinte comando: pip install virtualenv
Após a virtual env ser instalada, basta dar o seguinte comando para criar seu ambiente virtual: virtualenv env

Após criar a env, basta instalar as dependências necessárias: 
1 - .\env\Scripts\pip3 install fastapi
2 - .\env\Scripts\pip3 install uvicorn

para executar o código da FastAPI, basta dar o seguinte comando: uvicorn main:app --reload

Quando o servidor uvicorn iniciar, basta abrir o navegador, digitar o localhost e o endpoint desejado, por exemplo: localhost/livros (retornará todos os livros e seus respectivos autores); localhost/autores (retprnará a lista de todos os autores e suas respectivas obras literárias).
