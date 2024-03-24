## Exercício 10

## 10. Manipulação de API:

Utilizando a API REST do GitHub, desenvolva um script que faça uma requisição para obter os repositórios de um usuário e exiba as informações na tela.

O usuário deve informar o nome do usuário do GitHub.

O script deve exibir o nome, descrição, linguagem e quantidade de estrelas de cada repositório.


## :spiral_notepad: NOTAS

A solução para a criação do script para buscar repositórios no github é bem simples. O **endpoint** da api pública do github utilizado **não** precisa de autenticação. No entanto, **há um limite de 60 requisições/hora**, mas acredito ser suficiente para esse exercício.


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
python -m challenge_10.src.main
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
python -m challenge_10.src.main
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