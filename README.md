# SPRINT8
Para iniciar el servidor: 
    python3 manage.py runserver
Para verificar los requisitos del sprint se puede utilizar Postman, o la página del servidor. 

Para las peticiones realizadas por un CLIENTE, se puede utilizar el siguiente usuario y contraseña: 

    user: 56493045
    passs: 1234

* OBTENER DATOS DE UN CLIENTE
    http://127.0.0.1:8000/api/cliente/56493045/

* OBTENER SALDO DE CUENTA DE UN CLIENTE

    http://127.0.0.1:8000/api/cliente/56493045/ 

* OBTENER MONTO DE PRESTAMOS DE UN CLIENTE

    http://127.0.0.1:8000/api/cliente/56493045/ 

Para las peticiones realizadas por un EMPLEADO, se puede utilizar el siguiente usuario y contraseña: 

    user: 
    passs: 1234
    
* OBTENER MONTO DE PRESTAMOS DE UNA SUCURSAL
* OBTENER TARJETAS ASOCIADAS A UN CLIENTE
* GENERAR UNA SOLICITUD DE PRESTAMO PARA UN CLIENTE
* ANULAR SOLICITUD DE PRESTAMO DE CLIENTE

Para las peticiones realizadas por un CLIENTE o un EMPLEADO, se puede utilizar el siguiente usuario y contraseña: 
CLIENTE: 
    user: 56493045
    passs: 1234
EMPLEADO: 
    user: 
    passs: 1234
* MODIFICAR DIRECCION DE UN CLIENTE

En el caso del endpoint público: 
* LISTADO DE TODAS LAS SUCURSALES: 
    http://127.0.0.1:8000/api/sucursales/