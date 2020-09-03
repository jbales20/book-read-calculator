# This input asks for the user's average reading speed
readSpeed = input("What is your average reading speed in words per minute? ")
#This asks for the user the amount of pages in the book
pages = input("What is the amount of pages in the book? ")
#This asks the user a rough estimate for the amount of words per page.
wordsPpage = input("Give me a rough estimate about the amount of words per page. ")


#The script calculates it here.
aprox = (int(pages)*int(wordsPpage))/int(readSpeed)

#This script converts the minutes into hours.
minutes = aprox%60
hours = (aprox - minutes)/60

print("The book will take you about " + str(hours) + " hours and " + str(minutes) + " minutes to read.")
