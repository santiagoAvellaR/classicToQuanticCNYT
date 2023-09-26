# En esta librería se encuentra las funciones de los diferentes sistemas, tanto deterministicos como probabilisticos
# ademas del experimento de la doble rendija
import matrxVectorsLibrary as mv
import matplotlib.pyplot as plt
import complexNumbersLibrary as cn
import math

def marbleSimulation(Dynamics, iniState, clicks, numb):
    finState = iniState
    for i in range(clicks):
        finState = mv.accMtrxVect(Dynamics, finState)
    categorias = [str(j) for j in range(len(iniState))]
    valores = [0 for i in range(len(finState))]
    for i in range(len(finState)):
        valores[i] = finState[i][0][0]
    fig, ax = plt.subplots()
    ax.bar(categorias, valores)
    ax.set_xlabel('Cajas')
    ax.set_ylabel('Canicas')
    ax.set_title('Marble Simulation ' + str(numb))
    plt.savefig('graficoMarbleSimulation' + str(numb) + '.png')
    plt.show()
    return finState

def dobleRendijaSimulationReals(Dynamics, numb):
    finalState = [[(1,0)]] + [[(0,0)] for i in range(len(Dynamics[0])-1)]
    for i in range(2):
        finalState = mv.accMtrxVect(Dynamics, finalState)
    categorias = [str(j) for j in range(len(Dynamics[0]))]
    valores = [0 for i in range(len(finalState))]
    for i in range(len(finalState)):
        valores[i] = finalState[i][0][0]
    fig, ax = plt.subplots()
    ax.bar(categorias, valores)
    ax.set_xlabel('Estados')
    ax.set_ylabel('Cantidad de luz del foton inicial')
    ax.set_title('Sistema Doble Rendija Pesos Reales ' + str(numb))
    plt.savefig('graficoSistemaProbabilistico' + str(numb) +'.png')
    plt.show()
    return finalState

def dobleRendijaSimulationQuantum(Dynamics, numb):
    finalState = [[(1,0)]] + [[(0,0)] for i in range(len(Dynamics[0])-1)]
    for i in range(2):
        finalState = mv.accMtrxVect(Dynamics, finalState)
    category = [str(j) for j in range(len(Dynamics[0]))]
    values = [0 for m in range(len(finalState))]
    for k in range(len(finalState)):
        values[k] = cn.modCmplx(finalState[k][0])
    fig, ax = plt.subplots()
    ax.bar(category, values)
    ax.set_xlabel('Estados')
    ax.set_ylabel('Cantidad de luz del foton inicial')
    ax.set_title('Sistema Doble Rendija Pesos Cuanticos ' + str(numb))
    plt.savefig('graficoSistemaCuantico' + str(numb) + '.png')
    plt.show()
    return finalState

def graphicState():
    # Datos
    categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4']
    valores = [10, 15, 7, 12]
    # Crear un objeto figura y un eje (axis)
    fig, ax = plt.subplots()
    # Crear el diagrama de barras
    ax.bar(categorias, valores)
    # Personalizar el gráfico
    ax.set_xlabel('Categorías')
    ax.set_ylabel('Valores')
    ax.set_title('Diagrama de Barras Simple')
    # Guardar el gráfico como una imagen (por ejemplo, en formato PNG)
    plt.savefig('grafico_de_barras.png')
    # Mostrar el gráfico en pantalla
    plt.show()



def casosPrueba():
    print(marbleSimulation([[(1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                                   [(0,0),(1,0),(0,0),(0,0),(1,0),(0,0)], [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                                   [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)], [(0,0),(0,0),(1,0),(0,0),(0,0),(1,0)]],
                                  [[(2,0)],[(3,0)],[(0,0)],[(2,0)],[(4,0)],[(1,0)]], 2,1))
    print(marbleSimulation([[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                                   [(0,0),(1,0),(0,0),(0,0),(0,0),(1,0)], [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
                                   [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)], [(1,0),(0,0),(0,0),(0,0),(1,0),(0,0)]],
                           [[(6,0)],[(2,0)],[(1,0)],[(5,0)],[(3,0)],[(10,0)]],4,2))

    print(dobleRendijaSimulationReals([[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(1/2,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                                    [(1/2,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(1/3,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
                                    [(0,0),(1/3,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],[(0,0),(1/3,0),(1/3,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
                                    [(0,0),(0,0),(1/3,0),(0,0),(0,0),(0,0),(1,0),(0,0)],[(0,0),(0,0),(1/3,0),(0,0),(0,0),(0,0),(0,0),(1,0)]],1))

    print(dobleRendijaSimulationReals([[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(1/6,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                [(2/3,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(1/6,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                [(0,0),(1/10,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)], [(0,0),(7/10,0),(0,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                [(0,0),(2/10,0),(1/10,0),(0,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(0,0),(4/5,0),(0,0),(0,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
                [(0,0),(0,0),(1/10,0),(2/7,0),(0,0),(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)], [(0,0),(0,0),(0,0),(4/7,0),(0,0),(0,0),(0,0),(0,0),(0,0),(1,0),(0,0)],
                [(0,0),(0,0),(0,0),(1/7,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(1,0)]],2))

    print(dobleRendijaSimulationQuantum([[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(1/math.sqrt(2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                                    [(1/math.sqrt(2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(-1/math.sqrt(6),1/math.sqrt(6)),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
                                    [(0,0),(-1/math.sqrt(6),-1/math.sqrt(6)),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],[(0,0),(1/math.sqrt(6),-1/math.sqrt(6)),(-1/math.sqrt(6),1/math.sqrt(6)),(0,0),(0,0),(1,0),(0,0),(0,0)],
                                    [(0,0),(0,0),(-1/math.sqrt(6),-1/math.sqrt(6)),(0,0),(0,0),(0,0),(1,0),(0,0)],[(0,0),(0,0),(1/math.sqrt(6),-1/math.sqrt(6)),(0,0),(0,0),(0,0),(0,0),(1,0)]],1))

    print(dobleRendijaSimulationQuantum([[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)], [(0,1/math.sqrt(2)),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                  [(0,1/math.sqrt(2)),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)], [(0,0),(0,-1/math.sqrt(3)), (0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
                  [(0,0),(0,1/math.sqrt(3)), (0,0),(0,0),(1,0),(0,0),(0,0),(0,0)], [(0,0),(0,-1/math.sqrt(3)), (0,-1/math.sqrt(3)),(0,0),(0,0),(1,0),(0,0),(0,0)],
                  [(0,0),(0,0), (0,1/math.sqrt(3)),(0,0),(0,0),(0,0),(1,0),(0,0)], [(0,0),(0,0), (0,-1/math.sqrt(3)),(0,0),(0,0),(0,0),(0,0),(1,0)]],2))