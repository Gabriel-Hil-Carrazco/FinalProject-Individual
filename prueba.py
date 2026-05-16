'''
Se necesita llevar el registro de pacientes de un consultorio odontológico.
Cada paciente se representa como un nodo en una lista enlazada, donde cada 
nodo contiene información sobre el paciente, como el nombre, dni y obra social. 
Se debe poder agregar pacientes al registro y luego listarlos. 
Se debería poder agregar pacientes al registro, buscar un paciente por dni 
y listar los pacientes del consultorio.

'''
class Paciente:
    def __init__(self, nombre, dni, obraSocial):
        self.nombre = str(nombre)
        self.dni = int(dni)
        self.obraSocial = str(obraSocial)
        self.next = None

class ListaPacientes:
    def __init__(self):
        self.head = None
    

    def insert(self, new_node): 
        if self.head:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
            last_node.next = new_node
        else:
            self.head = new_node


    def display(self): 
        temp_node = self.head 
        while temp_node != None: 
            print(temp_node.data, end='->')
            temp_node = temp_node.next
        print('Null')

    def get_pos(self, pos): 
        temp_node = self.head 
        counter = 0
        while temp_node != None: 
            if counter == pos: 
                return temp_node 
            counter += 1
            temp_node = temp_node.next
        raise Exception("Lista vacía o fuera de rango")



consultorio = ListaPacientes()

while True:
    print('             -- CONSULTORIO ODONTOLÓGICO --\n')
    print('      ¬ Seleccione la operación a realizar:\n')
    print('> (1) Ingresar Paciente')
    print('> (2) Ver lista de Pacientes')
    print('> (3) Buscar Paciente')
    print('> (4) Salir del programa...\n')
    
    operacion = int(input('[Operación] > '))
    
    if operacion == 4:
        break
    
    elif operacion == 1:
        nombre = input('Nombre: ')
        dni = int(input('DNI :'))
        obraSocial = input('Obra Social: ')
        paciente = Paciente(nombre, dni, obraSocial)
        consultorio.insert(paciente)
        print(f'Paciente {nombre} agregado...\n')
    
    elif operacion == 2:
        print('\n-- LISTA DE PACIENTES --')
        consultorio.display()
    
    elif operacion == 3:
        print('\n-- BUSCAR PACIENTE --')
        buscarDni = int(input('DNI a buscar: '))
        temp_node = consultorio.head
        while temp_node:
            if temp_node.dni == buscarDni:
                print(f'Encontrado: \n{temp_node.nombre}\n{temp_node.dni}\n{temp_node.obraSocial}')
                break
            temp_node = temp_node.next
        else:
            print('Paciente no encontrado...')
    
    else:
        print('Ingresó un carácter Inválido...\n')