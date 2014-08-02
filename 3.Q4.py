#ye olde tower of hanoi
def tower_of_hanoi(n, start, end):
  def mid_mk(startr):
    if startr ==1:
      return lambda x: 3 if x == 2 else 2
    elif startr == 2:
      return lambda x: 3 if x == 1 else 1
    else: #startr must be 3
      return lambda x: 2 if x == 1 else 1
  if start == end:
    return
  elif n == 1:
    move_disc(start, end)
  else:
    mid = mid_mk(start)(end)
    tower_of_hanoi(n - 1, start, mid)
    tower_of_hanoi(1, start, end)
    tower_of_hanoi(n - 1, mid, end)

def move_disc(start, end):
  print("Move 1 disk from rod " + str(start) + " to rod " + str(end))# your code goes here
  
move_disc(1, 3)
#should print Move 1 disk from rod 1 to rod 3
move_disc(2, 3)
#should print Move 1 disk from rod 2 to rod 3
print("Full Hanoi?")
print("Test 1,1,3")
tower_of_hanoi(1, 1, 3)
print("Test 2,1,3")
tower_of_hanoi(2, 1, 3)
print("Test 2,1,2")
tower_of_hanoi(2,1,2)
print("Test 2,2,3")
tower_of_hanoi(2, 2, 3)
print("Test 3,1,3")
tower_of_hanoi(3,1,3)
#It's perfect now.
