
from todoist_api_python.api import TodoistAPI
from settings import todoist_token
import re
import time

api = TodoistAPI(todoist_token)

def getProjectId(project_name):
    if project_name == "null":
        project_name = "Fútbol"
    for project in api.get_projects():
        if re.search(project_name, str(project)):
            regex = re.findall(" id='[0-9]+'", str(project))
            for id in regex:
                return(id.strip().split("'")[1])

def getTaskId(task_name):
    for task in api.get_tasks():
        if re.search(task_name, str(task)):
            regex = re.findall(" id='[0-9]+'", str(task))
            for id in regex:
                return(id.strip().split("'")[1])

def addTask(local, visitor, competition, date, hour, priority, channel, matches):
    try:
        if not getTaskId(local+' - '+visitor):
            print("Se añadió el siguiente partido: "+local, visitor, competition, date, hour, priority, channel)
            api.add_task(content=local+' - '+visitor, project_id=getProjectId('Fútbol'), due_date=date+"T"+hour+":00", priority=priority, description=channel, labels=[competition])
            json_task = {"local": ""+local+"", "visitor": ""+visitor+"", "competition": ""+competition+"", "date": ""+date+"", "hour": ""+hour.strip()+"", "channel": ""+channel+""}
            matches.append(json_task)
    except:
        print("No se ha podido añadir el siguiente partido: "+local, visitor, competition, date, hour, priority, channel)

def deleteExpiredTasks():
    for task in api.get_tasks(project_id=getProjectId('Fútbol')):
        if time.strftime("%Y-%m-%d") > task.due.date:
            print("Se ha eliminado el siguiente partido: "+task.content, task.due.date)
            api.delete_task(task.id)
