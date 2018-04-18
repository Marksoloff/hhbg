from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    return render(request, 'index.html')
# The above code directs user to templates/index.html as the default HOME page!

def roll(request):
    return render(request, 'roll.html')

def stats(request):
    return render(request, 'stats.html')

def name(request):
    return render(request, 'name.html')

def stats():
    personality_stat = random.choice(personalities)
    bear_types_stat = random.choice(bear_types)
    criminal_roles_stat = random.choice(criminal_roles)
    print(f"""Badda-BOOM! Hey get a load of you, ya stinkin':

        {personality_stat}
        {bear_types_stat}
        {criminal_roles_stat}""")
    input(prompts["postStat"])

# Function for user to input their own name.
def self_name():
    self_name_choice = input(prompts["diyNameQuestion"] + "\n")
    if self_name_choice.upper() == "Y":
        typed_name = input(prompts["writeName"]+"\n")
        print("\n" + responses["meetchaTyped"] + typed_name + ". \n" + responses["welcomeGang"])
    else:
        print(prompts["proceed"])
        gen_or_not()
 #If user answers N to self_name_choice, call gen_or_not function.

# First & Last name strings to randomize
def name(assignment):
    global boy_name
    global girl_name
    global asex_name
    global surname
# Variable names assigned to randomly selected names
    if assignment.upper() == "M":
        first_name = random.choice(boy_name)
    elif assignment.upper() == "F":
        first_name = random.choice(girl_name)
    else:
        first_name = random.choice(asex_name)
    surname = random.choice(surname)
    return first_name + " " + surname

def ungender():
    while True:
        print("\n" + responses["genRetort"])
        input(prompts["preparingName"] + "\n")
        print("\n" + responses["yourNameIs"] + name("U") + "! \n" + responses["welcomeGang"])
        return

def gender():
    while True:
        male_or_fem = input ("Is your bear male or female? M/F? \n")
        if male_or_fem.upper() == "M":
            print("Nice to meetcha, pal!")
            input(prompts["preparingName"] + "\n")
            print("\n" + responses["yourNameIs"] + name("M") + "! \n" + responses["welcomeGang"])
            return
        elif male_or_fem.upper() == "F":
            print(responses["meetFem"])
            input(prompts["preparingName"] + "\n")
            print("\n" + responses["yourNameIs"] + name("F") + "! \n" + responses["welcomeGang"])
            return
        else:
            print(prompts["wrongGenderAnswer"] + "\n")
            gender()
            return
#created gen_or_not function for users who don't want to ID as male or female.
def gen_or_not():
    while True:
        gendered=input(prompts["isThereGender"])
        print(gendered)
        if gendered.upper() == "Y":
            gender()
            return
        if gendered.upper() == "N":
            ungender()
            return
        else:
            print("\n" + prompts["yOrN"])
            gen_or_not()
            return
def main():
    print(prompts["welcome"])
    input(prompts["rollPrompt"])
    stats()
    self_name()
#added print("mazel tov, kid.") to main() to reduce redundancy.
    print("\n" + responses["congrats"])

if __name__ == "__main__":
        main()


#    return HttpResponse(
#        '<a href="{% url roll %}">HTTP RESPONSE Click Roll Link</a>')


#def firstLink(request):
#    return render(request, 'firstLink.html')



    #return HttpResponse(
    #    "<a href='{% url firstLink %}'>HTTP RESPONSE Navigate to First Link Page</a>"
    #    "<h1>Roll</h1>")
