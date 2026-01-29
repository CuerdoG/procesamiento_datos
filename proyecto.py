
import ipaddress

#1) leer fichero

def leer_fichero(ruta):
    lineas_validas = []

    try:
        with open(ruta, "r", encoding="utf-8") as fichero:
            linea = fichero.readline()

            while linea:
                linea = linea.strip()
                if linea and not linea.startswith("#"):
                    lineas_validas.append(linea)

                linea = fichero.readline()

    except FileNotFoundError:
        print(f"Ruta no encontrada: {ruta}")

    return lineas_validas

#2) normalizar lineas

def normalizar_linea(linea):
    for sep in [",", ";"]:
        linea = linea.replace(sep, "|")

    partes = [p.strip() for p in linea.split("|")]

    while len(partes) < 5:
        partes.append("")

    nombre, ip, sistema, ubicacion, responsable = partes[:5]

    sistema = sistema.lower()
    responsable = responsable.capitalize() if responsable else ""

    return {
        "nombre": nombre,
        "ip": ip,
        "sistema": sistema,
        "ubicacion": ubicacion,
        "responsable": responsable
    }

#3) validar datos

def validar_datos(d):
    #nombre obligatorio
    if not d["nombre"]:
        return False, "Nombre vacío"
    #validar ip
    if not d["ip"]:
        return False, "IP vacia"
    try:
        ipaddress.ip_address(d["ip"])
    except Exception:
        return False, f"IP invalida: {d['ip']}"
    #validar sistema operativo
    sistemas_validos={"linux","windows","macos"}
    if d["sistema"] not in sistemas_validos:
        return False, f"Sistema no valido: {d['sistema']}"
    #normalizar ubicacion
    if d["ubicacion"].strip()== "":
        d["ubicacion"]= None
    #normalizar responsable
    if d["responsable"] in ("","-"):
        d["responsable"] = None

    return True, d

#4) procesamiento del inventario

def procesar_inventario(ruta_fichero):
    lineas = leer_fichero(ruta_fichero)

    inventario = []
    errores = []

    for linea in lineas:
        dic = normalizar_linea(linea)
        valido,resultado = validar_datos(dic)
        if valido:
            inventario.append(resultado)
        else:
            errores.append(f"{linea}' -> {resultado}" )

    from collections import Counter
    contar_sistemas = Counter(srv["sistema"] for srv in inventario)

    #generar informe
    ips_unicas = sorted({srv["ip"] for srv in inventario})
    responsables = {srv["responsable"] for srv in inventario if srv["responsable"]}

    with open("informe_servidores.txt", "w", encoding="utf-8") as f:
        f.write(f"Número de servidores válidos: {len(inventario)}\n")
        f.write(f"Número de líneas descartadas (con errores): {len(errores)}\n")
        f.write(f"Lista de IPs únicas: {', '.join(ips_unicas)}\n")
        f.write(f"Responsables distintos: {len(responsables)}\n")
        f.write("\nServidores por sistema operativo:\n")
        for sistema, cantidad in contar_sistemas.items():
            f.write(f"  {sistema}: {cantidad}\n")

    return inventario, errores


if __name__ == "__main__":
    inv, errs = procesar_inventario("inventario.txt")
    print("=== INVENTARIO VÁLIDO ===")
    for s in inv:
        print(s)
    print("\n=== ERRORES ===")
    for e in errs:
        print(e)
    print("\nInforme guardado en informe_servidores.txt")