import threading
import time

tenedor_Array = [1,1,1,1,1]

class filosofos(threading.Thread):
    
    def __init__(self, tenedores, num_Filosofos):
        threading.Thread.__init__(self)
        tenedor_Array[num_Filosofos] = threading.BoundedSemaphore(1)
        
        self.tenedores = tenedores
        self.num_Filosofos = num_Filosofos
        self.dato_Temporal = (self.num_Filosofos + 1) % 5

    def run(self):
        while(True):
            print("Filosofo iniciando", self.num_Filosofos)
            time.sleep(2)
            print("Filosofo ", self.num_Filosofos, "Pasando Tenedor Del Lado Izquierdo")
            self.tenedores[self.num_Filosofos].acquire()
            time.sleep(2)
            print("Filosofo ", self.num_Filosofos, "Recoge Tenedor Del Lado Derecho")
            self.tenedores[self.dato_Temporal].release()
            time.sleep(2)
            print("Filosofo ", self.num_Filosofos, "Libre Derecho")
            self.tenedores[self.dato_Temporal].acquire()
            time.sleep(2)
            print("Filosofo ", self.num_Filosofos, "Libre Izquierdo")
            self.tenedores[self.num_Filosofos].release()
            time.sleep(2)

for i in range(5):
    total = filosofos(tenedor_Array, i)
    total.start()