## Exercício 09

## 9. Simulador de Financiamento:

Crie um programa que simule o calculo de financiamento de um imóvel ou veículo, baseado na tabela PRICE.

O programa deve solicitar o valor total do financiamento, a quantidade de parcelas e a taxa nominal de juros anual.

O programa deve exibir o valor da parcela, o valor total a ser pago, o custo efetivo total do financiamento e a taxa efetiva mensal.

O programa deve permitir a simulação de diferentes cenários de financiamento.


## :spiral_notepad: NOTAS

Para esse exercício foi tomado um cuidado com as classes de forma que o método **Price** (e futuros métodos) implementem a interface `FincancingMethod`, e a classe `Financing` recebe uma instância dessa interface como injeção de dependência. Dessa forma, é possível criar um outro método de financiamento como o Sac, por exemplo, e injetar na classe Financing para que o mesmo seja utilizado.

A classe possui fácil manutenibilidade e baixo acoplamento por conta da inversão de controle somada a injeção de dependência.

Além disso, no resultado final foi adicionado a tabela de parcelas mensais junto aos calculos do juros, da amortização e saldo devedor.

Decidi manter os parâmetros idênticos aos da fórmula informada pensando em desenvolvimento orientado ao domínio. Neste exemplo, considerei um contexto onde as pessoas que utilizarão a classe têm como linguagem padrão as abreviações das fórmulas. No entanto, a classe está bem documentada descrevendo cada um dos parâmtros bem como as funcionalidades dos métodos da classe. 


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
python -m challenge_09.src.main
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
python -m challenge_09.src.main
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