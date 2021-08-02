import sqlite3
import numpy as np
import matplotlib.pyplot as plt


def fetch():
    conn = sqlite3.connect('heart.db')
    c = conn.cursor()
    c.execute('SELECT pulso FROM sensor')
    data = c.fetchall()
    conn.close()
    return data

def show(data):
    fig = plt.figure()
    fig.suptitle('EVOLUCION DEL RITMO CARDIACO',color="darkblue")
    ax = fig.add_subplot()
    ax.plot(data, color='lime')
    ax.set_facecolor('whitesmoke')
    ax.set_ylabel('Pulsaciones p/m', color= "darkblue")
    ax.set_xlabel('tiempo',color="darkblue")
    plt.show()

def estadisticas(data):
    valor_medio = np.mean(data)
    print('valor medio ', valor_medio)
    valor_minimo = np.min(data)
    print('valor minimo ', valor_minimo)
    valor_maximo = np.max(data)
    print('valor maximo ', valor_maximo)
    desvio_estandar = np.std(data)
    print('desviación estándar ', desvio_estandar)

def regiones(data):
    valor_medio = np.mean(data)
    desvio_estandar = np.std(data)

    x1 = [i for i in range(len(data)) if data[i] <= (valor_medio - desvio_estandar)]
    y1 = [data[i] for i in range(len(data)) if data[i] <= (valor_medio - desvio_estandar)]
    
    x2 = [i for i in range(len(data)) if data[i] >= (valor_medio + desvio_estandar)]
    y2 = [data[i] for i in range(len(data)) if data[i] >= (valor_medio + desvio_estandar)]

    x3 = [i for i in range(len(data)) if i not in x1 and i not in x2]
    y3 = [data[i] for i in range(len(data)) if data[i] not in y1 and data[i] not in y2]

    fig = plt.figure()
    fig.suptitle('REGIONES',color="darkblue")
    ax = fig.add_subplot()
    ax.scatter(x1, y1, c='darkblue', label='"Tranquilo"')
    ax.scatter(x2, y2, c='green', label='"Excitado"')
    ax.scatter(x3, y3, c='y', label='Estado normal')
    ax.set_facecolor('whitesmoke')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    
    data = fetch()
    
    show(data)
    
    estadisticas(data)

    regiones(data)