import psycopg2
from Scraping import Spider

class DBStroring():
    def store(self, gen):
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="tina",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="dataset")
            cursor = connection.cursor()
            query = """ INSERT INTO items (title, latest) VALUES (%s,%s)"""
            for item in gen:
                record = (item["title"], "latest")
                cursor.execute(query, record)
                connection.commit()
                count = cursor.rowcount
            print (" succesful insertion into DB ")
        except (Exception, psycopg2.Error) as error :
                if(connection):
                    print("Failed to insert record into items", error)
        finally:
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

a= Spider()
s=DBStroring()
g=a.parse("https://www.data.gouv.fr/api/1/datasets/?page=3000&page_size=1")
s.store(g)
