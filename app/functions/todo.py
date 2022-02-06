
import json
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
    try:
        checktask = list(filter(lambda x:x["due"]["date"]==date+"T"+hour+":00", list(filter(lambda x:x["content"]==local+' - '+visitor, api.state['items']))))
        if not checktask:
            api.items.add(content=local+' - '+visitor, project_id=getProjectId(competition), due={"date": date+"T"+hour+":00"}, priority=priority, description=channel)
            json_task = '{"local": "'+local+'", "visitor": "'+visitor+'", "competition": "'+competition+'", "date": "'+date+'", "hour": "'+hour+'", "channel": "'+channel+'"}'
            json_parsed = json.loads(json_task)
            print(json.dumps(json_parsed, indent=2, ensure_ascii=False))
            api.commit()
    except:
        print("No se ha podido añadir el siguiente partido: "+local, visitor, competition, date, hour, priority, channel)
