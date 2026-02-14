questions = ["Which planet in our solar system is known as the Red Planet due to the iron oxide on its surface?",
             "What is the primary gas that humans exhale as a waste product of respiration?",
             "What is the process called when a liquid turns into a gas?",
             "How many degrees are there in a perfect circle?",
             "Which of the following is the hardest naturally occurring substance found on Earth?",
             "What is the process by which green plants use sunlight to synthesize nutrients from carbon dioxide and water?",
             "How many seconds are there in exactly one hour?",
             "On the pH scale, a substance with a value of 7 is considered to be:",
             "Which of these marine animals is classified as a mammal rather than a fish?",
             "Which color of visible light has the shortest wavelength?"]

options = [
    ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
    ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"],
    ["A) Condensation", "B) Freezing", "C) Melting", "D) Evaporation"],
    ["A) 90°", "B) 180°", "C) 360°", "D) 450°"],
    ["A) Gold", "B) Iron", "C) Diamond", "D) Granite"],
    ["A) Osmosis", "B) Photosynthesis", "C) Respiration", "D) Fermentation"],
    ["A) 60 seconds", "B) 1,200 seconds", "C) 2,400 seconds", "D) 3,600 seconds"],
    ["A) Highly Acidic", "B) Highly Alkaline (Basic)", "C) Neutral", "D) Radioactive"],
    ["A) Shark", "B) Whale", "C) Tuna", "D) Seahorse"],
    ["A) Red", "B) Yellow", "C) Green", "D) Violet"]
]

answers = ["B","C","D","C","C","B","D","C","B","D"]
Guesses = []

option_num = 0
score = 0

for question in questions:
    print(question)
    for option in options[option_num]:
        print(option)
    guess = input()
    Guesses.append(guess)
    if (guess == answers[option_num]):
        print("Correct")
        score += 1
    else:
        print(f"Wrong {answers[option_num]} is correct")
    option_num += 1

print(answers)
print(Guesses)
print(score)
