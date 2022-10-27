# Flask Project with mysql and postgressql as different container with docker

* Run mqsql without Dockerfile:
	`sudo docker run -d --name mysql_test -e MYSQL_ROOT_PASSWORD=123456 mysql`

* Use Dockerfile to build postgres image:
	`sudo docker build -t postgres_test:v1 -f Dockerfile_postgres .`

* Run container:
	`sudo docker run -d --name postgres_test postgres_test:v1`

* Get ip of mysql/postgres container:
	`sudo docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name_or_id>`

* Create app.py with the ip of mysql and postgres and default port with which it is running
* Build image with Dockerfile and run container
	`docker build -t flask_test:v1 -f Dockerfile_flask .`
	`docker run -d --name flask_test -p 5000:5000 flask_test:v1`

* Check the output: http://localhost:5000/

### OR

* Create network to interact with other containers by contaniner name:
	`sudo docker network create new_network`

* Run mqsql without Dockerfile within network:
	`sudo docker run -d --name mysql_test -e MYSQL_ROOT_PASSWORD=123456 --network new_network mysql`

* Use Dockerfile to build postgres image:
	`sudo docker build -t postgres_test:v1 -f Dockerfile_postgres .`

* Run container within network:
	`sudo docker run -d --name postgres_test --network new_network postgres_test:v1`

* Build image with Dockerfile and run container within network
	`docker build -t flask_test:v1 -f Dockerfile_flask .`
	`sudo docker run -d --name flask_test --network new_network -p 5000:5000 flask_test:v1`

* Check the output: http://localhost:5000/


### OR

* Create docker-compose.yml file to run muti-container at the time.
* Build images with docker compose:
	`docker compose build`

* Run containers with docker compose:
	`docker compose up -d`

* Check the output: http://localhost:5000/

* Remove containers with docker compose:
	`docker compose down`