##  Python dictionary deep dive
## 
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}


#Retreiving items from dictionary
# print(programming_dictionary["Function"])


#Adding new items to dictionary
programming_dictionary["loop"] = "The action of doing something over and over again"


#Create an empty dictionary
empty_dictionary = {}


##Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)


#Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)


# looping through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


#nesting 
capitals = {
    "France", "Paris",
    "Germany", "Berlin"
}

#Nesting a list in dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgarg"],
}

#testing dictionary in dictionary
travel_log ={    
    "France": {"Cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgarg"],
}    

#nesting dictionary into a list
travel_log =[
    {
        "country":"France",
        "Cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country":"Germany",
        "Cities_visited": ["Berlin", "Hamburg", "Stuttgarg"],
        "total_visits": 8
    },
]    