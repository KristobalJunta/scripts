#!/usr/bin/python

from ConfigParser import ConfigParser
import subprocess
import os

config = ConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__)) + '/config')

user = config.get('credentials', 'user')
password = config.get('credentials', 'password')
backupPath = config.get('backup_dir', 'path')

databasesRaw = subprocess.check_output('mysql -u{} -p{} -e \'show databases;\''.format(user, password), shell=True)

databases = databasesRaw.split()
excludeDb = ['Database', 'mysql', 'phpmyadmin', 'information_schema', 'performance_schema']
databases = [db for db in databases if db not in excludeDb]

for dbName in databases:
    subprocess.call('mysqldump -u{} -p{} {} > {}/{}.sql &'.format(user, password, dbName, backupPath, dbName), shell=True)
