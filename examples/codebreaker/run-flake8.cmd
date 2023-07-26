@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing flake8...
ECHO -----------------------------------------
env\Scripts\flake8.exe app.py
env\Scripts\flake8.exe app\__init__.py
env\Scripts\flake8.exe app\controllers\__init__.py
env\Scripts\flake8.exe app\controllers\base_controller.py
env\Scripts\flake8.exe app\controllers\codebreaker_easy.py
env\Scripts\flake8.exe app\controllers\codebreaker_hard.py
env\Scripts\flake8.exe app\controllers\codebreaker_normal.py
env\Scripts\flake8.exe app\decorators\__init__.py
env\Scripts\flake8.exe app\helpers\__init__.py
env\Scripts\flake8.exe app\interfaces\__init__.py
env\Scripts\flake8.exe app\interfaces\base_controller.py
env\Scripts\flake8.exe app\interfaces\base_model.py
env\Scripts\flake8.exe app\interfaces\base_view.py
env\Scripts\flake8.exe app\models\__init__.py
env\Scripts\flake8.exe app\models\base_model.py
env\Scripts\flake8.exe app\models\codebreaker.py
env\Scripts\flake8.exe app\models\codebreaker_easy.py
env\Scripts\flake8.exe app\models\codebreaker_hard.py
env\Scripts\flake8.exe app\models\codebreaker_normal.py
env\Scripts\flake8.exe app\models\errors.py
env\Scripts\flake8.exe app\models\validations.py
env\Scripts\flake8.exe app\models\entities\__init__.py
env\Scripts\flake8.exe app\views\__init__.py
env\Scripts\flake8.exe app\views\base_view.py
env\Scripts\flake8.exe app\views\codebreaker_easy.py
env\Scripts\flake8.exe app\views\codebreaker_hard.py
env\Scripts\flake8.exe app\views\codebreaker_normal.py
env\Scripts\flake8.exe tests\__init__.py
env\Scripts\flake8.exe tests\test_codebreaker.py
pause