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

### NAMENODE

Para acessar o ambiente do namenode, execute:
```shell
docker exec -it namonode bash
```

## Introdução 

Para o nosso trabalhado, escolhemos um dataset referente a reviews de cervejas (beer_reviews.csv). O objetivo é importarmos este arquivo no HDFS e poder localizá-lo no HUE, em seguida trabalhar no Jupyter utilizando o PySpark 

## Subir o arquivo HDFS

Primeiro, vamos subir criar um diretório no namenode e no HDFS para receber nosso arquivo.

__OBS__: Acessar o namenode

* namenode:
```shell
mkdir /mba-data
```
* HDFS:
```shell
hadoop fs -mkdir /mba-data
```


Em seguida, vamos enviar o arquivo do nosso ambiente local para o namenode, e depois para o HDFS:

__ambiente local --> namenode --> HDFS__

* No ambiente local, vamos carregar o arquivo para o namenode:
```shell
docker cp /home/docker/bigdata_docker_mba_spark-main/beer_reviews.csv namenode:/mba-data/beer_reviews.csv
```


* No namenode, vamos subir o arquivo para o HDFS:
```shell
hadoop fs -put /mba-data/beer_reviews.csv /mba-data/beer_reviews.csv
```


* Vamos acessar o HUE para validar o arquivo:

http://localhost:8888/


* Em seguida vamos localizar o diretório que criamos e acessá-lo para validar se o arquivo está lá: 

![hue](/images/HUE.png)

### OPCIONAL

Para baixar o arquivo do dataset via Python, é possível utilizar a API do kaggle. Basta gerar um token no site do Kaggle e guardá-lo em ```~/.kaggle/kaggle.json```

Depois rode o arquivo main.py dentro de /app:

```shell
python3 main.py
```

## PySpark - Jupyter

Link do Jupyter: http://localhost:8889/

Vamos acessar o Jupyter e criar um novo projeto PySpark. 

__new --> PySpark (Notebook)__

* Vamos ler nosso arquivo dentro de uma variável para consumir os dados. 

```python
df = spark.read.csv('/mba-data/beer_reviews.csv', header=True)
```

* Em seguida, vamos validar se os dados foram lidos com sucesso (No caso vamos limitar em 10 linhas).

```python
df.show(10)
```

* Resultado:
![10 linhas](/images/show-10-lines.png)
