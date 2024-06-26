import datetime

possible_moods = ["angry", "sad", "apathetic", "relaxed", "happy"]
moods_ints = []



def assess_mood():
    entered_already = False
    current_mood_int = 0
    past_seven_moods_list = []
    date_today = str(datetime.date.today())
    file =  "data/mood_diary.txt"
    f = open(file,"r")
    for line in f:
        if date_today in line:
            print("Sorry, you have already entered your mood today.")
            entered_already = True
            break
    f.close()

    is_current_mood_possible = False
    while is_current_mood_possible is False and entered_already is False:
        current_mood = str(input("What is your current mood?"))
        if current_mood in possible_moods:
            current_mood_int = (str(possible_moods.index(current_mood)-2))
            is_current_mood_possible = True
    if entered_already is False:
        f=open(file,"a")
        f.write(date_today + " --> " + str(possible_moods.index(current_mood)-2) + "\n")
        f.close()
    
    entered_already = False
    if entered_already is False:
        sum_of_mood_int = 0
        f = open (file,"r")
        list_of_moods = f.readlines()
        print(list_of_moods)
        if len (list_of_moods) < 7:
            print("")
            return
        else:
            past_seven_moods = list_of_moods[-1: -8: -1]
            for line in past_seven_moods:
                individual_mood = line.split("> ")[-1]
                past_seven_moods_list.append(individual_mood)
                sum_of_mood_int = int(individual_mood) + sum_of_mood_int

        sad_counter = 0
        happy_counter = 0
        apathetic_counter = 0
        
        
        for i in past_seven_moods_list:
            if i == "-1\n":
                sad_counter = sad_counter + 1
            if i == "2\n":
                happy_counter = happy_counter + 1
            if i == "0\n":
                apathetic_counter = apathetic_counter + 1
        
        if sad_counter >= 4:
            print("Your diagnosis: depressive!")
        elif happy_counter >= 5:
            print("Your diagnosis: manic!")
        elif apathetic_counter >= 6:
            print("Your diagnosis: schizoid!")          
        else:
            avg_mood_ints = round((sum_of_mood_int)/7)
            print(avg_mood_ints)
            if avg_mood_ints == -2:
                print ("Your diagnosis: angry!")
            elif avg_mood_ints == -1:
                print ("Your diagnosis: sad!")
            elif avg_mood_ints == 0:
                print ("Your diagnosis: apathetic!")
            elif avg_mood_ints == 1:
                print ("Your diagnosis: relaxed!")
            elif avg_mood_ints == 2:
                print ("Your diagnosis: happy!")