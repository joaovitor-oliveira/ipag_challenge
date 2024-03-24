## Exercício 05

## 5. Validador de Senha:

Escreva um programa que peça ao usuário uma senha.

A senha deve ter no mínimo 8 caracteres e conter pelo menos uma letra maiúscula, uma letra minúscula e um número.

Valide a senha e informe ao usuário se ela é válida ou não.


## :spiral_notepad: NOTAS

A solução foi pensada e desenvolvida com base no `Notification Pattern`, cujo princípio é retornar **todos** os erros de validação de uma vez, em vez de apresentar apenas um *único* erro e permitir que o usuário continue cometendo erros até passar por todas as condições. Essa abordagem adaptativa mostrou-se eficaz para resolver o problema atual e oferece oportunidades para futuras melhorias.

A inclusão de novas condições pode ser facilmente realizada, e alterações podem ser feitas por meio de um dicionário de condições, permitindo adaptações ao método `validate` sem que ele se torne excessivamente extenso, garantindo assim uma manutenção mais simples.

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
python -m challenge_05.src.main
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
python -m challenge_05.src.main
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