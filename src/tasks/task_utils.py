from prefect import task
from config import config
from mysql import connector


@task(name="Inicializar la tabla de usuario")
def task_init_table():
  try: 
    with connector.connect(**config.MYSQL_CONFIG) as db:
      with db.cursor() as cursor:
          query_drop_table = "drop table if exists usuario"

          cursor.execute(query_drop_table)
          db.commit()

          query_create_table = """
          create table if not exists usuario(
            id int auto_increment primary key,
            ruc varchar(11),
            razon_social varchar(255),
            direccion varchar(255)
          )
          """
          cursor.execute(query_create_table)
          db.commit()
  except Exception as error:
     print("error: ", error)


@task(name="Consultar la existencia de un usuario en la db")
def task_get_user_from_db(ruc):
   with connector.connect(**config.MYSQL_CONFIG) as db:
      with db.cursor() as cursor:
         query_select_one = "select * from usuario where ruc = %s"
         cursor.execute(query_select_one, (ruc,))
         user = cursor.fetchone()
         return user