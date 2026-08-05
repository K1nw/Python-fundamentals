import random

words = ["apple", "banana", "cherry", "date", "elderberry"]
lives = 6

secret_word = random.choice(words)
hidden_word = ["_"] * len(secret_word)

print ("Welcome to the Word Guessing Game!")
print(f"The word has {len(secret_word)} letters.")
print(f"Hidden word: {' '.join (hidden_word)}")

while lives > 0 and "_" in hidden_word:
    guess = input("Digite uma letra: ").lower()
    if guess in secret_word:
        for i in range(len(hidden_word)):
            if secret_word[i] == guess:
                hidden_word[i] = guess
                print(" ".join(hidden_word))
    else:
        lives = lives - 1
        print(f"Wrong letter, try again. lives = {lives}")
if "_" not in hidden_word:
    print("Parabéns, você ganhou!")
else:
    print(f"Você perdeu. A palavra era: {secret_word}")
