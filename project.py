import csv
import random

# Dictionary of countries and capitals
capital_cities = {
    "Australia": "Canberra",
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasilia",
    "Canada": "Ottawa",
    "Germany": "Berlin",
    "Italy": "Rome",
    "India": "New Delhi",
    "Mexico": "Mexico City",
    "Egypt": "Cairo",
    "New Zealand": "Wellington",
    "Russia": "Moscow",
    "China": "Beijing",
    "United Kingdom": "London",
    "Ukraine": "Kyiv",
    "Sweden": "Stockholm",
    "United States": "Washington DC",
    "South Korea": "Seoul",
    "Bandladesh": "Dhaka",
    "North Korea": "Pyongyang",
    "United Arab Emirates": "Abu Dhabi",


}

# Welcome Page
welcome_page = input("Welcome to the Capital City Game! Press 1 to start, Press 2 to quit: ")

# Loop until valid input
while welcome_page != "1" and welcome_page != "2":
    print("Invalid input. Please try again.")
    welcome_page = input("Welcome to the Capital City Game! Press 1 to start, Press 2 to quit: ")

# Start the game
if welcome_page == "1":
    print("Starting the game...\n")

    get_username = input("Please enter your username: ")
    print(f"Hello {get_username}! Let's see how well you know your capital cities.\n")
    print("\033[92mThere is a total of 20 questions, lets see how many you can get right.\033[0m\n")
    print("At Any time type \033[91mexit\033[0m to quit the game.")
    print(" ")
    
    
    # Create a list of countries to track which ones have been asked
    available_countries = list(capital_cities.keys())
    
    # Initialize score counter
    score = 0

    # Write CSV header once at start
    with open('quiz_answers.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([])
        writer.writerow(["Username", "Country", "User Answer", "Correct Answer", "Result"])
        writer.writerow([])

    # Output 20 random questions
    for i in range(20):
        with open('quiz_answers.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            country = random.choice(available_countries)
            available_countries.remove(country)  # Remove the country to avoid repetition
            
            user_answer = input(f"What is the capital city of {country}? ").strip().lower()

            # Check if the user wants to exit
            if user_answer == "exit":
                print("Exiting the game.")
                break

            # Compare answers in lowercase to make it case-insensitive
            if user_answer == capital_cities[country].lower():
                print("Correct! 🎉\n")
                score += 1  # Increment score
            else:
                print(f"Wrong! The correct answer is {capital_cities[country]}.\n")
            writer.writerow([get_username, country, user_answer, capital_cities[country], "Correct" if user_answer == capital_cities[country].lower() else "Wrong"])

    # Show final score
    print(f"You got {score} out of 20 correct!")
    print("Thanks for playing!")

elif welcome_page == "2":
    print("Thanks for visiting! Goodbye!")
    exit()