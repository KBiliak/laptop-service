
def post_laptop(mysql, laptop):
    with mysql.connection.cursor() as cursor:
        sql = f"insert into laptop(name, year) value('{laptop['name']}', {laptop['year']})"
        cursor.execute(sql)
        mysql.connection.commit()

def get_laptop(mysql):
    with mysql.connection.cursor() as cursor:
        sql = f"Select * from laptop"
        cursor.execute(sql)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            laptop = {
                "id": row[0],
                "name": row[1],
                "year": row[2]
            }
            result.append(laptop)
    return result

def delete_all_laptops(mysql):
    with mysql.connection.cursor() as cursor:
        sql = f"delete from laptop"
        cursor.execute(sql)
        mysql.connection.commit()


def delete_id_lap(mysql,id):
    with mysql.connection.cursor() as cursor:
        sql = f"delete from laptop where id = {id}"
        cursor.execute(sql)
        mysql.connection.commit()

def update_lap(mysql, id, laptop):
    with mysql.connection.cursor() as cursor:
        sql = f"update laptop set name = '{laptop['name']}', year = {laptop['year']} where id = {id}"
        cursor.execute(sql)
        mysql.connection.commit()