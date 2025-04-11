#!/bin/bash
apt-get update
apt-get -y install mysql-server
curl -fsSL https://ollama.com/install.sh | sh
service mysql start
mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'root';FLUSH PRIVILEGES;"
mysql -u root -p -e "CREATE DATABASE medical_cs;"
mysql -u root -p medical_cs < medical_cs_db.sql
pip install langchain langgraph PyMySQL mysql-connector-python PyMySQL langchain-community 'bitsandbytes==0.45.0' 'accelerate >=0.26.0' langchain-ollama langgraph-prebuilt "fastapi[all]"
ollama serve
