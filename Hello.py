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
