User = input("User: ")
Reason = input("Reason: ")
Punishment = input("Punishment: ")
Reference = input("Reference: ")

with open ('pendings.txt', 'a') as p:
    p.write("\nUser: " + User + "\nReason: " + Reason + "\nPunishment: " + Punishment + "\nReference: " + Reference + "\n")

print("\nUser: " + User + "\nReason: " + Reason + "\nPunishment: " + Punishment + "\nReference: " + Reference + "\n\nCopy paste ready! Info has also been saved to pendings.txt")
