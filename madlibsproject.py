def mad_libs():
    print("Welcome to MAD LIBS!")
    while True:
        # Ask the user for words
        noun = input("Enter a noun: ")
        verb = input("Enter a verb: ")
        adjective = input("Enter an adjective: ")
        adverb = input("Enter an adverb: ")
        # Create the story
        print("\nHere is your story:")
        print(f"The {adjective} {noun} likes to {verb} {adverb} every day.\n")
        # Ask if they want to play again
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Start the game
mad_libs()
