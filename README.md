# Python

Лабораторна робота №1

14 варіант ('python 3.8.*', 'virtualenv + requirements.txt')

Для того щоб розгорнути проект перш за все потрібно інсталювати Python 3.8 версії за допомогою pyenv і встановити інтегроване середовище розробки для цієї мови програмування (наприклад Pycharm) 

Якщо ви ніколи не клонували репозиторій ,то вам потрібно встановити git.
https://git-scm.com/download/win - скачуємо git
https://www.youtube.com/watch?v=qt-QDN3MyeM - відео про його встановлення
Клонування реаозиторію :
-	створюємо папку
-	в пошуковому запиті вводимо Git Brash 
-	переходимо по знайденів програмі
-	після її відкриття вводимо 
git clone https://github.com/Matseiko/Python.git
Після цього необхідно добавити в залежності проекту і інсталювати Flask за допомогою вводу такої команди : 
pip install flask 
Також ми інсталюємо gevent (сумісний з WSGI, може бути використаний для професійного обслуговування нашої програми Flack) .Команда :
pip install gevent
Про використання gevent і Flask у Windows:                   
http://www.danieleteti.it/post/gevent-and-flask-on-windows/
Для запуску проекту потрібно відкрити файл app.py в інтерактивному середовищі і закомпілювати його. 
Перейшовши за посиланням http://127.0.0.1:5000/api/v1/hello-world-14 ви побачите текст “Hello World 14” з HTTP статус кодом відповіді ‘200’.
