from task import Task


class Tasklist:

  def __init__(self):
    self.tasklist = []
    self.load_tasks()

  def load_tasks(self):
    with open('tasklist.txt', 'r') as file:
      for line in file:
        desc, date, time = line.strip().split(',')
        task = Task(desc, date, time)
        self.tasklist.append(task)
      self.tasklist.sort()

  def add_task(self, desc, date, time):
    new_task = Task(desc, date, time)
    self.tasklist.append(new_task)
    self.tasklist.sort()

  def mark_complete(self):
    if self.tasklist:
      print(f"Current task is: {self.tasklist[0]}")
      del self.tasklist[0]

  def save_file(self):
    with open('tasklist.txt', 'w') as file:
      for task in self.tasklist:
        file.write(repr(task) + '\n')

  def __getitem__(self, index):
    return self.tasklist[index]

  def __len__(self):
    return len(self.tasklist)
