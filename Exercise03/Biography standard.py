#Define personal information variables
Name = "Farah"  #the name as a string
Hometown = "Pakistan"    #Hometown in string form
Age = 18                 #Age expressed as an integer

#Keep data in a dictionary using descriptive keys.
info = {
    "Name": Name,        #Enter "Name" as the key value.
    "Hometown": Hometown, #Enter the value of "Hometown" in the key.
    "Age": Age            #Enter "Age" along with the age value.
}

#Print a new line for each piece of information.
print(f"{info['Name']}\n{info['Hometown']}\n{info['Age']}")
