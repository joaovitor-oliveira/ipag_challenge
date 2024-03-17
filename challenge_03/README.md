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

Além disso, é perceptível a **facilidade** de adição de uma nova forma geométrica e a sua utilização na classe `main.py`;

Por fim, o código foi pensado de forma a não possuir diversos `Ifs` ou `switch case` e é perceptível a facilidade de adição de uma nova forma geométrica e a sua utilização na classe `main.py`;


## Como executar

TODO