## Exercício 07

## 7. Manipulação e Comunicação de Objetos:

Crie um programa que conecte controles de marcas diferentes (LG, Samsung, Sony, etc) a uma ou mais TVs.

O programa deve permitir a seleção de um controle e a comunicação com a TV para ligar e desligar;

As TVs e controles devem ser representados por objetos, e a comunicação entre eles deve ser feita por métodos.

O programa deve exibir na tela as ações realizadas e o estado atual da TV.

Caso o controle selecionado não seja compatível com a TV, o programa deve exibir uma mensagem de erro.


## :spiral_notepad: NOTAS

A solução foi pensada tendo como base o `Design Pattern` **Bridge**.

As interfaces do Controle e da TV são descritas dessa forma pois não há uma interface oficial no python. Além disso, cada controle e cada tv possuem uma implementação para si pois podem haver especializações específicas de cada um.

Apesar de utilizar o controle injetando a dependência de uma TV, é possível adaptar para que a sua utilização possa vir atrelada a um método `attach` com o objetivo de sincronizar uma TV ao controle alvo. Dessa forma, o controle pode passar a _existir_ sem estar composto por uma tv.


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
python -m challenge_07.src.main
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
python -m challenge_07.src.main
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