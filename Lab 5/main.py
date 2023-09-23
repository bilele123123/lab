#Name: Thai Le, Hoa Nguyen
#Date: 9/22/2023
#Description: This program allows you to move a rectangle around a grid. The user will be able to choose the size fo the rectangle and move the rectangle in any direction. Using the user prompted choices. The user can quit the program anytime by entering the quit option.

from rectangle import Rectangle
from check_input import get_int_range


def display_grid(grid):
  for row in grid:
    print(' '.join(row))
  print()


def reset_grid(grid):
  for i in range(20):
    for j in range(20):
      grid[i][j] = '.'


def place_rect(grid, rect):
  x, y = rect.get_coords()
  width, height = rect.get_dimensions()
  for i in range(height):
    for j in range(width):
      grid[y + i][x + j] = '*'


def main():
  width = get_int_range("Enter rectangle width (1-5): ", 1, 5)
  height = get_int_range("Enter rectangle height (1-5): ", 1, 5)

  rect = Rectangle(width, height)
  grid = [['.' for _ in range(20)] for _ in range(20)]

  place_rect(grid, rect)

  while True:
    display_grid(grid)
    print("Enter Direction:")
    print("1. Up\n2. Down\n3. Left\n4. Right\n5. Quit")

    choice = get_int_range("", 1, 5)

    if choice == 1:
      rect.move_up()
    elif choice == 2:
      rect.move_down()
    elif choice == 3:
      rect.move_left()
    elif choice == 4:
      rect.move_right()
    elif choice == 5:
      break
    else:
      print("Invalid choice. Please choose a valid option (1-5).")

    reset_grid(grid)
    place_rect(grid, rect)


if __name__ == "__main__":
  main()
