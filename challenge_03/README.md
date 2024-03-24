## Exercício 03

## 3. Área de Formas Geométricas:

Crie um programa que seja capaz de calcular a área de formas geométricas.

O programa deve permitir o cálculo da área de um quadrado, retângulo, triângulo e círculo.

O usuário deve escolher a forma geométrica e informar os dados necessários para o cálculo da área.


## :spiral_notepad: NOTAS

A solução foi pensada e feita utilizando **POO** e com a utilização dos métodos de forma estática, ou seja, não é necessários instanciar o objeto. 

A classe `Shape` é a abstração de uma forma geométrica, todas as outras devem herdar deste tipo.

Decidi deixar a validação dentro do método calcular área pois tais métodos são estáticos e, portanto, teria que utilizar o método de validação no arquivo `main.py`. Uma **solução** para a situação é:

- Os métodos serem métodos de instância;
- A validação seria no construtor partindo do princípio do DDD de que se os parâmetros de criação do objeto não forem válidos tal objeto nem deve ser criado;
- Por fim, seria só criar a instancia do objeto e chamar seu método de calcular área.

O código foi pensado de forma a não possuir diversos `Ifs` ou `switch case` e é perceptível a **facilidade** de adição de uma nova forma geométrica e a sua utilização na classe `main.py`;


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
python -m challenge_03.src.main
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
python -m challenge_03.src.main
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