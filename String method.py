name = 'swara chokshi'

#Capitalizes the only first word of the string
#Will not change the original string 
print(name.capitalize())
print(name)

#title will do upper case to every word of he string 
print (name.title())

print(name.upper())

print(name.lower())

#it will give the first occurence of the word
print(name.find('a'))
print(name.index('s'))

#it will give the total number of occurences in the string
print(name.count('a'))

print(name.replace('a','A'))

#splits the content if you have the space in between
print(name.split())
print(name.split('a'))

#the methods will give ans in boolean 

print(name.isupper())

print(name.islower())

print(name.isnumeric())

print(name.isalpha())