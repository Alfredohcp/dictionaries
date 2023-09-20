def learn_dictionaries():
  
    #######################################Dictionaries###############################
#    capitals = {"USA" : "Washington D.C",
#          "India" : "New delhi",
#          "China" : "Beijijng",
#          "Russia" : "Moscow" }
# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))
# print(capitals.get("China"))
# print(capitals.get("India"))
    # Dictionaries Practice #1
  # Create a dictionary called fruits with the following key-value pairs:
  # apple --> red
  # banana --> yellow
  # mango --> green
  # cherry --> red
  # watermelon --> green
  # Display the dictionary on the screen.
      fruits = {"apple" : "red",
            "banana" : "yellow",
            "mango" : "green",
            "cherry" : "red" ,
            "watermelon" : "green"}
print(fruits["apple"])
print(fruits["banana"])
print(fruits["mango"])
print(fruits["cherry"])
print(fruits["watermelon"])
    # Dictionaries Practice #1
    # Create a dictionary called my_dict that stores the following information about a person:
    # name: Karen
    # surname: Jurgens
    # age: 35
    # occupation: Journalist
    # The names of the keys and values must be equal to the ones indicated above.
my_dict={"name": "Karen",
    "surname": "Jurgens",
    "age": "35",
    "occupation": "Journalist"}
    
    #   Dictionaries Practice #2
    # Use print to returns the second item of the list called points2, inside the following dictionary.
    # If the value 300 were to change in the future, the code should work the same to return the value at that same position. To do this, you must refer to the names of the keys and/or indexes as appropriate.
my_dict2 = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
print(my_dict2["points"]["points2"][1]) 
  # Dictionaries Practice #3
  # Update the information in our dictionary called my_dict (reassigning new values to the keys as appropriate), and add a new key called "country" (without a tilde). The new data is:
  # name: Karen
  # surname: Jurgens
  # age: 36
  # occupation: Editor
  # country: Colombia
  # to do this, you should not change the line of code already written, but update the values using dictionary methods.
  # my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}
  