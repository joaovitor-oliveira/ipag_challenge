# Desafio iPag - Desenvolvedor(a) Júnior


## Organização do Projeto

Este desafio consiste em 10 exercícios de programação, cujas soluções serão submetidas por meio de Pull Requests e compiladas na branch `develop`.

Cada exercício possui sua própria pasta, por exemplo: `challenge_01`. Dentro de cada pasta de exercício, há duas subpastas, chamadas `src` e `tests`.

Os Pull Requests seguem um fluxo de **CI** (Continuous Integration) via Github Actions para validação de linting, testes e qualidade de código através do **SonarCloud**.

As soluções para os exercícios foram implementadas em Python e são compatíveis com a versão 3.9.6 ou superior.

É possível executar as soluções tanto localmente quanto no `Docker`. As instruções estão disponíveis abaixo e também no README de cada exercício.

Gostaria que o código fosse analisado cuidadosamente, visando sua qualidade, manutenibilidade e as ideias das soluções propostas.

**Todos** os exercícios incluem testes automatizados.

Feedbacks são muito bem-vindos e serão apreciados!

**Estou disponível para conversarmos sobre as soluções.**


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
python -m challenge_n.src.main
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
python -m challenge_n.src.main
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