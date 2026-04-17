while True: 
     print()
     print("-- Fishing Log App --")
     print()
     print("1. Add Catch")
     print("2. View Logs")
     #print("3. Search By Species")
     #print("4. Search by Characteristics")
     print("3. Exit")
     print()
     choice = input("Choose a number (1-3): ").strip().lower()

     if choice not in ["1", "2", "3"]:
          print()
          print("-- Invalid choice. Try again. --\n")
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
          
          elif choice2 in ["S", "s", "Save", "save"] and not any(total_output):
               print("\n-- Nothing to Save --\n")
          
          elif choice2 in ["C", "c", "Cancel", "cancel"]:
               print("\n-- Canceled --\n")

     if choice in "2":
          print("\n-- Fishing Logs --\n")
          input("Currently being worked on ")
     

     if choice in "3":
          print()
          print("-- Goodbye! --")  
          print()        
          break