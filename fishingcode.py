import os

while True: 
     os.system("cls" if os.name == "nt" else "clear") 
     print()
     print("-- Fishing Log App --")
     print()
     print("1. Add a Catch")
     print("2. View Logs")
     #print("3. Search By Species")
     #print("4. Search by Characteristics")
     print("3. Exit")
     print()

     try:
          choice = input("Choose a number (1–3): ").strip().lower()
     except KeyboardInterrupt:
               print("\n\nProgram interrupted\n")
               break

     if choice not in ["1", "2", "3"]:
          print()
          input("-- Invalid choice. Try Again (Press Enter) -- ")
          os.system("cls" if os.name == "nt" else "clear")
          continue
          
     if choice in "1": 
          print("\n-- Add a Catch --\n")
          species = input("Species: ")
          characteristics = input("Characteristics: ")
          weight = input("Weight: ")
          bait = input("Bait Used: ")
          location = input("Location: ")
          time = input("Time: ")
          date = input("Date: ")

          total_output = [species, characteristics, location, time, bait, weight, date] 


          choice2 = input("Press S to SAVE or C to CANCEL: ").strip().lower()

          while choice2 not in ["S", "s", "Save", "save", "c", "C", "Cancel", "cancel"]:
               choice2 = input("Press S to SAVE or C to CANCEL: ").strip().lower()

          if choice2 in ["S", "s", "Save", "save"] and any(total_output):
               import os 

               filename = "fishing_log.csv"

               if not os.path.exists(filename):    # Creates a csv file if it doesn't exist
                    with open(filename, "w") as file:
                         file.write("Species,Characteristics,Weight,Bait Used,Location,Time,Date\n")

               with open(filename, "a") as file: #Puts the values in the CSV file
                    file.write(f"{species},{characteristics},{weight},{bait},{location},{time},{date}\n")
               print("\nSaved\n")
               input("Go back to Main Menu (Press Enter): ")
               os.system("cls" if os.name == "nt" else "clear")
          
          elif choice2 in ["S", "s", "Save", "save"] and not any(total_output):
               print("\n-- Nothing to Save --\n")
               input("Go back to Main Menu (Press Enter): ")
               os.system("cls" if os.name == "nt" else "clear")
          
          elif choice2 in ["C", "c", "Cancel", "cancel"]:
               print("\n-- Canceled --\n")
               input("Go back to Main Menu (Press Enter): ")
               os.system("cls" if os.name == "nt" else "clear")

     if choice in "2":
          print("\n-- Logs --\n")
          print("(Oldest -> Newest)\n")
          
          filename = "fishing_log.csv"

          try:
               with open(filename, "r") as file:
                    next(file)
                    for line in file:
                         data = line.strip().split(",")
                         print("  Species:", data[0] if data[0] else "?")
                         print("  Characteristics:", data[1] if data[1] else "?")
                         print("  Weight:", data[2] if data[2] else "?")
                         print("  Bait Used:", data[3] if data[3] else "?")
                         print("  Location:", data[4] if data[4] else "?")
                         print("  Time:", data[5] if data[5] else "?")
                         print("  Date:", data[6] if data[6] else "?")
                         print()
                    print("(End of logs)")
                    print()
                    input("Go back to Main Menu (Press Enter): ")
                    os.system("cls" if os.name == "nt" else "clear")
          except:
               print("No logs found yet.")
               print()
               input("Go back to Main Menu (Press Enter): ")
               os.system("cls" if os.name == "nt" else "clear")

     if choice in "3":
          print()
          print("-- Goodbye! --")  
          print()        
          break