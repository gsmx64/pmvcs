# Python MVC Shell Framework Package

## Sobre el paquete

Python MVC Shell Framework Package (PMVCS) es un pequeño framework para proyectos en shell realizados en Python.


### Instalar con pip3

```
pip install pmvcs

o

pip3 install pmvcs
```


### Configuración desde la consola en español

```
>>> python -m pmvcs.cli setup -l es
o
>>> python -m pmvcs.cli setup -language es
```

### Configuración desde la consola en inglés

```
>>> python -m pmvcs.cli setup -l en
o
>>> python -m pmvcs.cli setup -language en
```


### Configuración, paso a paso:

```
Inserta el nombre para la APP (predeterminado: "MyApp", deja en blanco):
>>> Mi App de Testeo

Inserta el nombre de carpeta para la APP (default: "app", deja en blanco):
>>> app

¿Habilitar depuración? (predeterminado: "No")
(Y) Sí - (N) No:
>>> Y

¿Ver información del proyecto al salir? (predeterminado: "Sí")
(Y) Sí - (N) No:
>>> Y

¿Habilitar soporte Multi-Idioma? (predeterminado: "Sí")
(Y) Sí - (N) No:
>>> Y

Selecciona el idioma predeterminado (predeterminado: "(1)")
(1) English - (2) Español:
>>> 2

¿Instalar datos de ejemplo, usar menú para múltiples
módulos o un único módulo personalizado?
(E) Datos de ejemplo
(M) Múltiples módulos
(S) Único módulo personalizado

Opción:
>>> E   -> Instala datos de ejemplo, un módulo en el menú con archivos controlador, modelo y vista.
>>> M   -> Instala múltiple módulos en menú con archivos controlador, modelo y vista cada uno.
>>> S   -> Instala un único módulo sin menú con archivo controlador.

-------------------------------------------------
 >>> ¡La configuración ha finalizado!
 >>> ¡Gracias por elegir PMVCS!
-------------------------------------------------

Presione una tecla para continuar . . .
```


### Agrega más Múltiples módulos

Instala nuevos múltiples achivos del módulo en el menú con controlador, modelo y vista cada uno.
Para agregar nuevos módulo en el menú, ejecuta lo siguiente:

```
>>> python -m pmvcs.cli menu -l es
o
>>> python -m pmvcs.cli menu -language es
```

```
Nombre actual de carpeta de la APP:
>>> app01

Inserta el nombre del módulo:
>>> example_two

¿Agregar otro módulo?
(Y) Sí - (N) No:
>>> N

-------------------------------------------------
 >>> ¡La configuración ha finalizado!
 >>> ¡Gracias por elegir PMVCS!
-------------------------------------------------

Presione una tecla para continuar . . .
```

### Ayudantes PMVCS

Puedes cargar ayudantes de PMVCS, por ejemplo:

```
viejo_valor = str('5')
print(type(viejo_valor))
>>> <class 'str'>

filters = self.pmvcs_helper.load_helper('filters', True)
nuevo_valor = filters.data_type(viejo_valor)

print(type(nuevo_valor))
>>> <class 'int'>
```

El ayudante "filters" devuelve un valor entero desde un número en cadena.


### Ayudantes Personalizados

Puedes cargar ayudantes personalizados, por ejemplo:

```
example = self.pmvcs_helper.load_helper('example')
example.my_func()
```

Ruta para almacenar tu ayudante: (carpeta_de_la_app)/helpers/

Formato en el archivo del ayudante:
```
from pmvcs.core.helpers.base_helper import BaseHelper


class ExampleHelper(BaseHelper):
    """ Class for Example Helper """

    def __init__(self, **kwargs) -> None:
        """
        Init PMVCS Example Helper requirements
        """
        super().__init__(**kwargs)

    def my_func(self):
        """
        Returns a float or int value
        """
        pass
```


## Repositorio

* [Repositorio PMVCS](https://github.com/gsmx64/pmvcs)
