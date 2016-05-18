#!/usr/bin/python

from ConfigParser import ConfigParser
import subprocess

config = ConfigParser()
config.read('credentials')

user = config.get('credentials', 'user')
password = config.get('credentials', 'password')

databasesRaw = subprocess.check_output('mysql -u {} -e \'show databases;\''.format(user), shell=True)

databases = databasesRaw.split()
excludeDb = ['Database', 'mysql', 'phpmyadmin', 'information_schema', 'performance_schema']
databases = [db for db in databases if db not in excludeDb]

for dbName in databases:
    subprocess.call('mysqldump -u {} {} > {}.sql'.format(user, dbName, dbName), shell=True)
