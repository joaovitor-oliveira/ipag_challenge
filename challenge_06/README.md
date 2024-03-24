## Exercício 06

## 6. Lista de Tarefas:

Crie um programa que permita ao usuário adicionar, remover e visualizar tarefas.

Cada tarefa deve ter descrição, prioridade e um status (pendente ou concluída).

O programa deve permitir a navegação, ordenação e edição da lista de tarefas.


## :spiral_notepad: NOTAS

A solução foi pensada e projetada em POO e a sua execução está no arquivo `main.py`.

A cada inserção, alteração ou conclusão de tarefas, a lista é ordenada baseada no status de conclusão e na prioridade. De qualquer forma, decidi deixar a opção no menu para que fique explícito que há essa funcionalidade.


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
python -m challenge_06.src.main
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
python -m challenge_06.src.main
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