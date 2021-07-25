class Task:
    """
    A task is used for the coding club to practise or complete with.
    """

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def info(self):
        if self.id == 0:
            return "Please create a task"
        return f"""
        Task id: {self.id}
        Task name: {self.name}
        """
