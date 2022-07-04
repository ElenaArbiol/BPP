import pdb
pdb.set_trace()

# sacar el número máximo de cada lista que se encuentra en una lista 


def maximo_lista(l):
    maximo=[]
    for i in range(len(l)):
        maximo.append(max(l[i]))
    return maximo


# he hecho la misma operacion pero con comprensión de listas
def maximo_lista_1(l):
     maximos=[max(l[i]) for i in range(len(l))]
     return maximos


# numeros primos 

def es_primo(n):
    primo=True
    for i in range(2,n):
        if(n%i==0):
            primo=False
    return primo

def lista_primos(l):
    lista_primos=[]
    for i in range(len(l)):
       if es_primo(l[i]):
            lista_primos.append(l[i])
    return lista_primos

# listar primos con comprension listas
def lista_primos_2(l):
    primos2=[l[i] for i in range(len(l)) if es_primo(l[i])]
    return primos2

# listar los números primos usando la funcion filter

def lista_primos_1(l):
    primos1=list(filter(es_primo,l))
    return primos1


if __name__=='__main__':
    maximo_lista([[2,4,1],[1,2,3,4,5,6,7,8],[100,250,43]])
    maximo_lista_1([[2,4,1],[1,2,3,4,5,6,7,8],[100,250,43]])
    lista_primos([3,4,8,5,5,22,13])
    print(lista_primos_1([3,4,8,5,5,22,13]))
    print(lista_primos_2([3,4,8,5,5,22,13]))