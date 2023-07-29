# Python MVC Shell Framework Package

## Sobre el paquete

Python MVC Shell Framework Package (PMVCS) es un pequeño framework para proyectos en shell realizados en Python.

![PMVCS inicio selección de idioma](/docs/images/pmvcs-intro-language.png)

![PMVCS menus para múltiples módulos](/docs/images/pmvcs-es-menus.png)

![PMVCS corriendo un módulo](/docs/images/pmvcs-es-runing-module.png)

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
o
>>> pmvcs-cli setup -l es
o
>>> pmvcs-cli setup -language es
```

### Configuración desde la consola en inglés

```
>>> python -m pmvcs.cli setup -l en
o
>>> python -m pmvcs.cli setup -language en
o
>>> pmvcs-cli setup -l en
o
>>> pmvcs-cli setup -language en
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


### Ayudantes Personalizados: Pasar variables:

En el __init__ debería tener:

```
def __init__(self, **kwargs) -> None:
	self.pmvcs_helper = kwargs['pmvcs_helper']
	self.kwargs = { 'pmvcs_cfg': kwargs['pmvcs_cfg'],
					'pmvcs_lang': kwargs['pmvcs_lang'],
					'pmvcs_helper': kwargs['pmvcs_helper']}
						
```

Y en la función que llama al ayudante:

```
def to_string_table(self, data: dict) -> str:
	kwargs2 = { 'data': data,
				'file_name': 'temp_file'}
	kwargs2.update(self.kwargs)
	table_helper = self.pmvcs_helper.load_helper('table', **kwargs2)
	table_helper.record_file()
```

Finalmente en el ayudante recuperamos los valores como:

```
def __init__(self, **kwargs) -> None:
	super().__init__(**kwargs)
	
	self._data = kwargs['data']
	self._file_name = f"{kwargs['file_name']}.{self._file_extension}"
```


### Obtener constantes de configuration de config.ini:

Obtiene una constante de configuración en tipo cadena desde "OPTIONS":
```
Código: >>> self.cfg.get("EXAMPLE_CONSTANT", "OPTIONS")
Retorna: This is an example value from config file
Tipo de Valor: <class 'str'>
```

Obtiene una constante de configuración en tipo cadena desde "DEFAULT":
```
Código: >>> self.cfg.get("DEFAULT_TITLE", "DEFAULT")
Retorna: Example App
Tipo de Valor: <class 'str'>
```

Obtiene una constante de configuración en tipo entero:
```
Código: >>> self.cfg.get("EXAMPLE_INT", "OPTIONS", "int")
Retorna: 8
Tipo de Valor: <class 'int'>
```

Obtiene una constante de configuración en tipo flotate:
```
Código: >>> self.cfg.get("EXAMPLE_FLOAT", "OPTIONS", "float")
Retorna: 1.57
Tipo de Valor: <class 'float'>
```

Obtiene una constante de configuración en tipo booleano:
```
Código: >>> self.cfg.get("EXAMPLE_BOOLEAN", "OPTIONS", "boolean")
Retorna: True
Tipo de Valor: <class 'bool'>
```

Obtiene una constante de configuración en una lista:
```
Código: >>> self.cfg.get("EXAMPLE_LIST", "OPTIONS", "list")
Retorna: ['1', '2']
Tipo de Valor: <class 'list'>
```

Obtiene una constante de configuración en un diccionario:
```
Código: >>> self.cfg.get("EXAMPLE_DICT", "OPTIONS", "dict")
Retorna: {'value_one': '1', 'value_two': '2'}
Tipo de Valor: <class 'dict'>
```


### Obtener constantes de idioma de languages/es.ini:

Obtiene la etiqueta de idioma actual:
```
Código: >>> self.lang.tag
Retorna: en
Tipo de Valor: <class 'str'>
```

Obtiene una constante de idioma:
```
Código: >>> self.lang.get("LANG_EXAMPLE_STRING")
Retorna: This is an example string
Tipo de Valor: <class 'str'>
```

Obtenga una constante de idioma pasando un valor en String-Print-Format.
En el archivo de idioma verá por ejemplo: "El valor aquí: "{}"
```
Código: >>> self.lang.sprintf("LANG_EXAMPLE_SPRINTF", "3")
Retorna: String-Print-Format value here: "3"
Tipo de Valor: <class 'str'>
```

Obtenga una constante de idioma pasando varios valores en String-Print-Format.
En el archivo de idioma verá por ejemplo: "Uno: "{}". Dos: "{}". Tres: "{}".
```
Código: >>> self.lang.sprintf("LANG_EXAMPLE_SPRINTF2", "1", "2", "3")
Retorna: One: "1". Two: "2". Three: "3".
Tipo de Valor: <class 'str'>
```

Traduciendo una cadena:
```
Código: >>> self.lang.translate(value)   -> value = 'dictionary'
Retorna: Dictionary
Tipo de Valor: <class 'str'>
```
 
 
### Uso de las funciones de vista de PMVCS

Esto muestra la pancarta con el nombre de la App:
```
Código: >>> self.pmvcs_view.get_intro()
```

Esto muestra el mensaje de la salida:
```
Código: >>> self.pmvcs_view.get_exit()
```

Esto inserta un salto de línea sin print():
```
Código: >>> self.pmvcs_view.line_brake()
```

Esto inserta un salto de línea con print():
```
Código: >>> self.pmvcs_view.line_brake(True)
```

Esto inserta una pausa para presionar ENTER para comenzar:
```
Código: >>> self.pmvcs_view.input_start()
```

Esto inserta una pausa para presionar ENTER para continuar:
```
Código: >>> self.pmvcs_view.input_pause()
```
Esto inserta un input() de selección de opción:
```
Código: >>> self.pmvcs_view.input_options()
```

Esto inserta un input():
```
Código: >>> self.pmvcs_view.input_generic(text)
```

 
## Repositorio

* [Repositorio PMVCS](https://github.com/gsmx64/pmvcs)
