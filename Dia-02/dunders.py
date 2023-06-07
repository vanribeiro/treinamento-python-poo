# __new__ cria uma nova instância

class Nova:
    def __new__(cls):
        return super().__new__(cls)
    

nova = Nova()
print("Is a sub class?",issubclass(Nova, object))


class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'criado'):
            cls.criado = super().__new__(cls)
        return cls.criado