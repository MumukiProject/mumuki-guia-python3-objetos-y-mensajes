En capítulos anteriores hablamos de funciones y procedimientos, aprendimos que las primeras nos sirven para retornar un valor mientras que los procedimientos son para cuando necesitamos que nuestro código tenga efecto o modifique algo.

Hasta el momento en objetos, enviamos mensajes que nos retornan un valor, como `tiene_bateria_maxima` o `necesita_saldo`.

¿Podremos enviar un mensaje que tenga un efecto? :face_with_hand_over_mouth:

> Probá en consola los siguientes comandos y averigüemos qué pasa :eyes:
>
```python
ム celular_de_eli.tiene_bateria_maxima()
ム celular_de_eli.cargar_a_tope()
ム celular_de_eli.tiene_bateria_maxima()
```