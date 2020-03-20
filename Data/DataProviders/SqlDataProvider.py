import pymysql


class SqlDataProvider:
    def __init__(self):
        self.__db_connection = pymysql.connect("localhost", "develop", "Aa123456!", "my_db")

    def __initialize_connection(self):
        self.__db_connection.connect_timeout = 30000000

        return self.__db_connection.cursor(pymysql.cursors.DictCursor)

    def execute_query_command(self, command):
        try:
            cursor = self.__initialize_connection()

            cursor.execute(command)

            return cursor.fetchall()
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()
            self.__db_connection.close()

    def execute_single_value_query_command(self, command, column_name):
        try:
            cursor = self.__initialize_connection()

            cursor.execute(command)

            return cursor.fetchone()[column_name]
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()
            self.__db_connection.close()

    def execute_single_record_command(self, command):
        try:
            cursor = self.__initialize_connection()

            cursor.execute(command)

            return cursor.fetchone()
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()
            self.__db_connection.close()

    def execute_non_query_command(self, command):
        applied = False

        try:
            cursor = self.__initialize_connection()

            cursor.execute(command)
            applied = cursor.rowcount >= 1

        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()
            self.__db_connection.close()

            return applied
