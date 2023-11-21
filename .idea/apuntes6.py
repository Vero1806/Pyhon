def operar (n1,n2,operador): #funcion con def

    if operador == "+":
        return n1+n2
    elif operador == "-":
        return n1-n2
    else:
        return "Error"

print(operar(4,6, "+"))

def operar (n1,n2,operador = "+"): #parametro por defecto si no meto ninguno se queda, si meto uno se machaca
    if operador == "+":
        return n1+n2
    elif operador == "-":
        return n1-n2
    else:
        return "Error"

print(operar(4,6, "-"))

def operar (n1,n2,*,operador = "+"): #despues del * los argumentos se combiente en claves y los anteriores posicionales
    if operador == "+":
        return n1+n2
    elif operador == "-":
        return n1-n2
    else:
        return "Error"

print(operar(4,6, operador = "-"))

def sumar (n, *args): #args lista de argumentos. **kwargs es lista de claves
    resultado = n
    for i in args:
        resultado +=i

    return resultado

print(sumar(3,4,5,6,7,8,9))