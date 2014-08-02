#ye olde tower of hanoi
def tower_of_hanoi(n, start, end):
  if n == 1:
    move_disc(start, end)
  else:
    move_disc(start, end)
    move_disc(start, 2)
    move_disc(end, 2)
    tower_of_hanoi(n - 1, start, end)
  

def move_disc(start, end):
  print("Move 1 disk from rod " + start + "to rod" + end)
