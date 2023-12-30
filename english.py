import time
import random
from plyer import notification
import nltk

# Download the words dataset from nltk (run this once)
nltk.download('words')

def generate_random_word():
    word_list = nltk.corpus.words.words()
    return random.choice(word_list)

if __name__ == "__main__":
    while True:
        # Generate a random English word
        random_word = generate_random_word()

        # Display notification with the random word
        notification.notify(
            title="Please drink water now",
            message=f"You are on a certain cycle. Please drink 6 liters of water. Also, your random english word is: {random_word}",
            timeout=8  # Set timeout in seconds
        )

        # Wait for the next notification after 1 hour
        time.sleep(60*60)
