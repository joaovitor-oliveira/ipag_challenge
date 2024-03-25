## Exercício 02

 ## 2. Maior e Menor entre Três Números:

Escreva um programa que peça ao usuário três números.

Determine o maior e o menor número entre os três e exiba-os na tela.

## :spiral_notepad: NOTAS

A solução é trivial. A simples comparação entre os três elementos retorna a solução desejada.

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
python -m challenge_02.src.main
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
python -m challenge_02.src.main
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