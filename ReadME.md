# Emphasoft Case

Постановка задачи:
```
При открытии должно показать кнопку «авторизоваться» по нажатию делает oauth
авторизацию ВКонтакте, и показывает имя авторизованного пользователя и 5 любых
друзей пользователя. При последующих запусках/заходах на страницу 
сразу показывает всю информацию т.к. уже понимает, что авторизовано 
и авторизация запоминается. 

Бекенд,  если потребуется, на любой технологии на ваш выбор.
```


Бекэнд:
- aiohttp
- aiohttp-jinja2
- aioredis


Запуск:

В файле `docker-compose.yml` указать `VK_APP_ID` и `VK_APP_SECRET_KEY`.
Запустить контейнеры командой `docker-compose -f docker-compose.yml up -d`

`VK_APP_ID` - ID приложения
`VK_APP_SECRET_KEY` - Защищенный ключ

