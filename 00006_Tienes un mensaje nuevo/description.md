Ya enviamos nuestro primer mensaje. Obviamente los objetos pueden recibir más de un mensaje, sino sería muy acotado lo que podemos hacer con ellos. :face_with_raised_eyebrow:

A los objetos con los que trabajamos en lecciones anteriores también podemos enviarles mensajes y a algunos de ellos ya los conocés :hushed:. Funciones que utilizamos anteriormente como `str.upper` o `list.append` se pueden escribir de la forma `objeto.mensaje`. Por ejemplo:

En lecciones anteriores hemos escrito `str.upper("mumuki")` donde `str.upper` es una función y `"mumuki"` es el objeto string que recibe como argumento. Con la sintaxis que acabamos de aprender podríamos hacer directamente `"mumuki".upper()` donde `"mumuki"` es el objeto receptor del mensaje `upper`. 

> ¿No nos crees? Probá lo siguiente consola:
>
```python
ム celular_de_eli.tiene_bateria_maxima()
ム str.upper("mumuki")
ム "mumuki".upper()
ム numeros
ム list.append(numeros, 16)
ム numeros
ム numeros.append(32)
ム numeros
```
> ¿Te imaginás que va a pasar en cada caso?
