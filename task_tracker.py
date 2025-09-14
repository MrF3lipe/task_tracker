import os
import json
from datetime import datetime 

class TaskManager:

    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self) -> None:
        if os.path.exists(self.filename):
            try:
                if os.path.getsize(self.filename) == 0:
                    print("Archivo vacío. Creando nueva lista de tareas.")
                    self.tasks = []
                    self.save_tasks()
                    return
                
                with open(self.filename, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    if isinstance(data, dict) and 'tasks' in data:
                        self.tasks = data.get('tasks', [])
                    elif isinstance(data, list):
                        self.tasks = data
                    else:
                        print("Estructura del archivo inválida. Creando nueva lista.")
                        self.tasks = []
                        self.save_tasks()
                
                print(f"Tareas cargadas desde {self.filename}")
                
            except (json.JSONDecodeError, FileNotFoundError) as e:
                print(f"Error al cargar el archivo: {e}. Creando nueva lista de tareas.")
                self.tasks = []
                self.save_tasks()
        else:
            print(f"Archivo {self.filename} no encontrado. Creando nuevo archivo.")
            self.tasks = []
            self.save_tasks()

    def save_tasks(self, filename="tasks.json"):
        with open(filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, name: str):
        
        now = datetime.now().isoformat()

        task = {
            'id': len(self.tasks)+1,
            'name': name,
            'create_date': now,
            'update_date': now,
            'progress': 'todo'
        }

        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def update_time(self, id: int):
        now = datetime.now().isoformat()

        self.tasks[int(id)]['update_date'] = now

    def update_task(self, id: int, name: str):
        self.update_time(id)

        self.tasks[int(id)]['name'] = name
        self.save_tasks()

    
    def delete_task(self, id: int):
        id = int(id)

        if id >= len(self.tasks):
            print("Command Error")
            return

        del self.tasks[id]
        for i, t in enumerate(self.tasks):
            t['id'] = i
        
        self.save_tasks()
    
    def delete_all(self):

        self.tasks = []
        
        self.save_tasks()

    def mark_in_progress(self, id: int):
        self.update_time(id)

        self.tasks[int(id)]['progress'] = 'in-progress'

    
    def mark_done(self, id: int):
        self.update_time(id)

        self.tasks[int(id)]['progress'] = 'done'


    def list(self, flag: str = 'none'):

        for t in self.tasks:
            if flag == 'none':
                print(t['id'], t['name'], t['progress'])
            elif flag == t['progress']:
                print(t['id'], t['name'], t['progress'])


if __name__ == "__main__":

    manager = TaskManager()

    while True:
        
        inp = input()
        option = inp.split()

        if not len(option):
            print("Command Error")

        elif option[0] == "add":
            t = inp.split(' ', 1)
            t = t[1].strip('"\'')
            manager.add_task(t)

    
        elif option[0] == "update" and len(option) >= 2 and int(option[1]) < len(manager.tasks):
            t = inp.split(' ', 2)
            t = t[2].strip('"\'')
            manager.update_task(option[1],t)

        elif option[0] == "delete" and len(option) == 2:
            if option[1] == ".":
                manager.delete_all()
            else:
                manager.delete_task(option[1])
        
        elif option[0] == "mark-in-progress" and len(option) == 2:
            manager.mark_in_progress(option[1])

        elif option[0] == "mark-done" and len(option) == 2:
            manager.mark_done(option[1])

        elif option[0] == "list" and len(option) == 1:
            manager.list()
        
        elif option[0] == "list" and len(option) == 2:
            manager.list(option[1])

        elif option[0] == "end" and len(option) == 1:
            break

        else:
            print("Command Error")
