# Video

https://www.youtube.com/watch?v=FB2yRuvIY7w&ab_channel=CristoferCardoso

# MotoWorld

Proyecto dedicado a un eCommerce de productos y accesorios para motos.
Principales acciones ejecutables:

- Crear, editar y borrar articulos en venta.
- Seleccionar articulos y dejarlos en un carrito hasta ser comprados.
- Crearte un usuario para tener tu propio carrito de compras. 


# Ejecución 

Para ejecutar el proyecto se requiere:

## Instalar dependencias

Para instalar dependencias, se requiere ejecutar `pip install`, asegurarse de estar dentro de la carpeta del archivo y poder visualizar el archivo `requirements.txt` cuando se ejecute `ls` o en su defecto `dir`

```bash
> pip install -r requirements.txt
```

## Configuracion de Django

Una vez terminada la instalacion de las dependencias, se deberán de ejecutar unos comandos de Django.

### Migraciones

python manage.py migrate
```

### Crear Superuser

python manage.py createsuperuser
(Se pedirá que se genere un usuario, email y contraseña)
```

### Ejecutar el servidor

python mananage.py runserver
```
