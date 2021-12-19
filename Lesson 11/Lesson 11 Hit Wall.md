```python

def hit_wall():
  global current_health_point   #as we need to modify this global variable, we need to declare it as global
  current_health_point -= 1
  if current_health_point > 0:
    print(hit_wall_msg)
    print("Your remaining health point is", current_health_point)
    return "OK"
  else:
    print("You have used up all your health point!")  
    print("Gameover")
    return "GAMEOVER"

```
