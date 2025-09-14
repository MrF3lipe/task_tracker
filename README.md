# Task Tracker CLI (Interfaz de Línea de Comandos)

Task Tracker CLI es una herramienta que permite gestionar tareas mediante una aplicación de línea de comandos. Los usuarios pueden agregar, actualizar, marcar y eliminar tareas almacenadas en un archivo JSON, así como visualizar listas de tareas según su estado.

## Características

- **Agregar Tareas**: Permite añadir una nueva tarea con una descripción.
- **Actualizar Tareas**: Modifica la descripción de una tarea existente utilizando su ID.
- **Eliminar Tareas**: Borra una tarea existente utilizando su ID.
- **Marcar Tareas**: Cambia el estado de una tarea a "in progress" o "done" según su ID.
- **Listar Tareas**: Muestra las tareas según su estado (todo, in progress, done).

## Uso

### Agregar Tarea

Para agregar una tarea se utiliza `add`

```bash
pytho task_tracker.py add "Nombre de tarea"
```

### Actualizar Tarea

Para actualizar una tarea se utiliza `update`

```bash
pytho task_tracker.py update ID "Nuevo nombre de la tarea"
```

### Eliminar Tarea

Para eliminar una tarea se utiliza `delete`

```bash
pytho task_tracker.py delete ID
```

Tambien se pueden eliminar todas las tareas utilizando

```bash
pytho task_tracker.py delete .
```

### Marcar Tarea

Para cambiar el estado de una tarea se usa `mark-in-progress` o `mark-done`

```bash
pytho task_tracker.py mark-in-progress ID
pytho task_tracker.py mark-done ID
```

### Listar Tareas

Las tareas se pueden listar con `list` y si se quiere especificar entonces se usaría el estado

```bash
pytho task_tracker.py list 
pytho task_tracker.py list done
```

Proyecto basado en https://roadmap.sh/projects/task-tracker
