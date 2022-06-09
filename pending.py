User = input("User: ")
Reason = input("Reason: ")
Punishment = input("Punishment: ")
Reference = input("Reference: ")
Title = input("Thread Reason: ")

with open ('pendings.txt', 'a') as p:
    p.write("\nTitle: " + User + " - "  + Title + "\nUser: " + User + "\nReason: " + Reason + "\nPunishment: " + Punishment + "\nReference: " + Reference + "\n")

print("\nTitle: " + User + " - "  + Title + "\nUser: " + User + "\nReason: " + Reason + "\nPunishment: " + Punishment + "\nReference: " + Reference + "\n")

input("Press enter to exit ;)")
