Los objetos con los que trabajamos viven en un ambiente. Imaginemos que tenemos el siguiente código:

```python
bruno_diaz = batman
bruce_wayne = bruno_diaz
clark_kent = superman
```

Nuestro ambiente se verá así:

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-objetos-y-mensajes/master/assets/objetos_nuevo_1_1647530733877.3.svg" alt="objetos_nuevo_1_1647530733877.3.svg" width="350px" height="auto">

Los círculos son los objetos y las flechas que los apuntan son referencias. Diremos que dos referencias son idénticas si apuntan al mismo objeto y para saberlo contamos con el operador `is`.

> Probá lo siguiente en la consola:
>
``` python
ム bruno_diaz is batman
ム bruno_diaz is bruce_wayne
ム superman is clark_kent
ム superman is batman
```
> ¿Te imaginás que va a responder en cada caso?