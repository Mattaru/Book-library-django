### Для начала работы локально:
1. Копируйте ссылку репозитория с GitHub или же просто копируйти эту ссылку https://github.com/Mattaru/Book-library-django.git
1. Откройте командную строку и перейдите в папку, в которой хотите разместить проект `>>> cd path`
1. В командной строке введите `>>> git clone https://github.com/Mattaru/Book-library-django.git`
1. Перейдите в папку созданного репозитория `>>> cd Book-library-django`
1. Создайте вертуальную среду для Python. Для этого введите команду `>>> python -m venv путь до папки с проектом включительно/название вертуальной среды`
Пример полной команды: `>>> python -m venv C:/MyFolder/Book-library-django/env`
1. Теперь активируйте виртуальную среду `C:/MyFolder/Book-library-django> env\Scripts\activate`
1. Установите все модули совместимостей, для этого введите команду `>>> pip install -r requirements.txt` 
1. После того, как все совместимости установлены, перейдите в папку my_site `>>> cd my_site`
1. Создайте базу данных введя команду `>>> python manage.py migrate`
1. Импортируйте в базу уже подготовленные данные, в виде json, командой `>>> python manage.py loaddata data.json `
1. Сервер полностью готов к работе, запустите его командой `>>> python manage.py runserver`
#### После всего проделанного, можете открыть браузер и обраться по любому из указанных url:
###### http://127.0.0.1:8000/book/
###### http://127.0.0.1:8000/author/
###### http://127.0.0.1:8000/friend/
###### http://127.0.0.1:8000/publisher/
Для управления данными используйте соответсвующий интерфейс на страницах приложения или интерфейс администратора.
#### Права администратора:
Перед тем, как пользоваться интерфейсом администратора, нужно создать `superuser`. Что бы это сделать: выключите сервер, и введите команду
`>>> python manage.py createsuperuser` после чего заполните данные, через логин и парол вы будете получать доступ к правам администратора.
Теперь можете снова запустить сервер `>>> python manage.py runserver`
#### Можете использовать UI администратора, если обратитесь по url:
###### http://127.0.0.1:8000/admin/

### For local start:
* `>>> git clon -rep-`
* `>>> cd rep/path`
* `>>> python -m venv -dir-`
* `>>> -venv-dir\Scripts\activate`
* `>>> pip install -r requirements.txt`
* Create in my_site/ directory the folder with name "databases" if folder not exist
* `>>> cd my_site`
* `>>> python manage.py migrate`
* `>>> python manage.py loaddata data.json`
* `>>> python manage.py runserver`
* Now you can go to on one of urls:
  * http://127.0.0.1:8000/book/
  * http://127.0.0.1:8000/author/
  * http://127.0.0.1:8000/friend/
  * http://127.0.0.1:8000/publisher/
