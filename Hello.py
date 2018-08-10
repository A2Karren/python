print("Hello world")
print("I'm going to build a chatbot one day!")

#For Loops

texasCities = ["Houston","Austin","Dallas","San Antonio"]
for texas in texasCities:
    print(texas)


#List of Lists
texasRanking = ["Houston,1","Austin,2","Dallas,3","San Antonio,4"]
finalRanking = []

for rows in texasRanking:
    interimRanking = rows.split(',')
    finalRanking.append(interimRanking)
print(finalRanking)


#Unique Mechanisms in List of Lists
firstCityPair = finalRanking[0]
firstCity = firstCityPair[0]
print(firstCityPair)
print(firstCity)

alternativeCity = finalRanking [1][0]
print(alternativeCity)

#Comparison Operators
print(8 == 8) # True
print(8 != 8) # False
print(8 == 10) # False
print(8 != 10) # True


#List Operations
animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = "space_monster" in animals
print(space_monster_found)

if "cat" in animals:
    print("Cat found")

#Disadvantages of using a list vs. Leveraging Indexes over Dictionaries  is silly
students = ["Tom", "Jim", "Sue", "Ann"]
scores = [70, 80, 85, 75]

indexes = [0,1,2,3]
name = "Sue"
score = 0
for i in indexes:
    if students[i] == name:
        score = scores[i]
print(score)

#Count the number of times that each element occurs in the list named pantry that appears in the code block below. You'll need to:
pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_count = {}

for item in pantry:
    if item in pantry_count:
        pantry_count[item] = pantry_count[item] + 1
    else:
        pantry_count[item] = 1
print(pantry_count)



#To prepare new list of list you have to split it by lines, then commas, and then append to empty list

#Three arguments to a function
wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False


def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False

wonder_woman_in_color = index_equals_str(wonder_woman,2,"Color")
print(wonder_woman_in_color)
