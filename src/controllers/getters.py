from src.connections.escalationdb import connectToEscalationDB


def getAllTeams() -> list:
    query = ''' select * from teams 
            order by team_name asc
            '''
    conn = connectToEscalationDB()

    conn.execute(query)
    teams = conn.fetchall()
    conn.commit()
    conn.close()

    return teams

def getTeamNameByID (teamID: int) -> str:
    query = ''' select team_name from teams where team_id = {} '''.format(teamID)
    conn = connectToEscalationDB()

    conn.execute(query)
    teamName = conn.fetchone()
    conn.commit()
    conn.close()

    try:
        return teamName[0]
    except:
        return ""

def getUrlsByID(teamID) -> list:
    query = ''' select * from URLs 
            where team_id={}
            '''.format(teamID)
    conn = connectToEscalationDB()

    conn.execute(query)
    urls = conn.fetchall()
    conn.commit()
    conn.close()
    try:
        return urls
    except:
        return None