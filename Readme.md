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
        docker-compose up -d rabbit
        docker-compose up -d consumer
        docker-compose -f docker-compose.yml logs -f
        
        
  Url
  
      http://localhost:8080/listen/docs#/ -listen service
      http://localhost:8080/fast/docs#/   fast service