# BIGDATA DOCKER MBA SPARK

## INSTRUÇÕES

Para subir o ambiente, entre no console com o comando:
```shell
docker-compose up -d
```

Para derrubar o ambiente::
```shell
docker-compose down
```

### HUE

A primeira vez que subir o ambiente, entre no container do HUE:
```shell
docker exec -it hue bash
```
E execute este comando para criar as tabelas do HUE no database:
```shell
./build/env/bin/hue migrate
```
Para acessar a interface do HUE, use o endereço ```http://localhost:8888```

Se receber um erro de que não conseguiu se conectar ao Hive, espere um pouco, pois o hive-server pode demorar um pouco para subir.
