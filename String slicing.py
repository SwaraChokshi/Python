name = 'Swara Chokshi '

print(name[0])

print(name[0:4])

length = len(name)

#this is gonna print the string with jump of 2 
print(name[0:length:2])

#this will also oprint the whole string with jump of 2 
print(name[::2])

#this will take default starting point as -1 and ending as -length +1 
# -length +1 is that you have calculated your length and from backward ad when you wirte at the ending point the last isalways exculed so we add 1 to it
 
print(name[::-1])