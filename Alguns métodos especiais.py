class Numero:
    def __init__(self, valor):
        self.valor = valor
    # Este é o método inicializador (construtor) da classe.
    # Ele é chamado quando um novo objeto da classe é criado.

    def __add__(self, outro):
        return Numero(self.valor + outro.valor)
    # Este método define o comportamento do operador de adição '+' para a classe.

    def __sub__(self, outro):
        return Numero(self.valor - outro.valor)
    # Este método define o comportamento do operador de subtração '-' para a classe

    def __eq__(self, outro):
        return self.valor == outro.valor
    # Este método define o comportamento do operador de igualdade '==' para a classe.

    def __lt__(self, outro):
        return self.valor < outro.valor
    # Este método define o comportamento do operador de comparação '<' (menor que) para a classe. 
    # Se a comparação for verdadeira, retorna 'True', se for falsa, retorna 'False'.

    def __len__(self):
        return len(str(self.valor))
    # Este método define o comportamento da função len() para a classe.
    # Neste caso, ele retorna o comprimento (número de dígitos) do valor do objeto 'Numero'.

    def __str__(self):
        return str(self.valor)
    # Este método define o comportamento da função str() para a classe.
    # Ele retorna a representação em string do objeto Numero.

# Testando a classe Numero
num1 = Numero(10)
num2 = Numero(20)

print(f"Soma: {num1 + num2}")   # Resultado: Soma: 30
print(f"Subtração: {num1 - num2}")  # Resultado: Subtração: -10
print(f"Igual: {num1 == num2}")  # Resultado: Igual: False
print(f"Menor: {num1 < num2}")   # Resultado: Menor: True
print(f"Tamanho: {len(num1)}")   # Resultado: Tamanho: 2
print(f"String: {num1}")         # Resultado: String: 10
