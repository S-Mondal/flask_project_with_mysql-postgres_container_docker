from flask import Flask, jsonify
import psycopg2
import mysql.connector

def get_mysql_version():
	try:
		conn = mysql.connector.connect(host='mysql_test', user='root', password='123456')
		db_Info = conn.get_server_info()
		print(db_Info)
		return db_Info
	except Exception as e:
		print("Connection failed: ",e)
		return None

app = Flask(__name__)

def get_postgres_version():
	try:
		conn = psycopg2.connect("host=postgres_test dbname=docker_db user=souvik password=souvik123")
		cur = conn.cursor()
		cur.execute('SELECT version()')
		db_version = cur.fetchone()
		print(db_version)
		return db_version
	except Exception as e:
		print("Connection failed: ",e)
		return None


@app.route('/')
def demo():
	postgres_ver = get_postgres_version()
	mysql_ver = get_mysql_version()
	return jsonify({"postgres_version":postgres_ver, "mysql_version":mysql_ver})


if  __name__ == '__main__':
	app.run(host='0.0.0.0')
