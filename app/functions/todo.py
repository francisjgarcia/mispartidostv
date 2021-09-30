from todoist import TodoistAPI
from settings import todoist_token

api = TodoistAPI(todoist_token)
api.sync()

def getProjectId(project_name):
    if project_name == "null":
        project_name = "Fútbol"
    project_id = list(filter(lambda x:x["name"]==project_name, api.state['projects']))
    return(project_id[0]['id'])

def addTask(local, visitor, competition, date, hour, priority, channel):
    checktask = list(filter(lambda x:x["due"]["date"]==date+"T"+hour+":00", list(filter(lambda x:x["content"]==local+' - '+visitor, api.state['items']))))
    if not checktask:
        api.items.add(content=local+' - '+visitor, project_id=getProjectId(competition), due={"date": date+"T"+hour+":00"}, priority=priority, description=channel)
        api.commit()
