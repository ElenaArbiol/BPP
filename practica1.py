import pandas as pd
import pylab as pl



#he impreso el fichero para ver informacion de su contenido, como columnas, sus delimitadores y los datos por columna que hay, así como el tipo de datos
#print(pd.read_csv("c:/Users/lito_/Documents/ELENA/MASTER PYTHON/6.Buenas prácticas de programación en Python/Lección 1. Control de errores, pruebas y validacion de datos/finanzas2020[1].csv"))
#listaerror=[]  la he utilizado para ver qué datos estaban "mal" introducidos
datos=[]

try:
    f=pd.read_csv("c:/Users/lito_/Documents/ELENA/MASTER PYTHON/6.Buenas prácticas de programación en Python/Lección 1. Control de errores, pruebas y validacion de datos/finanzas2020[1].csv", delimiter="\t") # 100 filas y una columna con separador \t
    if len(f.columns)!=12:
        raise NameError( "El fichero no tiene las 12 columnas referentes a los meses del año")
    for i in f.columns:
        lista=[]
        gastos=0 # suma de los gastos del mes
        ingresos=0 #suma de los ingresos del mes 
        if len(f[i])<100:
            raise NameError("el fichero contiene datos vacios")
        for j in range (100):
            try:
                int(f[i][j])
                lista.append(int(f[i][j]))
                
            except ValueError: # si el dato no es de tipo entero que lo sustituya por 0
                #listaerror.append((f[i][j],i,j))
                lista.append(0)
                pass
            if int(lista[j]) >0:
                ingresos=ingresos +int(lista[j])
            else:
                 gastos=gastos+int(lista[j])
        datos.append((i, ingresos, gastos,ingresos-gastos)) # creo una lista de listas con los datos: mes,ingresos,gastos y ahorro
    #print(datos)

except IOError:
    print(" el fichero no existe o no se puede abrir")

# vamos a sacar resultados solicitados
#¿Que mes ha gastado más?
maximo=0
mes=[]
for i in range (len(datos)):
    if datos[i][2]<maximo:
        maximo=datos[i][2]
        mes=datos[i][0]
print("el mes que más dinero se ha gastado es :" , mes)

#¿Que mes se ha ahorrado más?
for i in range (len(datos)):
    if datos[i][3]>maximo:
        maximo=datos[i][3]
        mes=datos[i][0]
print("el mes que más dinero se ha ahorrado es :",mes)
#media de gastos al año
gastosaño=0
for i in range (len(datos)):
    gastosaño=gastosaño+datos[i][2]
print("la media de gastos del año ha sido: ","{:,.2f}".format(-gastosaño/len(datos)),"€")
print("el gasto total a lo largo del año es :","{:,}".format( -gastosaño), "€")
#ingresos totales a lo largo del año
ingresos=0
for i in range(len(datos)):
    ingresos=ingresos+datos[i][1]
print("Los ingresos totales del año han sido:","{:,}".format( ingresos), "€")

# imprimir grafica de ingresos por meses 
x=[]
y=[]
for i in range (len(datos)):
    x.append(datos[i][0])
    y.append(datos[i][1])
#pl.plot(x,y,color="blue",linewidth=1.0, linestyle="-",label="ingresos")
#pl.legend(loc='upper right')
#pl.show()

pl.bar(x,y,edgecolor="blue")
for x, y in zip(x, y):
    pl.text(x, y,"{:,}".format(y),ha='center', va='bottom')
pl.ylabel("Ingresos")
pl.xlabel("Meses")
pl.title("Evolución de los ingresos totales por meses")
pl.show()




