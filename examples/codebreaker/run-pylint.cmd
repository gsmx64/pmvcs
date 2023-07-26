@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing PyLint...
ECHO -----------------------------------------
env\Scripts\pylint.exe app.py
env\Scripts\pylint.exe app\__init__.py
env\Scripts\pylint.exe app\controllers\__init__.py
env\Scripts\pylint.exe app\controllers\base_controller.py
env\Scripts\pylint.exe app\controllers\codebreaker_easy.py
env\Scripts\pylint.exe app\controllers\codebreaker_hard.py
env\Scripts\pylint.exe app\controllers\codebreaker_normal.py
env\Scripts\pylint.exe app\decorators\__init__.py
env\Scripts\pylint.exe app\helpers\__init__.py
env\Scripts\pylint.exe app\interfaces\__init__.py
env\Scripts\pylint.exe app\interfaces\base_controller.py
env\Scripts\pylint.exe app\interfaces\base_model.py
env\Scripts\pylint.exe app\interfaces\base_view.py
env\Scripts\pylint.exe app\models\__init__.py
env\Scripts\pylint.exe app\models\base_model.py
env\Scripts\pylint.exe app\models\codebreaker.py
env\Scripts\pylint.exe app\models\codebreaker_easy.py
env\Scripts\pylint.exe app\models\codebreaker_hard.py
env\Scripts\pylint.exe app\models\codebreaker_normal.py
env\Scripts\pylint.exe app\models\errors.py
env\Scripts\pylint.exe app\models\validations.py
env\Scripts\pylint.exe app\models\entities\__init__.py
env\Scripts\pylint.exe app\views\__init__.py
env\Scripts\pylint.exe app\views\base_view.py
env\Scripts\pylint.exe app\views\codebreaker_easy.py
env\Scripts\pylint.exe app\views\codebreaker_hard.py
env\Scripts\pylint.exe app\views\codebreaker_normal.py
env\Scripts\pylint.exe tests\__init__.py
env\Scripts\pylint.exe tests\test_codebreaker.py
pause