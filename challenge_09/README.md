## Exercício 09

## 9. Simulador de Financiamento:

Crie um programa que simule o calculo de financiamento de um imóvel ou veículo, baseado na tabela PRICE.

O programa deve solicitar o valor total do financiamento, a quantidade de parcelas e a taxa nominal de juros anual.

O programa deve exibir o valor da parcela, o valor total a ser pago, o custo efetivo total do financiamento e a taxa efetiva mensal.

O programa deve permitir a simulação de diferentes cenários de financiamento.


## :spiral_notepad: NOTAS

Para este exercício, foram tomados cuidados específicos com as classes, de modo que o método **Price** (e futuros métodos) implemente a interface `FinancingMethod`, e a classe `Financing` receba uma instância dessa interface como injeção de dependência. Isso possibilita a criação de outros métodos de financiamento, como o **SAC**, por exemplo, e sua injeção na classe `Financing` para serem utilizados.

A classe possui fácil manutenção e baixo acoplamento devido à inversão de controle e à injeção de dependência.

Além disso, no resultado final, foi adicionada uma tabela de parcelas mensais junto aos cálculos dos juros, da amortização e do saldo devedor.

Decidi manter os parâmetros idênticos aos da fórmula informada, pensando no desenvolvimento orientado ao domínio. Neste exemplo, considerei um contexto em que as pessoas que utilizarão a classe estão familiarizadas com as abreviações das fórmulas. No entanto, a classe está bem documentada, descrevendo cada um dos parâmetros, bem como as funcionalidades dos métodos da classe.


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