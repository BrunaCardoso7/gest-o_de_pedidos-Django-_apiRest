# README do Projeto gestao de pedidos Django apiRest


## Descrição
Instruções para configurar o ambiente de desenvolvimento da api de pedidos e executar o projeto em seu sistema.


### Detalhe importante*

Na raiz do projeto está disponível um arquivo de coleção com todas as rota do projeto já pre-definidas para utilização em programas como postman e insomnia:
```bash
./rotas_api_pedidos_postman_insominia.json
```
## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- **Python 3.x**: 
- **pip**:

### Url para acesso da documentação:

```bash
http://localhost/api/schema/swagger-ui/#/
```


Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- **Python 3.x**: 
- **pip**: 

## Passos para Executar o Projeto

### 1. Clonar o Repositório

Primeiro, clone o repositório para o seu computador. Abra o terminal e execute o seguinte comando:

```bash
git clone https://github.com/BrunaCardoso7/gestao_de_pedidos_Django_apiRest.git
```


### 2. Acessar o Diretório do Projeto

Após clonar o repositório, entre no diretório do projeto:

```bash
cd gestao_de_pedidos_Django_apiRest
```



### 3. Criar e Ativar Ambiente Virtual

- Criar Ambiente Virtual
  
```bash
python3 -m venv venv
```

- Ativar Ambiente Virtual
  
No Linux🐧:

```bash
source venv/bin/activate
```
No Windows:

```bash
.\venv\Scripts\activate
```


### 4. Instalar as Dependências

Agora que o ambiente virtual está ativado, instale as dependências do projeto usando o pip. Execute:

```bash
pip install -r requirements.txt
```

### 5. Renomear arquivo

Renomeie o arquivo, .env.exmple para .env
  
No Linux🐧:

```bash
mv .env.example .env
```
No Windows:

```bash
ren .env.example .env
```

### 6. Configuração de Banco de Dados 

```bash
python manage.py migrate
```



### 7. Executar o Projeto

Após as dependências estarem instaladas, você pode rodar o servidor com o seguinte comando:
```bash
python manage.py runserver
```




### 8. Testar o Projeto

execute-os para garantir que tudo esteja funcionando corretamente:

os teste garante que o funcionamento das rotas e requisitos solicitados estejam funcionando

```bash
python manage.py test
```


