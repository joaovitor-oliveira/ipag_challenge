## Exercício 04

## 4. Jogo da Adivinhação:

Crie um programa que gere um número aleatório entre 1 e 100.

O usuário deve tentar adivinhar o número com o mínimo de tentativas possível.

Dê dicas ao usuário, informando se o seu palpite está "acima", "abaixo" ou se ele adivinhou o número.


## :spiral_notepad: NOTAS

A solução é trivial. No entanto, foi tomado um cuidado com o **seed** da geração do número a ser adivinhado com o objetivo de que tal número seja `diferente` a cada execução do script.


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
python -m challenge_04.src.main
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
python -m challenge_04.src.main
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