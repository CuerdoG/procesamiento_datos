# Procesamiento de Inventario de Servidores

Este repositorio contiene una solución en Python para el procesamiento, limpieza y validación de un fichero de inventario de servidores (`inventario.txt`). El script transforma datos irregulares y poco estructurados en una lista de diccionarios validada, generando un informe final de auditoría.

## Descripción del Proyecto

El objetivo es procesar un archivo con formato inconsistente que presenta:
* **Separadores mixtos**: Uso de `;` y `,`.
* **Inconsistencias de texto**: Espacios sobrantes y variaciones en mayúsculas/minúsculas.
* **Datos faltantes**: Campos opcionales o líneas incompletas.
* **Ruido**: Comentarios (marcados con `#`) y líneas vacías.

## Requisitos Técnicos

El script implementa una arquitectura modular basada en las siguientes funciones obligatorias:

1.  **`leer_fichero()`**: Carga el archivo y descarta líneas irrelevantes.
2.  **`normalizar_linea()`**: Homogeniza separadores, limpia espacios y ajusta el formato de *strings* (SO a minúsculas y responsables capitalizados).
3.  **`validar_datos()`**: Aplica lógica de validación (formato IPv4, sistemas operativos permitidos y obligatoriedad de campos).
4.  **`procesar_inventario()`**: Orquestador principal que coordina el flujo y genera las métricas.

## Instalación y Uso

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/CuerdoG/procesamiento_datos.git](https://github.com/CuerdoG/procesamiento_datos.git
   cd procesamiento_datos

2. **Ejecutar el .py**:
   ```bash
   py procesamiento_inventario.py

## Ejemplo de salida
```bash
{
    "nombre": "srv-web01",
    "ip": "192.168.1.10",
    "sistema": "linux",
    "ubicacion": "sala 1",
    "responsable": "Ana"
}
```
## Ejemplo del informe generado
```bash
Número de servidores válidos cargados: 6
Número de líneas descartadas (con errores): 5
Lista de IPs únicas: 192.168.1.10, 192.168.1.20...
Responsables distintos: 3
