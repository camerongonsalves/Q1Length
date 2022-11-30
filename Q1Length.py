Loop = "Yes"
Loop = "yes"

while Loop == "Yes" or Loop == "yes":
 word = input("Enter a word: ")  

 howLong = len(word)

 print()

 print ("The word, " + word + ", is", howLong, "characters long.")

 print()
  
 print ("Would you like to enter another word?")
 print ("")
 Loop = input()
 if (Loop) == "yes" or (Loop) == "Yes":
    print ("")
    print ("")
 if (Loop) == "no" or (Loop) == "No":
  print ("")
  print ("Have a nice day!")