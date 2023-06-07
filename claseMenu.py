from claseManejador import ManejadorAgente
from claseNodo import Nodo
from clasePersonal import Personal
from claseApoyo import Apoyo
from claseDocente import Docente
from claseInvestigador import Investigador
from claseDocInv import DocenteInvestigador

class Menu:
    __cod: int
    
    def __init__(self):
        self.__cod = 0
    
    def mostrar_menu(self):
        print('')
        print('Opcion 1: Cargar Agentes del archivo')
        print('Opcion 2: Crear e insertar un agente a la coleccion')
        print('Opcion 3: Crear y agregar un agente al final de la coleccion')
        print('Opcion 4: Dada una posicion de la colección, mostrar que tipo de agente se encuentra')
        print('Opcion 5: Dada una carrera, mostrar un listado ordenado por nombre de todos los Docentes Investigadores')
        print('Opcion 6: Dada un area de investigacion mostrar cuantos son Investigadores y cuantos son Docentes Investigadores')
        print('Opcion 7: Mostrar Nombre, Apellido, tipo de agente y sueldo de todos los agentes ordenado por apellido')
        print('Opcion 8: Dada una categoria de Investigacion generar un listado')
        print('Opcion 9: Guardar la coleccion en el archivo "personal.json"')
        print('Opcion 0: Finalizar Operacion')
        print('')
        print('--------------------------------------------------------------------------------------------------------')
        
        
    def ejecutar_menu(self, MA:ManejadorAgente):
        self.mostrar_menu()
        self.__cod = int(input('Ingrese el Codigo'))
        while self.__cod != 0:
            if self.__cod == 1:
                MA.cargar()
            elif self.__cod == 2:
                unAgente = MA.crear_personal()
                MA.insertarElemento(unAgente)
            elif self.__cod == 3:
                unAgente = MA.crear_personal()
                MA.agregarElemento(unAgente)
            elif self.__cod == 4:
                MA.mostrar_tipo_posicion()
            elif self.__cod == 5:
                MA.generar_listado_carrera()
            elif self.__cod == 6:
                area = input("Ingrese un area de investigacion: ")
                MA.contar_area(area)
            elif self.__cod == 7:
                MA.listado_agentes()
            elif self.__cod == 8:
                MA.listar_segun_categoria()
            self.mostrar_menu()
            self.__cod = int(input('Ingrese el Codigo'))