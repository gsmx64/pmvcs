@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing AutoPEP8...
ECHO -----------------------------------------
env\Scripts\autopep8.exe -i -r app.py
env\Scripts\autopep8.exe -i -r app\__init__.py
env\Scripts\autopep8.exe -i -r app\controllers\__init__.py
env\Scripts\autopep8.exe -i -r app\controllers\base_controller.py
env\Scripts\autopep8.exe -i -r app\controllers\codebreaker_easy.py
env\Scripts\autopep8.exe -i -r app\controllers\codebreaker_hard.py
env\Scripts\autopep8.exe -i -r app\controllers\codebreaker_normal.py
env\Scripts\autopep8.exe -i -r app\decorators\__init__.py
env\Scripts\autopep8.exe -i -r app\helpers\__init__.py
env\Scripts\autopep8.exe -i -r app\interfaces\__init__.py
env\Scripts\autopep8.exe -i -r app\interfaces\base_controller.py
env\Scripts\autopep8.exe -i -r app\interfaces\base_model.py
env\Scripts\autopep8.exe -i -r app\interfaces\base_view.py
env\Scripts\autopep8.exe -i -r app\models\__init__.py
env\Scripts\autopep8.exe -i -r app\models\base_model.py
env\Scripts\autopep8.exe -i -r app\models\codebreaker.py
env\Scripts\autopep8.exe -i -r app\models\codebreaker_easy.py
env\Scripts\autopep8.exe -i -r app\models\codebreaker_hard.py
env\Scripts\autopep8.exe -i -r app\models\codebreaker_normal.py
env\Scripts\autopep8.exe -i -r app\models\errors.py
env\Scripts\autopep8.exe -i -r app\models\validations.py
env\Scripts\autopep8.exe -i -r app\models\entities\__init__.py
env\Scripts\autopep8.exe -i -r app\views\__init__.py
env\Scripts\autopep8.exe -i -r app\views\base_view.py
env\Scripts\autopep8.exe -i -r app\views\codebreaker_easy.py
env\Scripts\autopep8.exe -i -r app\views\codebreaker_hard.py
env\Scripts\autopep8.exe -i -r app\views\codebreaker_normal.py
env\Scripts\autopep8.exe -i -r tests\__init__.py
env\Scripts\autopep8.exe -i -r tests\test_codebreaker.py
pause