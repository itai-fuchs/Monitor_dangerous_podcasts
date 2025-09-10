

docker network create app-net

cd C:\Users\itai\PycharmProjects\Monitor_dangerous_podcasts\yamls

#run kafka container
   docker-compose -f "docker-compose_kafka.yml" up -d



# run elastic & kibana containers

    docker-compose -f "docker-compose_elastic.yml" up -d



# run services &  containers

    docker-compose -f "docker-compose_services.yml" up -d
cd ..

#run mongo container

  docker run --name my-mongo-container -d -p 27017:27017 mongo:latest

  docker network connect app-net mongo

cd .