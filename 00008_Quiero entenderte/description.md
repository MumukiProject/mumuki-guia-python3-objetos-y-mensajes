Lo que sucede es que para que podamos enviarle un mensaje a un objeto, el objeto tiene que entender ese mensaje. De lo contrario se lanzará un error como el que vimos en el ejercicio anterior. :grimacing:

Al conjunto de mensajes que podemos enviarle a un objeto lo denominamos _interfaz_.
Por ejemplo si retomamos a `batman` y le enviamos los siguientes mensajes:

```python
ムbatman.necesita_descanso()
True
ムbatman.llamar_a_robin()
ムbatman.volar()
File "<input>", line 1, in <module>
AttributeError: 'Batman' object has no attribute 'volar'
```
Podemos notar que tanto `necesita_descanso` como `llamar_a_robin` forman parte de la interfaz de `batman`, mientras que `volar` no.

>  Según lo que ya probamos, ¿qué mensajes conforman la interfaz del `celular_de_eli`?
