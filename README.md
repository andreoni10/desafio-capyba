# Desafio-capyba

API construida em Python/Django para o desafio-capyba. A API consiste em um CRUD da entidade Filme,
ou seja, é possível criar, atualizar, deletar e ler os dados de um filme. 

## Como instalar

- Clone o repositório
- Acesse o diretório desafio-capyba e rode o seguinte comando:
```
python manage.py runserver
```

## Rotas
1. /film (GET): Responsável por obter os dados dos filmes já cadastrados
    - Parâmetros:
        - page_number: Número da página
        - page_size: Número de filmes por página
        - name: Filtrar filme pelo nome
        - order_by: Ordenar filmes por nome ('film_name') ou data de lançamento ('film_release')

2. /film (POST): Responsável por adicionar um novo filme
    ```
    {
        film_name: "Titanic"
        film_genre: "Drama"
        filme_release: 1997
    }
    ```

3. /update-film/{film_id} (PATCH): Responsável por atualizar um filme

4. /update-film/{film_id} (DELETE): Responsável por excluir um filme