import random

def target_num_input(input_string):
    if input_string.isdigit():
        return int(input_string)
    else:
        print("Please enter a number!")
        raise SystemExit(1)

def num_parse_input(input_string):
    if input_string.strip() in {"1", "2", "3", "4", "5", "6", "7", "8"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 8.")
        raise SystemExit(1)

def adv_parse_input(input_string):
    input_string = input_string.strip().upper() 
    if input_string in {"F", "I", "N"}:
        if input_string == "F":
            return True
        elif input_string == "I":
            return False
        elif input_string == "N":
            return None
        else:
            print("How did you get here, you little nerd!")
            raise SystemExit(1)
    else:
        print("Please enter one of the following letters: F, I or N")
        raise SystemExit(1)

def yn_parse_input(input_string):
    input_string = input_string.strip().upper() 
    if input_string in {"Y", "N"}:
        if input_string == "Y":
            return True
        elif input_string == "N":
            return False
        else:
            print("How did you get here, you little nerd!")
            raise SystemExit(1)
    else:
        print("Please enter one of the following letters: Y, N")
        raise SystemExit(1)

def special_result(roll):
    if roll == 11:
        return "Eye of Sauron"
    elif roll == 12:
        return "Gandalf rune"
    else:
        return roll

def degree_of_success(sixes, result, target):
    if result > target:
        if sixes == 1:
            return "A Great Success"
        elif sixes >= 2:
            return "An Extraordinary Success"
        else:
            return "A Success"
    else:
        return "A Failure"

def roll_dice(target_num, num_success_dice, advantage, weary, miserable):
    roll_results = {}
    adv_feat_roll_results = {}
    success_roll_results = []
    sixes = 0
    success_total = 0

    if advantage == None:
        feat_roll = random.randint(1,12)
        roll_results["Feat Dice"] = special_result(feat_roll)
    else:
        feat_roll_1 = random.randint(1,12)
        feat_roll_2 = random.randint(1,12)

        higher_result = feat_roll_1 if feat_roll_1 > feat_roll_2 else feat_roll_2
        lower_result = feat_roll_1 if feat_roll_1 < feat_roll_2 else feat_roll_2

        adv_feat_roll_results["Higher Feat Dice"] = special_result(higher_result)
        adv_feat_roll_results["Lower Feat Dice"] = special_result(lower_result)

        roll_results["Feat Dice"] = adv_feat_roll_results

    for _ in range(num_success_dice):
        roll = random.randint(1,6)
        if weary == True:
            if roll <= 3:
                roll = 0
        success_total += roll
        success_roll_results.append(roll)

    for roll in success_roll_results:
        if roll == 6:
            sixes += 1

    roll_results["Success Dice"] = success_roll_results

    if advantage == True:
        if higher_result == 12:
            result = target_num + 1
        else:
            result = success_total + higher_result
    elif advantage == False:
        if lower_result == 11:
            result = success_total + 0
        else:
            result = success_total + lower_result
    else:
        result = success_total + feat_roll
    
    if miserable == True:
        if advantage == True and higher_result == 11 or advantage == False and lower_result == 11:
            final_outcome = "A Failure"
        else:
            final_outcome = degree_of_success(sixes, result, target_num)
    else:
        final_outcome = degree_of_success(sixes, result, target_num)

    roll_results["Outcome"] = {"Degree of Success": final_outcome, "Number of sixes": sixes}
        
    return roll_results

target_num = target_num_input(input("What is the target number?"))
success_num_dice = num_parse_input(input("How many success dice do you want to roll? [1-8]"))
feat_advantage = adv_parse_input(input("Is your roll favored, ill-favored or is this a normal roll? [F/I/N]"))
weary_status = yn_parse_input(input("Are you weary? [Y/N]"))
miserable_status = yn_parse_input(input("Are you miserable? [Y/N]"))

roll_results = roll_dice(target_num, success_num_dice, feat_advantage, weary_status, miserable_status)

print(roll_results)