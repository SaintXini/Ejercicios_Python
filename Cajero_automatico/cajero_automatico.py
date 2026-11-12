print("Bienvenido al cajero automático")

saldo = 1000;
print(f"Su saldo es: {saldo}");

salir = False;

while not salir:
    print("Seleccione una opción:")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        print(f"Su saldo es: {saldo:.2f}")
    elif opcion == "2":
        monto = float(input("Ingrese el monto a retirar: "))
        if monto <= saldo:
            saldo -= monto
            print(f"Ha retirado {monto}. Su nuevo saldo es: {saldo}")
        else:
            print("Saldo insuficiente.")
    elif opcion == "3":
        monto = float(input("Ingrese el monto a depositar: "))
        saldo += monto
        print(f"Ha depositado {monto}. Su nuevo saldo es: {saldo:.2f}")
    elif opcion == "4":
        salir = True
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")