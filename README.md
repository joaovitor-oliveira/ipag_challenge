# Desafio iPag - Desenvolvedor(a) Júnior


## Como este projeto está organizado

- Este desafio possui 10 exercícios de programação, as soluções para os exercícios serão através de um Pull Request e compiladas na branch `develop`.

- Cada desafio possui sua pasta, exemplo: **challenge_01**. Dentro da pasta do desafio haverão outra duas, compostas por `src` e `tests`.

- Os Pull Requests possuem um fluxo de **CI** via `Github Actions` para validação de **linter**, **testes** e qualidade de código via **SonarCloud**;

- As soluções para os exercícios foram feitas em **Python** e funcionam a partir da versão 3.9.6;

- É possível executar tanto em ambiente local quanto no docker. As intruções estarão logo abaixo mas também estão presentes no readme de todos os exercícios.

### GOSTARIA QUE O CÓDIGO FOSSE ANALISADO CUIDADOSAMENTE VISANDO SUA QUALIDADE, MANUTENIBILIDADE E AS IDEIAS DAS SOLUÇÕES PROPOSTAS

### TODOS OS EXERCÍCIOS POSSUEM TESTES


Feedbacks são muito bem-vindos e serão bem apreciados!


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