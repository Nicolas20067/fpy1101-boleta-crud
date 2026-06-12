productos = []
opcion = ""

while opcion != "3":
    print("\n=== Supermerka2 ===")
    print("1. Agregar producto")
    print("2. Ver mis productos")
    print("3. modificar preoducto")
    print("4. eliminar preoducto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        while True:
           def agregar_producto(nombre, precio):
            producto = {"nombre": nombre, "precio": precio}
            boleta.append(producto)
            print(f"Producto ' {nombre} agregado correctamente")


            seguir = input("¿Quiere continuar? (s/n): ").lower()
            if seguir == "n":
                

    elif opcion == "2":
       def mostrar_boleta():
         if len(boleta) == 0:
            print("La boleta está vacía.")
    else:
        print("\n------ BOLETA ------")
        for producto in boleta:
            print(f"  {producto['nombre']}  -  ${producto['precio']}")
        print(f"  TOTAL: ${calcular_total()}")
        print("--------------------\n")


        if opcion == "3":
            def actualizar_precio(nombre, nuevo_precio):
                for producto in boleta:
                    if producto["nombre"] == nombre:
                      producto["precio"] = nuevo_precio
                    print(f"Precio de '{nombre}' actualizado a ${nuevo_precio}.")
                    return
                    print(f"Producto '{nombre}' no encontrado.")
