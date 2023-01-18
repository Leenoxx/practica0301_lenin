# Escribir dos funciones, una función que reciba un número
# entero positivo n y calcule el número de fibonacci asociado
# a ese número de manera recursiva y otra función que haga
# la misma operación pero con bucles.
import datetime


def fibonacci_rec(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci_rec(numero - 1) + fibonacci_rec(numero - 2)


def fibonacci_bucle(numero):
    n = 0
    m = 1
    for i in range(numero):
        c = n + m
        n = m
        m = c
    return n


start_time = datetime.datetime.now()
fibonacci_bucle(40)
end_time = datetime.datetime.now()
print(end_time - start_time)
