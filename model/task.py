class Task:

    def __init__(self, task_id: int, title: str, description: str, status: str):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = status


    @property
    def status(self):
        return self._status


    @status.setter
    def status(self, status_val):
        if status_val not in ["pending", "done"]:
            raise Exception("Status must be either 'pending' or 'done'")
        self._status = status_val


    def __str__(self):
        return f"""
\tId:     {self.id}
\tTitle:  {self.title}
\tStatus: {self.status}
\t___________________________________________
\t{self.description}\n
"""
