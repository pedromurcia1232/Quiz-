# Intregrates: Pedro Murcia, Jonathan Buitrago, Sebastian Vega 
# Una empresa de CDA solicita un software en el cual se puedan ver el registros los clientes que han ingresado los datos a la empresa,
#agregar nuevos usuarios, Ver las leyes de trancito y los precios de tecnomecanica de cada tipo de vehiculo 
#

from PIL import Image

# Diccionario
leyes={"llantas":"La resolución 3768 de 2013 establece como base para los criterios de inspección y certificación de vehículos la norma técnica NTC 5375 de 2012, la cual define la profundidad mínima de labrado que deben tener las llantas para ser consideradas aptas para servicio",
       "luces":"La ley 769 de 2002, articulo 86 de las luces exteriores. Todo vehículo automotor deberá tener encendidas las luces exteriores a partir de las dieciocho (18) horas hasta las seis (6) horas del día siguiente, y cuando las condiciones de visibilidad sean adversas. Sin embargo, las autoridades de tránsito podrán fijar horarios de excepción.",
       "gases":"Resolución 005 de 1996, el Ministerio de Ambiente, Vivienda y Desarrollo Territorial considera necesario establecer normas de emisión para vehículos automotores activados con gasolina y diésel (ACPM), con el propósito de proteger el medio ambiente, los recursos naturalesrenovables y la salud de la población en genera.",
       "frenos":"Resolución 3752 de 2015, artículo 4, Es de obligatorio cumplimiento la utilizacióndel Sistema Antibloqueo de Frenos (ABS), paratodos los vehículos automotores, remolques y semirremolques de ensamble o fabricación nacional e importados, que se comercialicen en Colombia."}
#Tuplas
precios=("Para motocicletas, la tarifa máxima es de 218.251 pesos",
         " En el caso de automóviles y camionetas, el tope se sitúa en 327.219 pesos.",
         " Para los vehículos eléctricos, la tarifa máxima establecida es de 243.200 pesos.",
         "Para vehículo de carga a tarifa máxima establecida es de 427.099 pesos")
#Lista 
usuarios=[[],["Semana_1 Usuario: Jonathan Buitrago Cedula: 12112129 "],
          ["Semana_2 Usuario: Nicolas Rubio Codigo: 123123143  "],
          ["Semana_3 Usuario: Sebastian Vega Codigo: 72622513"],["Semana_4 Usuario: Pedro Murcia Codigo: 1002735859"]]

def ver_usuarios():
    print(usuarios)
    selec=int(input("¿Que semana desea ver? "))
    print(usuarios[selec])

    if selec== 1:
        imagen = Image.open('C:/Users/pmurc/OneDrive/Documentos/Linea de profundizacionIII/carro.jpg')


        imagen.show()
    elif selec==2:
        imagen2 = Image.open('C:/Users/pmurc/OneDrive/Documentos/Linea de profundizacionIII/rara.jpg')


        imagen2.show()
    elif selec ==3:
        imagen3 = Image.open('C:/Users/pmurc/OneDrive/Documentos/Linea de profundizacionIII/vega.jpg')
        imagen3.show()

    elif selec ==4:
        imagen4 = Image.open('C:/Users/pmurc/OneDrive/Documentos/Linea de profundizacionIII/gallo.jpg')
        imagen4.show()    
    elif selec ==5:
         imagen5 = Image.open('C:/Users/pmurc/OneDrive/Documentos/Linea de profundizacionIII/tonto.jpg')
         imagen5.show()   
     




def agregar_usuario():
    ingresar= input("Ingrese el nombre del usuario:  ").lower()
    cedula=input("Ingrese la cedula: ")
    usuarios.append(ingresar)
    usuarios.append(cedula)

def eliminar_usuario():
    usuario_eliminar = int(input("Ingrese la semana que desea eliminar: "))
    
    usuarios.pop(usuario_eliminar)
    print(f"El usuario '{usuario_eliminar}' ha sido eliminado de la lista.")
   

while True:
    print("\n1. Ver Usuario")
    print("2. Agregar usuario")
    print("3. Eliminar usuario")
    print("4. Consultar ley")
    print("5 Ver precios")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        ver_usuarios()
    elif opcion == '2':
        agregar_usuario()
        

    elif opcion == '3':
        eliminar_usuario()

    elif opcion == '4':

        print("llantas","luces","gases","frenos")
        ley=input("¿Sobre que parte del vehiculo quiere ver su ley?")
        print(leyes.get(ley,"No existe almacenada esta ley "))
  
    elif opcion== '5':
        print(precios)

    elif opcion == '6':
        print("Gracias por compartir con nosotros el mejor CDA pais vuelva pronto !")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")