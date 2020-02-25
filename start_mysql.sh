#!/usr/bin/env bash

pushd `dirname $0` > /dev/null
BASE_DIR=`pwd -P`
popd > /dev/null

#############
# Functions
#############
function logging {
    echo "[INFO] $*"
}



function rebuild_db {
	logging "studb "

	HOSTNAME="127.0.0.1" #数据库信息
	PORT="3306"
	USERNAME="root"
	PASSWORD="12345678"
	DBNAME="studb"  #数据库名称

	#删除数据库
	delete_sql="drop database ${DBNAME}"
	mysql -h${HOSTNAME}  -P${PORT}  -u${USERNAME} -p${PASSWORD} ${DBNAME} -e "${delete_sql}"
	#创建数据库
	create_db_sql="create database IF NOT EXISTS ${DBNAME}"
	mysql -h${HOSTNAME}  -P${PORT}  -u${USERNAME} -p${PASSWORD} -e "${create_db_sql}"


	# rm -rf "db.sqlite3"
	rm -rf "account/migrations/0001_initial.py"
		
	logging "makemigrations" "account"
	python "manage_mysql.py" "makemigrations" "account"

	logging "migrate"
	python "manage_mysql.py" "migrate"
    
    logging "studb end"

}



#############
# Main
#############
cd ${BASE_DIR}/mysite
OPT_ENV_FORCE=$1

rebuild_db


