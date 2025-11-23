Guía de Pruebas – Examen Flask

Autora: Angela Zarate – Naturopatía

A continuación se detallan las pruebas sugeridas para verificar el funcionamiento de los dos ejercicios desarrollados en Flask: Compra de Pintura y Login de Usuarios.

Ejercicio 1: Compra de Tarros de Pintura

Objetivo: Calcular el total a pagar considerando el valor del producto y el descuento según la edad del cliente.
| Concepto                    | Valor      |
| --------------------------- | ---------- |
| Precio por tarro de pintura | $9.000 CLP |


Reglas de descuento
| Edad                     | Descuento Aplicado  |
| ------------------------ | ------------------- |
| Menores de 18 años       | No aplica descuento |
| 18 a 30 años (inclusive) | 15% de descuento    |
| Mayores de 30 años       | 25% de descuento    |


Pruebas sugeridas
Caso 1 – Sin descuento
| Nombre | Edad | Tarros | Total sin descuento | Descuento | Total a pagar |
| ------ | ---: | -----: | ------------------: | --------- | ------------: |
| Pedro  |   16 |      1 |               9.000 | 0%        |         9.000 |


Caso 2 – 15% de descuento
| Nombre | Edad | Tarros | Total sin descuento | Descuento   | Total a pagar |
| ------ | ---: | -----: | ------------------: | ----------- | ------------: |
| Ana    |   20 |      2 |              18.000 | 2.700 (15%) |        15.300 |


Caso 3 – 25% de descuento
| Nombre | Edad | Tarros | Total sin descuento | Descuento   | Total a pagar |
| ------ | ---: | -----: | ------------------: | ----------- | ------------: |
| Luis   |   35 |      4 |              36.000 | 9.000 (25%) |        27.000 |


Casos de borde (verifican la lógica exacta)
| Nombre | Edad | Tarros | Descuento Esperado |
| ------ | ---: | -----: | ------------------ |
| Edad18 |   18 |      1 | 15%                |
| Edad30 |   30 |      2 | 15%                |
| Edad31 |   31 |      2 | 25%                |

Ejercicio 2: Login de Usuarios

Objetivo: Validar el acceso según usuario y contraseña predefinida en el servidor.

Credenciales válidas
| Tipo de Usuario | Usuario | Contraseña | Resultado Esperado            |
| --------------- | ------- | ---------- | ----------------------------- |
| Administrador   | juan    | admin      | Bienvenido administrador juan |
| Usuario normal  | pepe    | user       | Bienvenido usuario pepe       |


Credenciales incorrectas
| Usuario | Contraseña | Resultado Esperado               |
| ------- | ---------- | -------------------------------- |
| juan    | 1234       | Usuario o contraseña incorrectos |
| maria   | admin      | Usuario o contraseña incorrectos |
| test    | test       | Usuario o contraseña incorrectos |
| pepe    | admin      | Usuario o contraseña incorrectos |

El campo del usuario convierte el valor a minúsculas, por lo que JUAN, juan o Juan funcionarán igual.
