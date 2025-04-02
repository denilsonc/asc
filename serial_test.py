"""
Exemplo de uso da classe serial_lib.py
Desenvolvido por: Adalberto Oliveira
Fainor - Curso de Engenharia de Computação
Processamento Digital de Sinais
Outubro de 2024
"""


import time
import random
from serial_lib import SerialCommunication
from processamento_lib import Processamento




# iniciar o grafico 
import matplotlib.pyplot as plt
r = plt.ion()
data = [0] * 100





# Defining serial port info
port = "COM6"
baud_rate = 9600

serial = SerialCommunication(port=port, 
                          baud_rate=baud_rate, 
                          data_length=1, 
                          health_test=True, timeout=0.1)
serial.start()


pds = Processamento(vin=12, tensao_base=4.682)


tick = time.time()
while True:

    if (time.time() - tick) > 0.001:

        tick = time.time()

        # Reading serial port
        serial_data = serial.get_data()
        # serial_data = [random.randint(500, 1023)]
        

        if serial_data:
            valor = serial_data[0]
            tensao = pds.tensao(valor)
            print(f"Amostra: {round(pds.amostra,2)} Tensao: {round(tensao,2)}",end="\r")
            
            

            # atualizar o grafico 
            data.append(tensao)
            data = data[-100:]
            plt.plot(data)
            plt.draw()
            plt.pause(0.0001)
            plt.clf()