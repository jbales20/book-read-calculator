# Option A -------------------------------------------------------------------------------------------------
def optionA():
    # Finds out the users' prefered reading time.
    time = input("How many days do you have to finish the reading? ")
    timeRequest = input("How many days a week do you wish to read? ")
    # Calls the function Reading and sets the two return values to minutes and hours.
    minutes, hours = reading()
    print()
    #Converts time value into weeks value
    weeks = int(time)/7
    #Calculates how many days you are and are not reading based off time and timeRequest
    daysNotReading = abs((int(timeRequest)*weeks) - int(time))
    daysNotReading = daysNotReading - (daysNotReading%1)
    daysReading = int(time) - int(daysNotReading)
    #Gets the total minutes for reading
    minutes = minutes + (hours*60)
    #Gets the amount of minutes for each day. Cast as int to round it
    minsPerDay = int(minutes/daysReading)+1
    print("The book will take around " + str(minsPerDay) + " minutes each day, for you to read across " + str(daysReading) + " days of reading.")
# Option A -------------------------------------------------------------------------------------------------


# Option B --------------------------------------------------------------------------------------------------
def optionB():
    #This calls the function reading and sets it to the two variables listed.
   minutes, hours = reading()
   #Blank Line
   print()
   #Prints the results
   print("The book will take you about " + str(hours) + " hours and " + str(minutes) + " minutes to read.")

# Option B --------------------------------------------------------------------------------------------------

#Reading Time
def reading():
    # This input asks for the user's average reading speed
    readSpeed = input("What is your average reading speed in words per minute? ")
    #This asks for the user the amount of pages in the book
    pages = input("What is the amount of pages in the book? ")
    #This asks the user a rough estimate for the amount of words per page.
    wordsPpage = input("Give me a rough estimate about the amount of words per page. ")
    #The script calculates it here.
    aprox = (int(pages)*int(wordsPpage))/int(readSpeed)
    #Line below gets the remaining minutes, the one below that subtracts it from total to get the total hours in minutes and then converts into hours.
    minutes = int(aprox%60)
    hours = int((aprox - minutes)/60)
    return minutes, hours



choice = input("Create A Reading Schedule or need an estimate for how long it'll take to read (Type '1' or '2' to choose) ")
# Determines which option the user chooses. 
if choice == "1":
    print()
    optionA()

if choice == "2":
    print()
    optionB()

