# Task Tracker CLI (Interfaz de Línea de Comandos)

Task Tracker CLI es una herramienta que permite gestionar tareas mediante una aplicación de línea de comandos. Los usuarios pueden agregar, actualizar, marcar y eliminar tareas almacenadas en un archivo JSON, así como visualizar listas de tareas según su estado.

## Características

- **Agregar Tareas**: Permite añadir una nueva tarea con una descripción.
- **Actualizar Tareas**: Modifica la descripción de una tarea existente utilizando su ID.
- **Eliminar Tareas**: Borra una tarea existente utilizando su ID.
- **Marcar Tareas**: Cambia el estado de una tarea a "in progress" o "done" según su ID.
- **Listar Tareas**: Muestra las tareas según su estado (todo, in progress, done).

## Uso

Primero se ejecuta la aplicacion con

```bash
python task_tracker.py
```

### Agregar Tarea

Para agregar una tarea se utiliza `add`

```bash
add "Nombre de tarea"
```

### Actualizar Tarea

Para actualizar una tarea se utiliza `update`

```bash
update ID "Nuevo nombre de la tarea"
```

### Eliminar Tarea

Para eliminar una tarea se utiliza `delete`

```bash
delete ID
```

Tambien se pueden eliminar todas las tareas utilizando

```bash
delete .
```

### Marcar Tarea

Para cambiar el estado de una tarea se usa `mark-in-progress` o `mark-done`

```bash
mark-in-progress ID
mark-done ID
```

### Listar Tareas

Las tareas se pueden listar con `list` y si se quiere especificar entonces se usaría el estado

```bash
list
list done
```

### Salir

Para finalizar la aplicación puedes usar

```bash
end
```

Proyecto basado en https://roadmap.sh/projects/task-tracker
