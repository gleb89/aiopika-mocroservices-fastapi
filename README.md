# aiopika

### Структура 
    ├── fast отправляет слушателю
    |   ├── main.py
    |   ├── Dockerfile
    ├── listen просто сервис
    |   ├── main.py
    |   ├── Dockerfile
    ├── data
    |   ├── nginx
    |       └──app.conf
    ├── cons слушатель
    |   ├── cons.py
    |   ├── Dockerfile
    └─ docker-compose.yml
    
    
    
Старт через docker-compose
   start the container:
   
        docker-compose up --build
        docker-compose up -d
        docker-compose -f docker-compose.yml logs -f
