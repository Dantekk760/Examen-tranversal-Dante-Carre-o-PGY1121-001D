def comprar_entradas(ubicaciones_disponibles, precios):
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (1-3): "))
    while cantidad < 1 or cantidad > 3:
        print("Cantidad inválida. Intente nuevamente.")
        cantidad = int(input("Ingrese la cantidad de entradas a comprar (1-3): "))

    print("Ubicaciones disponibles:")
    for i in range(len(ubicaciones_disponibles)):
        if ubicaciones_disponibles[i] == "X":
            print("Ubicación", i + 1, " - No está disponible")
        else:
            print("Ubicación", i + 1)

    entradas_compradas = []
    contador_entradas = 0
    for _ in range(cantidad):
        ubicacion = int(input("Ingrese el número de la ubicación deseada: "))
        while ubicaciones_disponibles[ubicacion - 1] == "X":
            print("Ubicación no disponible. Intente nuevamente.")
            ubicacion = int(input("Ingrese el número de la ubicación deseada: "))

        entradas_compradas.append(ubicacion)
        ubicaciones_disponibles[ubicacion - 1] = "X"
        contador_entradas += 1

    total_pagar = 0
    for ubicacion in entradas_compradas:
        if ubicacion <= 20:
            total_pagar += precios["Platinum"]
        elif ubicacion <= 50:
            total_pagar += precios["Gold"]
        else:
            total_pagar += precios["Silver"]

    print("Operación realizada correctamente.")
    return total_pagar


def mostrar_ubicaciones(ubicaciones_disponibles):
    print("[          ESCENARIO         ]")
    for i in range(10):
        row = ""
        for j in range(10):
            ubicacion = i * 10 + j + 1
            if ubicaciones_disponibles[ubicacion - 1] == "X":
                row += "X".center(4)
            else:
                row += str(ubicacion).center(4)
        print(row)


def ver_listado_asistentes(asistentes):
    asistentes_ordenados = sorted(asistentes)
    print("Listado de asistentes:")
    for asistente in asistentes_ordenados:
        print(asistente)


def mostrar_ganancias(ventas, precios):
    print("Tipo Entrada    Cantidad    Total")
    total_ventas = 0
    for tipo, cantidad in ventas.items():
        precio = precios[tipo]
        total = precio * cantidad
        total_ventas += total
        print(f"{tipo:<15} {precio:>10,.0f} {cantidad:>10} {total:>10,.0f}")
    print("TOTAL", f"{sum(ventas.values()):>15} {total_ventas:>10,.0f}")


# Variables iniciales
ubicaciones_disponibles = [" "] * 100
precios = {
    "Platinum": 120000,
    "Gold": 80000,
    "Silver": 50000
}
asistentes = []
ventas = {
    "Platinum": 0,
    "Gold": 0,
    "Silver": 0
}

# Menú principal
while True:
    print("\n----- Menú -----")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        total_pagar = comprar_entradas(ubicaciones_disponibles, precios)
        contador_entradas = 0
        for _ in range(total_pagar):
            if contador_entradas >= 3:
                break
            run = input("Ingrese el RUN del asistente (sin guiones ni puntos): ")
            asistentes.append(run)
            if contador_entradas < 20:
                ventas["Platinum"] += 1
            elif contador_entradas < 50:
                ventas["Gold"] += 1
            else:
                ventas["Silver"] += 1
            contador_entradas += 1

    elif opcion == "2":
        mostrar_ubicaciones(ubicaciones_disponibles)

    elif opcion == "3":
        ver_listado_asistentes(asistentes)

    elif opcion == "4":
        mostrar_ganancias(ventas, precios)

    elif opcion == "5":
        import datetime
        fecha_actual = datetime.date.today().strftime("%d/%m/%Y")
        print("Saliendo del sistema...")
        print("Nombre: [Tu nombre]")
        print("Apellido: [Tu apellido]")
        print("Fecha actual:", fecha_actual)
        break

    else:
        print("Opción inválida. Intente nuevamente.")