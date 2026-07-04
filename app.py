from datetime import datetime

print("Python artifact demo")

with open("results.txt","w") as file:
  file.write("Hello from github \n")
  file.write("This file is generated dynamically \n")
  file.write(f"Genrated Time :{datetime.now()}")

print("results.txt file is created successfully")
