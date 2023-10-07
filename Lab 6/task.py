class Task:

  def __init__(self, desc, date, time):
    self.description = desc
    self.date = date
    self.time = time

  def __str__(self):
    return f"{self.description} - Due: {self.date} at {self.time}"

  def __repr__(self):
    return f"{self.description},{self.date},{self.time}"

  def __lt__(self, other):
    if self.date != other.date:
      return self.date < other.date
    elif self.time != other.time:
      return self.time < other.time
    else:
      return self.description < other.description
