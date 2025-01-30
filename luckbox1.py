while True:
        total_games += 1
        print("\nWelcome to the Lucky Box Game! Choose a box (1-6):")
        
        # Randomly assign awards to the 6 boxes
        contents = random.sample(awards, 6)
        
        try:
            choice = int(input("Enter your box number (1-6): "))
            if 1 <= choice <= 6:
                prize = box_contents[choice - 1]
                print(f"Congratulations! You won {prize}!")
                total_wins += 1
            else:
                print("Invalid choice. Please pick a number between 1 and 6.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue
        
        print(f"Games Played: {total_games} | Wins: {total_wins}")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print(f"Thanks for playing! You played {total_games} games and won {total_wins} times. See you next time!")
            break


