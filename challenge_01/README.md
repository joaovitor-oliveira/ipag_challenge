## Exercício 01

## 1. Calculadora Básica:

Crie uma calculadora que realize as operações básicas: soma, subtração, multiplicação e divisão.

Permita a entrada de dois números e a escolha da operação.

Exiba o resultado da operação na tela.


## :spiral_notepad: NOTAS

A solução está escrita de tal forma que **facilita** a adição de novos métodos de cálculo.

Por exemplo: caso queira adicionar uma operação de exponenciação é necessário apenas construir uma nova função e adicionar em `operations`.


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
python -m challenge_01.src.main
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
python -m challenge_01.src.main
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