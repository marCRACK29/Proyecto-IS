# SISTEMA DE MANEJO DE CITAS MÉDICAS

## Integrantes

* Gabriela Zambrano
* Daniel Aburto
* Javier Torres
* Diego Rebollo
* Marcos Martínez Rojas

## Ejecución

Se asume un sistema operativo linux.

### Preparar base de datos local (opcional)

Se debe tener instalado y configurado `posgresql` a modo de poder ejecutar los comandos `createdb` y `psql`.

Ejecutar el script de configuración de la base de datos:

```bash
[ruta-repositorio]/code/back/db$ chmod +x ./db-config.sh
[ruta-repositorio]/code/back/db$ ./db-config.sh
```

### Preparar el entorno

Primero, se debe crear un entorno virtual e instalar las dependencias del programa. Esto se puede hace automáticamente ejecutando el script `setup.sh`:

```bash
[ruta-repositorio]$ chmod +x ./setup.sh
[ruta-repositorio]$ ./setup.sh
```

### Ejecutar

Para correr el programa, ejecutar el script `run.sh`:

```bash
[ruta-repositorio]$ chmod +x ./run.sh
[ruta-repositorio]$ ./run.sh
```