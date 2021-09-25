from todoist import TodoistAPI
from settings import todoist_token

api = TodoistAPI(todoist_token)
api.sync()

def getProjectId(project_name):
    try:
        project_id = list(filter(lambda x:x["name"]==project_name, api.state['projects']))
        return(project_id[0]['id'])
    except:
        project_id = list(filter(lambda x:x["name"]=="Fútbol", api.state['projects']))
        return(project_id[0]['id'])

def addItem(local, visitor, competition, date, hour, priority, channel):
    item = api.items.add(content=local+' - '+visitor, project_id=getProjectId(competition), due={"date": date+"T"+hour+":00"}, priority=priority, description=channel)
    api.commit()
