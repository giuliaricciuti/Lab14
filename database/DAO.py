from database.DB_connect import DBConnect
from model.Order import Order
from model.store import Store


class DAO():
    @staticmethod
    def getAllStores():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM stores"
        cursor.execute(query)

        for row in cursor:
            result.append(Store(**row))
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getOrdersStore(store):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                    FROM orders o 
                    WHERE o.store_id = %s"""
        cursor.execute(query, (store,))

        for row in cursor:
            result.append(Order(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(store_id, days):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT o1.order_id, o2.order_id
                    FROM orders o1, orders o2
                    WHERE o1.store_id = o2.store_id
                    AND o1.store_id = %s
                    AND o1.order_id < o2.order_id
                    AND DATEDIFF(o2.order_date, o1.order_date) BETWEEN 1 AND %s-1
                    """
        cursor.execute(query, (store_id, days))

        for row in cursor:
            result.append((row[0], row[1]))
        cursor.close()
        conn.close()
        return result