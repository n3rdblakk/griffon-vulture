import mysql as mysql
import mysql.connector as db_driver

from application.database.utility.defaults import DbConfig


class Manager:

    def __init__(self, db_username, db_password, db_name, db_host_ip):

        self.db_username = db_username
        self.db_password = db_password
        self.db_name = db_name
        self.db_host_ip = db_host_ip

        self.db_connection = db_driver.Connect(user=db_username, password=db_password,
                                               host=db_host_ip, database=db_name)

    def get_db_conn(self):
        print("Retrieving Database Connection")
        return self.db_connection

