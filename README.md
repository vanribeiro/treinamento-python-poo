# Treinamento - Python Orientado a Objetos 

Treinamento oferecido pela Avanade nos dias 05/06 a 06/06/2023.

## Anotações - Dia 06/06/2023

### `*args` e `**kwargs`

Retorna array com os itens passados pelo objeto inicializado:

```python
# definição da classe
class Pessoa:
    def __init__(self, *args) -> None:
        self.nome = args[0]
        self.idade = args[1]

# classe instancia
pessoa = Pessoa("Carlos", 18)
```

Retorna um argumento do tipo chave e valor:

```python
# definição da classe
class Pessoa:
    def __init__(self, nome, idade, *kwargs) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = kwargs['sexo']

# classe instancia
pessoa = Pessoa("Carlos", 18, sexo='M')
```

### dunders

#### `__init__`

É um inicializador, que lembra muito um método construtor e é onde serão inicializadas os atributos durante as instância da classe.

```python
class Pessoa:
    def __init__(self, *args) -> None:
        ...
```

- é chamado depois que a instância da classe é criada
- o retorno deve ser none

`Pessoa.__new__() -> super().__new__(cls) -> Pessoa.__init__()`

#### `__new__`

Esse é o construtor de fato. Ele chamado de forma implícita, sempre que uma instância é criada e raramente é chamado explicitamente como em outras linguagens.

```python

class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'criado'):
            cls.criado = super().__new__(cls)
        return cls.criado

```

- é um método estático, mas não precisa ser marcado com decorator
- o retorno deve ser a nova instância de objeto(geralmente instância de cls)

#### `__del__`

É um finalizador. É chamado quando a instância está prestes a ser destruída.

- é usada é casos bem específicos, no encerramento de conexões com banco de dados, por exemplo.

#### `__str__`

Calcula a representação de string informal ou muito bem imprimível de um objeto. 

```python
class Pessoa:
    def __init__(self, *args) -> None:
        self.nome = args[0]
        self.idade = args[1]

    def __str__(self) -> str:
        return f"Pessoa{self.nome, self.idade}"
```

- retorno deve ser um objeto de string

#### `__len__`

Retorna o tamanho de uma lista:

```python

frutas = ["caqui", "goiaba", "manga", "caqui"]
quantidade_de_frutas = len(frutas)
print(quantidade_de_frutas)

```

#### `__contains__`

Verifica se um item existe ou não na lista:

```python
print("Tem manga?", cesta_de_frutas.__contains__("manga"))
print("Tem maçã?", cesta_de_frutas.__contains__("maçã"))
```