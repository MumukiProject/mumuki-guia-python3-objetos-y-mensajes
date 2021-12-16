Los objetos con los que trabajamos viven en un ambiente. Imaginemos que tenemos el siguiente código:

```python
brunoDiaz = batman
bruceWayne = brunoDiaz
clarkKent = superman
```

Nuestro ambiente se verá así:

[IMAGEN DE AMBIENTE]

Los círculos son los objetos y las flechas que los apuntan son referencias. Diremos que dos referencias son idénticas si apuntan al mismo objeto y para saberlo contamos con el operador `is`.

> Probá lo siguiente en la consola:
>
``` python
ム brunoDiaz is batman
ム brunoDiaz is bruceWayne
ム superman is clarkKent
ム superman is batman
```
> ¿Te imaginás que va a responder en cada caso?