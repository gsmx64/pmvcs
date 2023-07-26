# Python MVC Shell Framework Package

## About the package

Python MVC Shell Framework Package (PMVCS) is a tiny framework for shell projects making in Python.

![PMVCS intro language selection](/docs/images/pmvcs-intro-language.png)

![PMVCS menus for multiple modules](/docs/images/pmvcs-en-menus.png)

![PMVCS runing module](/docs/images/pmvcs-en-runing-module.png)

### Install with pip3

```
pip install pmvcs

or

pip3 install pmvcs
```


### Settings from console in english

```
>>> python -m pmvcs.cli setup -l en
or
>>> python -m pmvcs.cli setup -language en
or
>>> pmvcs-cli setup -l en
or
>>> pmvcs-cli setup -language en
```

### Settings from console in spanish

```
>>> python -m pmvcs.cli setup -l es
or
>>> python -m pmvcs.cli setup -language es
or
>>> pmvcs-cli setup -l es
or
>>> pmvcs-cli setup -language es
```


### Setup, step by step:

```
Insert APP name (default: "MyApp", leaves blank):
>>> My Test App

Insert APP folder name (default: "app", leaves blank):
>>> app

Enable debug? (default: "No")
(Y) Yes - (N) No:
>>> Y

View project information on exit? (default: "Yes")
(Y) Yes - (N) No:
>>> Y

Enable Multi-Language support? (default: "Yes")
(Y) Yes - (N) No:
>>> Y

Define default Language (default: "(1)")
(1) English - (2) Español:
>>> 2

Installs example data, use menu for multiple modules or unique module?
(E) Example data
(M) Multiple modules
(S) Unique module

Option:
>>> E   -> Installs data examples, one module in menu with controller, model and view files.
>>> M   -> Installs multiple modules in menu with controller, model and view files each one.
>>> S   -> Installs a unique module in menu with controller file.

-------------------------------------------------
 >>> Configuration has finished
 >>> Thanks for choose PMVCS!
-------------------------------------------------

Press any key to continue . . .
```


### Add a new Multiple modules

Installs new multiple modules in menu with controller, model and view files each one.
For adding new modules in menu, run the following:

```
>>> python -m pmvcs.cli menu -l en
o
>>> python -m pmvcs.cli menu -language en
```

```
Current APP folder name:
>>> app01

Insert module name:
>>> example_two

Insert another module
(Y) Yes - (N) No:
>>> N

-------------------------------------------------
 >>> Configuration has finished
 >>> Thanks for choose PMVCS!
-------------------------------------------------

Press any key to continue . . .
```


### PMVCS Helpers

You can load PMVCS Helpers, for example:

```
old_value = str('5')
print(type(old_value))
>>> <class 'str'>

filters = self.pmvcs_helper.load_helper('filters', True)
new_value = filters.data_type(old_value)

print(type(new_value))
>>> <class 'int'>
```

The helper "filters" returns an integer value from a string number.


### Custom Helpers

You can load custom helpers, for example:

```
example = self.pmvcs_helper.load_helper('example')
example.my_func()
```

Path to save your helper: (app_folder)/helpers/

Format in helper's file:
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


## Repository

* [Repository PMVCS](https://github.com/gsmx64/pmvcs)
