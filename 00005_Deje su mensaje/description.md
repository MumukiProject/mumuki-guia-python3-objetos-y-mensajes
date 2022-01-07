Por ahora sabemos que existen distintos tipos de objetos pero la verdad es que aún no vimos nada demasiado útil, ¿qué podemos hacer con esos objetos? :thinking:

Para solucionar problemas utilizando el paradigma orientado a objetos, interactuamos con ellos enviándoles mensajes a través de sus referencias.

:warning: Muchas veces, en lugar de decir que le enviamos un mensaje al objeto apuntado por la referencia, podemos llegar a decir...

_enviar un mensaje al objeto_ 

...o simplemente...

_enviar un mensaje a_

...porque si bien no es del todo correcto, es más breve :sweat_smile:. Lo importante es que entiendas que siempre estamos enviando el mensaje al objeto a través de una referencia y lo haremos escribiendo `objeto.mensaje`. ¡Veámoslo en práctica!

> Enviale el mensaje `necesita_saldo` al objeto referenciado por `celular_de_eli` escribiendo `celular_de_eli.necesita_saldo()` en la consola.