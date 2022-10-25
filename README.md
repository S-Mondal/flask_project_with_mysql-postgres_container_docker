# Flask Project with mysql and postgressql as container with docker

* Run mqsql without Dockerfile:
	`sudo docker run -d --name mysql_test -e MYSQL_ROOT_PASSWORD=123456 mysql`

* Use Dockerfile to build postgres image:
	`sudo docker build -t postgres_test:v1 -f Dockerfile_postgres .`

* Run container:
	`sudo docker run -d --name postgres_test postgres_test:v1 .`

* Get ip of mysql/postgres container:
	`sudo docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name_or_id>`

* Create app.py with the ip of mysql and postgres and default port with which it is running
* Build image with Dockerfile and run container and check the output 