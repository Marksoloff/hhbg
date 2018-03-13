# First, I typed import random so I could use the random module.
import random
personalities = ("Rookie", "Washed up", "Retired", "Unhinged", "Slick", "Incompetent")
bear_types = ("Grizzly Bear", "Polar Bear", "Panda", "Black Bear", "Sun Bear", "Honey Badger")
criminal_roles = ("Enforcer", "Mastermind", "Getaway Driver", "Hacker", "Thief", "Face")
# user input to starts the process.
def stats():
    personality_stat = random.choice(personalities)
    bear_types_stat = random.choice(bear_types)
    criminal_roles_stat = random.choice(criminal_roles)
    print(f"""Badda-BOOM! Hey get a load of you, ya stinkin':
        
        {personality_stat}
        {bear_types_stat}
        {criminal_roles_stat}""") 
    input("Welcome to the gang, ya filthy animal! Let's figure out your bear name. Hit ENTER, okay?")
# TODO: Create a finish screen.
#       Create a screen with "roll" button to replace current enter prompt. 
def self_name():
    self_name_choice = input("Would you like to think up your own bear name? Y/N? \n")
    if self_name_choice.upper() == "Y":
        typed_name = input("Now we're cookin' with gas! Enter your bear name:\n")
        print("Nice ta meetcha, " + typed_name + "!")   
    else:
        print("Okee doke! Let's proceed.")         
# First & Last name strings to randomize
def name(assignment):   
    boy_name = ("Bugsy", "Artie", "Mooksie", "Petey", "Vinnie", "Lou", "Mungo", "Mack", "Tony", "Teddy", "Bobo", "Chucky", "Bobby", "Lucio", "Musky", "Sticks", "Clawsy", "Yogi")
    girl_name = ("Ursula", "Coco", "Wendy", "Velvet", "Betty", "Mama", "Louisa", "Belladonna", "Carmen", "Jaimie", "Veronica", "Squeaky", "Bang-Bang", "Cookies", "Delores")
    asex_name = ("Grumbles", "Pork-Bone", "Pittsburgh", "Brumbo", "Binky", "Stabs", "Punchy", "Husky", "Shortstack", "Pookie", "Bing Bing", "Clawsy", "Dead-eye", "Knuckles", "Mookie", "Sneaky", "Two-toes", "Shades", "Bully", "Meatsy", "Chuckles", "Bingo", "Pathos")    
    surname = ("Malone", "LeRoy", "Falcone", "O'Malley", "Pitsacotta", "Rourke", "Putanesca", "the Chopper", "MacKenzie", "the Knife", "Fujimora", "Tanaka", "the Vermin of Scarsdale")    

# Variable names assigned to randomly selected names 
    if assignment.upper() == "M":  
        first_name = random.choice(boy_name)
    elif assignment.upper() == "F":
        first_name = random.choice(girl_name)
    else:
        first_name = random.choice(asex_name)
    surname = random.choice(surname)
    return first_name + " " + surname

#added print("mazel tov, kid." to end of every function bc it stopped printing in its old position.)
def ungender():
    while True:
        print("\nAh, what's gender anyways but a social construct?")
        input("Hit ENTER again and I'll cook up a real crackerjack of a name for ya.")
        print("And your name is: "+ name("U")+"!")
        print("Mazel tov, kid.")
        return
    
def gender():
    while True:
        male_or_fem = input ("Is your bear male or female? M/F? \n")
        if male_or_fem.upper() == "M":
            print("Nice to meetcha, pal!")
            input("Hit ENTER again and I'll cook up a real crackerjack name for ya. \n")
            print("And your name is: "+ name("M")+"!")
            print("Mazel tov, kid.")
            return
        elif male_or_fem.upper() == "F":
            print("Pleased to meetcha miss. Charmed, I'm sure.")
            input("Hit ENTER again and I'll cook up a real crackerjack name for ya.\n")
            print("And your name is: "+ name("F")+"!") 
            print("Mazel tov, kid.")
            return
        else:
            print("\nWhat's that? Stop bein' a mook and type 'M' or 'F'!")
            gender()
            return            
#created gen_or_not function.
def gen_or_not():
    while True:
        gendered=input ("Ey, I been wonderin'... Does your bear have a gender?: Y/N?")
        print(gendered)           
        if gendered.upper() == "Y":
            gender()
            return
        if gendered.upper() == "N":
            ungender()
            return
        else:
            print("\nI don't understand you, kid. Just type 'Y' or 'N' already!")
            gen_or_not()
            return
def main():
# Nested If statements narrow user's name options 
    print("Welcome to da Honey Heist Bearacter Generator")
    input("Press ENTER to create a new character, capeesh?")
# Function for user to input their own name.
    stats()
    self_name()
    gen_or_not()
    

if __name__ == "__main__":
        main()