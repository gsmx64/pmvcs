@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing flake8...
ECHO -----------------------------------------
env\Scripts\flake8.exe --append-config .flake8 app.py
env\Scripts\flake8.exe --append-config .flake8 setup.py
env\Scripts\flake8.exe --append-config .flake8 app\__init__.py
env\Scripts\flake8.exe --append-config .flake8 app\controllers\__init__.py
env\Scripts\flake8.exe --append-config .flake8 app\controllers\base_controller.py
env\Scripts\flake8.exe --append-config .flake8 app\controllers\example_one.py
env\Scripts\flake8.exe --append-config .flake8 app\controllers\test.py
env\Scripts\flake8.exe --append-config .flake8 app\decorators\__init__.py
env\Scripts\flake8.exe --append-config .flake8 app\helpers\__init__.py
env\Scripts\flake8.exe --append-config .flake8 app\interfaces\__init__.py
env\Scripts\flake8.exe --append-config .flake8 app\interfaces\base_controller.py
env\Scripts\flake8.exe --append-config .flake8 app\interfaces\base_model.py
env\Scripts\flake8.exe --append-config .flake8 app\interfaces\base_view.py
env\Scripts\flake8.exe --append-config .flake8 app\models\__init__.py
env\Scripts\flake8.exe --append-config .flake8 app\models\base_model.py
env\Scripts\flake8.exe --append-config .flake8 app\models\example_one.py
env\Scripts\flake8.exe --append-config .flake8 app\models\entities\__init__.py
env\Scripts\flake8.exe --append-config .flake8 app\views\__init__.py
env\Scripts\flake8.exe --append-config .flake8 app\views\base_view.py
env\Scripts\flake8.exe --append-config .flake8 app\views\example_one.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\__main__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\__version__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\cli.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\pmvcs.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\router.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\controllers\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\controllers\base_controller.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\controllers\menus.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\decorators\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\decorators\decorators_views.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\helpers\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\helpers\base_helper.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\helpers\filters.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\interfaces\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\interfaces\base_controller.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\interfaces\base_helper.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\interfaces\base_model.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\interfaces\base_view.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\interfaces\menus.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\interfaces\router.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\interfaces\sample.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\models\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\models\about.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\models\base_model.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\models\configuration.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\models\language.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\models\menus.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\models\parser.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\models\entities\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\setup\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\setup\setup.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\setup\setup_config_file.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\setup\setup_defaults.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\setup\setup_example.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\setup\setup_extras.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\setup\setup_files.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\setup\setup_install.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\setup\setup_menus.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\setup\setup_multiple.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\setup\setup_parser.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\setup\setup_unique.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\views\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\views\base_view.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\core\views\sample.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\app.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\defaults\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\defaults\controllers\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\defaults\controllers\base_controller.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\defaults\decorators\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\defaults\helpers\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\defaults\interfaces\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\defaults\interfaces\base_controller.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\defaults\interfaces\base_model.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\defaults\interfaces\base_view.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\defaults\models\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\defaults\models\base_model.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\defaults\models\entities\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\defaults\views\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\defaults\views\base_view.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\example\controllers\base_controller.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\example\controllers\example_one.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\example\models\example_one.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\example\views\example_one.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\module_unique\controllers\unique.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\modules_base\controllers\controller.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\modules_base\models\model.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\setup\modules_base\views\view.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\tests\__init__.py
env\Scripts\flake8.exe --append-config .flake8 pmvcs\tests\test_default.py
pause