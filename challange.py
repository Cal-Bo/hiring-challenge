key = ""
maxLength = 0

with open("space_missions.log", "r") as f:
  for line in f:
    ar = [item.strip() for item in line.split('|')]
      maxLength = int(ar[4])
      key = str(ar[7])
return key
    
