#this needs to prompt the user for a sentence .
#it will need to convert all the words to lowercase, delete all punctuation before counting the words, and delete any leading or trailing whitespace.
#then it will make a list of all indivaidual words in the sentence and print that list out without repetitions while still counting it for the total number of words.
#with that list it will find the avrage length of the words and the total number of words in the sentence.
#finaly it will display it clearly to the user in a nice format.
import string

sentence = input("Please enter a sentence or paragraph: ").strip().lower()
sentence = sentence.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
all_words = sentence.split()
unique_words = list(set(sentence.split()))
if len(all_words) > 0:
    total_word_length = sum(len(word) for word in all_words)
    average_word_length = sum(len(word) for word in all_words) / len(all_words)
print("Words in the sentence:", unique_words)
print("Average word length:", average_word_length)
print("Total number of words:", len(all_words))
