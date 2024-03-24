## Exercício 08

## 8. Estatísticas de Vendas:

Leia o arquivo em anexo "sales.csv" que contém dados de vendas agrupados por tipo e país.

Crie um programa que calcule e exiba as seguintes estatísticas:

Vendas (total de unidades vendidas, total de receita, custo total, lucro total) por tipo de produto.

Vendas por tipo de produto e região.

Tipo de produto com maior receita de cada país.


## :spiral_notepad: NOTAS

Para esta solução foi utilizado o `pandas`, um famoso pacote Python utilizado para análise e manipulação de dados.

Como o arquivo é único e estático, a solução se tornou mais simples. Foi feita a criação de uma classe `Sales` com os métodos de estatísticas solicitados.


## Como executar

<details>
<summary><strong>Em ambiente local</strong></summary></br>

Crie o ambiente virtual (caso não tenha feito anteriormente)
```bash
python -m venv .venv
```

Ative o ambiente

**LINUX e OS X**
```bash
source .venv/bin/activate
```

**WINDOWS**
```bash
\.venv\Scripts\activate
```

Instale as dependências
```bash
python -m pip install -r dev-requirements.txt
```

**Na raiz do projeto**

Execute o script
```bash
python -m challenge_08.src.main
```

Execute os testes
```bash
python -m pytest -v
```

Execute a cobertura de testes
```bash
python -m pytest --cov
```
</details>

<details>
<summary><strong>Docker</strong></summary></br>

**Certifique-se de possuir o docker e docker-compose instalados na sua máquina e com seus respectivos serviços ativados**

Criando container
```bash
docker-compose up -d
```

Acessando o container
```bash
docker exec -it python-environment bash
```

Execute o script
```bash
python -m challenge_08.src.main
```

Execute os testes
```bash
python -m pytest -v
```

Execute a cobertura de testes
```bash
python -m pytest --cov
```
</details>