phonebook = {}

while True:
  command = input("command (1 search, 2 add, 3 quit): ")
  
  if command == "1":
    name = input("name: ")
    if name in phonebook:
      for number in numbers:
        print(number)
    else:
      print("no number")
      
  elif command == "2":
    name = input("name: ")
    number = input("number: ")
    phonebook[name] = number
    print("ok!")

  elif command == "3":
    print("quitting...")
    break