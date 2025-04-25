#!/bin/bash
apt-get update
apt-get -y install mysql-server
curl -fsSL https://ollama.com/install.sh | sh
service mysql start
#this line below are used to setup a mysql database in the cloud vm as it naturally doesn't support any DBMS
mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'root';FLUSH PRIVILEGES;"
#create the database for the app
mysql -u root -p -e "CREATE DATABASE medical_cs;"
#loading the dummy database
mysql -u root -p medical_cs < medical_cs_db.sql
pip install langchain langgraph PyMySQL mysql-connector-python PyMySQL langchain-community faiss-cpu pypdf sentence-transformers 'bitsandbytes==0.45.0' 'accelerate >=0.26.0' langchain-ollama langchain_experimental langgraph-prebuilt "fastapi[all]"
ollama serve