#Name: Thai Le, Hoa Nguyen
#Date: 10/6/2023
#Description: A Task List program to practice class relationships in Python. This is a command-line based program that allow users to create and manage a task list for daily activities. Users can specify task details, including due date, hour, and time, and mark tasks as complete. The program provides options to display all tasks stored in the file, as well as the capability to make changes to the task list, which will be updated upon user prompt.

from tasklist import Tasklist
from datetime import datetime
from check_input import get_int_range


def main_menu(task_list):
  print("\n-Tasklist-")
  print(f"Tasks to complete: {len(task_list)}")
  print("1. Display current task")
  print("2. Display all tasks")
  print("3. Mark current task complete")
  print("4. Add new task")
  print("5. Save and quit")
  return str(get_int_range("Enter choice: ", 1, 5))


def get_date():
  while True:
    print("Enter due date:")
    month = get_int_range("Enter month: ", 1, 12)
    day = get_int_range("Enter day: ", 1, 31)
    year = get_int_range("Enter year: ", 2000, 3000)
    date = datetime(year, month, day).strftime("%m/%d/%Y")
    return date


def get_time():
  while True:
    print("Enter time:")
    hour = get_int_range("Enter hour: ", 0, 23)
    minute = get_int_range("Enter minute: ", 0, 59)
    time = f"{hour:02d}:{minute:02d}"
    return time


def main():
  task_list = Tasklist()
  while True:
    choice = main_menu(task_list)

    if choice == '1':
      if len(task_list) > 0:
        print(f"Current task is: {task_list[0]}")
      else:
        print("There are no more tasks to complete.")

    elif choice == '2':
      if len(task_list) > 0:
        for index, task in enumerate(task_list):
          print(f"{index + 1}. {task}")
      else:
        print("There are no more tasks to complete.")

    elif choice == '3':
      task_list.mark_complete()
      if len(task_list) > 0:
        print(
            f"Current task marked complete. \nNew current task: {task_list[0]}"
        )
      else:
        print("There are no more tasks to complete.")

    elif choice == '4':
      desc = input("Enter task description: ")
      date = get_date()
      time = get_time()
      task_list.add_task(desc, date, time)
      print("Task added successfully.")

    elif choice == '5':
      task_list.save_file()
      print("Task list saved. Quitting the program.")
      break


if __name__ == "__main__":
  main()
