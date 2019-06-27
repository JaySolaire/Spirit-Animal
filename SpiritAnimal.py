'''
Overview:
This is a program that I aimed to create as a joke to determine one's spirit animal. Rather than generating a normal one such as Wolf or Eagle, it 
pulls a random animal name from the complete list of all species in the world.
The problem: 
I don't have the file that contains all the animals in the world. I got close with the Catalog of Life, but haven't fully parsed that out yet.

Code:
The project might take two routes, depending on efficiency.
One is, if the number of lines in the file is known, to simply generate a random number between (1, numLines) and read off that line.
The second is to read in the entire file, line by line, get the number of lines, and then pull a random one after.
The second way is less efficient because 
	1. It needs to read in the whole file
	2. It will need to store the data in an array or method of some sort in order to instantly retrieve one line after reading in the whole file, else it will need to read in the whole file and then resort to method 1 after.
UNLESS there is a way to instantly retrieve any line number from a file, such as GetLine(filename, linenumber), but I haven't looked into this option (mostly because I haven't had a reason to follow up on this project without the list of species names.

Next Steps:
After coding a project that prints ("Your spirit animal is [insert name]"), there are a couple steps I could take
	1. Add a google function. After printing the name of the animal, it will attempt to pull up a webpage with a google search of the name and/or a picture from google images
	2. Turn the code into a website. Realistic Spirit Animal Generator.
'''


import rand

#open Names.txt

sizeOfFile = 999
nameLine = random.randint(0,sizeOfFile-1)
i = 0
while (i < nameLine)
	#read in line from 