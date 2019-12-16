string = "Hello Agnosticdev, I love Tutorials e foram felizes para sempre"
substring = "e nunca foram felizes"
 
# Straight forward approach for Python 2.7 and Python 3.6
# Executes the conditional statement when the substring is found
if substring in string:
	print ("Your substring was found!") 

else:
    print ("Your substring was not found!")