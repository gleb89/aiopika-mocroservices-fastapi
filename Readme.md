# aiopika

### Структура 
    ├── service_produser отправляет слушателю
    |   ├── main.py
    |   ├── Dockerfile
    ├── service_consumer сервис слушатель
    |   ├── main.py
    |   ├── Dockerfile
    ├── data\nginx
    |   └──app.conf
    ├── .env     
    └─ docker-compose.yml
    
touch file .env


        example
        POSTGRES_USER=postgres
        POSTGRES_PASSWORD=postgres
        POSTGRES_DB=postgres
    
Старт через docker-compose
   start the container:
   
        docker-compose up --build
        docker-compose up -d
        docker-compose up -d rabbit
        docker-compose up -d consumer
        docker-compose -f docker-compose.yml logs -f
        
        
  Url
  
      [a link]http://localhost:8080/service_produser/docs#/ -service produser
      [a link]http://localhost:8080/service_consumer/docs#/   service consumer