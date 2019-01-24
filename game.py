import random
name=input("What Is Your Name :")
print("Hello "+name+" It's Time to Play Hangman")
print ("Here are the Rules..")

print("1.You Will be guessing a word on the basis of the topic given by me")

print("2.You will keep guessing the letters of the word until you complete the word")

print("3. At the end of the game you will be shown the correct answer with the no of tries you used to finish to complete the word")
wordcollec = ["COW","BUFFALO","SHEEP","HORSE","GOAT","CROCODILE","ELEPHANT","CAT","DOG","LION","BIRD","BEAR","TIGER","RABBIT","FOX","SQUIRREL","DEER","HIPPOPOTAMUS","PIG"]
random.shuffle(wordcollec)
correctAnswer = list(wordcollec[0])
print("YOUR TOPIC IS ANIMAL NAMES :")
display=[]
display.extend(correctAnswer)

for i in range(len(display)):
	display[i] = "_"

print (' '.join(display))

count = 0 
while count < len(display):
	user_input = input("Guess The Word :")
	user_input = user_input.upper()

	for i in range(len(display)) :
		if correctAnswer[i]== user_input:
			display[i] =user_input
			count = count + 1
			print (''.join(display))
			print ("You Guessed the Word!!!")
		


			






