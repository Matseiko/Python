﻿Лабораторна робота №5

Автентифікація і авторизація

В даній лабораторній порібно реалідізувати автентифікацію та авторизацію користувачів для розробленого REST API. Автентифікація є перевіркою того, що запит відбувається від імені конкретного користувача. Авторизація є перевіркою того чи має конкретний користувач доступ до конкретної операції над певним ресурсом.

Для автентифікації до REST API замість типової для веб-сторінок моделі автентифікації на базі HTTP-cookie як правило виконують так звану HTTP автентифікацію. Зі сторони клієнта HTTP автентифікація виконується за допомогою хедера Authorization. Значення даного хедера можуть мати різні схеми автентифікації, та . Ми будемо розглядати дві такі схеми, а саме: Basic та Bearer.

При Basic смемі значення хедера виглядає наступним чином: Basic <credentials>. Де <credentials> це закодована в Base64 стрічка наступного виду: username:password.
При Bearer схемі значення хедера виглядає наступним чином: Bearer <credentials>. Де <credentials> є токеном автентифікації. Оригінально дану схему створили для токенів згенерованих при OAuth 2.0 авторизації, однак Bearer схеми використовуються для передачі токерів різного формату, як наприклад JWT-токени. Іноді для передачі JWT-токенів вказують схему JWT, однак вона не включена в офіційний стандарт.

Для спрощення реалізації Bearer (JWT-автентифікації) використовувався пакет Flask-JWT
Хід роботи
1. Реалізація автентифікацію користувачів обраним механіхмом, обмеження доступу до операцій над ресурсами для запитів, що не відповідають обраному механізму автентифікації
2. Реалізація авторизацію користувачів, перевірка права доступу для того чи іншого користувача, повернення ресурсів, що належать конкретному користувачеві
3. Перевірка коректність роботи автентифікації та авторизації здійснивши кілька запитів до системи

Додаткова інформація : 

https://www.youtube.com/watch?v=WxGBoY5iNXY

https://pythonhosted.org/Flask-JWT/

