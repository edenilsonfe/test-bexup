
## Requisitos

* Docker
* Docker-compose

## Como rodar

1. Clone o repositório:

   ```
   git clone https://github.com/edenilsonfe/test-bexup
   ```

2. Entre no diretório do projeto:

   ```
   cd test-bexup
   ```

3. Inicie os containers:

   ```
   docker-compose up -d
   ```

6. Para parar a aplicação, execute:

   ```
   docker-compose down
   ```

## Requests usando insomnia

disponibilizo um [Arquivo .json](insomnia.json) para ser importado no insomnia para que possam ser feitas as requests.

### ordem de execução

1. Load data from API1 to API2

```
Esse endpoint irá fazer uma requisição para a API Externa(https://deividfortuna.github.io/fipe/) para buscar a lista de marcas de carros e enviar para uma fila do RabbitMQ. Após enviar o item para a fila do RabbitMQ, a API2 irá receber esse objeto referente à marca e irá fazer uma nova requisição para buscas os modelos referentes a essa marca. Após a busca pelos modelos, os dados serão salvos no banco de dados mongodb com o seguinte formato:
{
    codigo: "1",
    nome: "Test",
    modelos: [{}]
}
```

2. Get all brands from db

```
Esse endpoint irá fazer uma requisição para o banco de dados para retornar todas as Marcas contendo os respectivos modelos processados pela API2
```

3. Get vehicle by BrandId

```
Esse endpoint irá fazer uma requisição para o banco de dados para retornar um veículo a partir de um id de marca. Por ex: brand_id = 59
```

## Configurações

As portas padrões podem ser alteradas no arquivo Docker-compose na raiz do projeto.
