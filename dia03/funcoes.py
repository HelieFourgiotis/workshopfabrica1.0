def soma(x: int | float, y: int | float) -> int | float:
    """Soma x + y e retorna o resultado""" 
    #resultado = x + y
    return x + y
#def é utilizado para criar função
def print_subtracao(x: int | float, y: int | float) -> None:
    """soma x = y e mostra resultado no print """
    print(f"resultado: {x - y}")
    
    
def soma_sem_parametro() -> int | float:
    x = 5
    y = 5
    return x + y



a = soma(1, 2)

