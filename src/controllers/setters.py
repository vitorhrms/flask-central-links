from src.connections.escalationdb import connectToEscalationDB


def addUrl(URL_name:str, URL_link:str, team_id:int) -> bool:
    try:
        query = '''insert into URLs 
        (URL_name, URL_link, team_id)
        values ('{}', '{}', {})
        '''.format(URL_name, URL_link, team_id)
        conn = connectToEscalationDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        print("Erro ao adicionar URL")
        return False

def deleteTeamByID(URL_id):
    try:
        query = '''delete from URLs 
                where URL_id = {}
                '''.format(URL_id)
        conn = connectToEscalationDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        print("Erro ao deletar URL")
        return False
