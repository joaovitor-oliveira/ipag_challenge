## Exercício 06

## 6. Lista de Tarefas:

Crie um programa que permita ao usuário adicionar, remover e visualizar tarefas.

Cada tarefa deve ter descrição, prioridade e um status (pendente ou concluída).

O programa deve permitir a navegação, ordenação e edição da lista de tarefas.


## :spiral_notepad: NOTAS

A solução foi pensada e projetada em POO e a sua execução está no arquivo `main.py`.

A cada inserção, alteração ou conclusão de tarefas, a lista é ordenada baseada no status de conclusão e na prioridade. De qualquer forma, decidi deixar a opção no menu para que fique explícito que há essa funcionalidade.

:warning: A cobertura de testes está reduzida nesse exercício pois o coverage não está excluindo o arquivo `main.py`, este que por sua vez possui métodos de interface com o usuário. Além disso, os prints da inferface com o usuário gerou 04 code smells no código, por conta de sua duplicidade.

**No mais, os testes das classes Task e TaskList estão com alta cobertura.**

