def steps(number: int):
  step_counter = 0
  if number == 0:
    raise ValueError("Only positive integers are allowed")
  elif number < 0:
    raise ValueError("Only positive integers are allowed")
    
  while True:
    number = int(number)

    if number == 1:
      return step_counter
      break
    elif number % 2 == 0:
      number /= 2
    else:
      number = (number * 3) + 1
      
    step_counter += 1
    
      


