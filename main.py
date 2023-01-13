"""
Qasim Hamid
ICS4U
Qasim_Hamid_Independent_Study_Project.py
Program that uses tkinter inorder to allows user to create and save workouts, calculate there requried calories, and view there saved workout"""
import tkinter as tk
import json
import sys
from tkinter import font

HEIGHT = 900
WIDTH = 900
#defining variables height and width for screen size when program is ran

def delete():
    #function that delets widgets from a frame in tkinter
    for widget in frame.winfo_children():
        widget.destroy()


def workout():
    #function that is run after uses selects 'Create a workout' in main menu. Purpose is to allow user to choose which path they would like to go for creating there workout
    delete()

    button = tk.Button(frame, text="Calisthenics", font=('Courier', 15), command=calisthenics)
    button.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.15)
    #creates button that runs calisthenics function when activated

    button = tk.Button(frame, text="Weights", font=('Courier', 15), command=weights)
    button.place(relx=0.3, rely=0.55, relwidth=0.4, relheight=0.15)
    #creates button that runs weights function when activated


def calisthenics():

    delete()
    #clears widgets in frame

    global workout_value
    workout_value = 'Calisthenics'
    #assing workout_value 'Calisthenics', which is global as it will be used in other loops in order to extract information workouts.txt file

    button = tk.Button(frame, text="Gain Muscle", font=('Courier', 15), command=gain_muscle)
    button.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.15)
    #button that activates gain_muscle function when activated

    button = tk.Button(frame, text="Lose Fat", font=('Courier', 15), command=lose_fat)
    button.place(relx=0.3, rely=0.55, relwidth=0.4, relheight=0.15)
    #button that activates lose_fat function when activated


def weights():

    delete()
    #clears widgets in frame

    global workout_value
    workout_value = 'Weights'
    #assign Weights to global variable workout_value

    button = tk.Button(frame, text="Gain Muscle", font=('Courier', 15), command=gain_muscle)
    button.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.15)
    #button that activates gain_muscle function when activated

    button = tk.Button(frame, text="Lose Fat", font=('Courier', 15), command=lose_fat)
    button.place(relx=0.3, rely=0.55, relwidth=0.4, relheight=0.15)
    #button that activates lose_fat function when activated


def gain_muscle():

    delete()
    #clears widgets in frame

    button = tk.Button(frame, text="20 - 40 Minute", font=('Courier', 15), command=short_workout)
    button.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.15)
    #button that activates short_workout function when activated

    button = tk.Button(frame, text="40 - 60 Minute", font=('Courier', 15), command=long_workout)
    button.place(relx=0.3, rely=0.55, relwidth=0.4, relheight=0.15)
    #button that activates long_workout function when activated


def lose_fat():

    delete()
    #clears widgets in frame

    gain_loss = 'Fat loss'
    #assigns 'Fat loss' to gain_loss

    with open('workouts.txt', 'r')as workouts:
        exc = eval(workouts.read())
        #opens workouts.txt file as workouts in order for python to read

        for type, excercise in exc.items():
            data = (excercise[workout_value][gain_loss])
            #python checks for workout_value (calisthenics or weights) in txt file, then checks for gain_loss which is Fat loss
        with open('save_workout_1.txt', 'w')as save:
            json.dump(data, save, indent=2)
            #dumps workout information that was called data into save_workout_1.txt

        save_info()
        #displays info of workout


def short_workout():

    delete()
    #clear  s widgets in frame

    global length
    length = '20-40 minute'
    #length variable used later

    button = tk.Button(frame, text="Beginner", font=('Courier', 15), command=beginner)
    button.place(relx=0.3, rely=0.15, relwidth=0.4, relheight=0.15)
    #button that activates beginner() function when activated

    button = tk.Button(frame, text="Intermediate", font=('Courier', 15), command=intermediate)
    button.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.15)
    #button that activates intermediate() function when activated

    button = tk.Button(frame, text="Advanced", font=('Courier', 15), command=advanced)
    button.place(relx=0.3, rely=0.65, relwidth=0.4, relheight=0.15)
    #button that activates advanced() function when activated


def long_workout():

    delete()
    #clears widgets in frame

    global length
    length = '40-60 minute'
    #assigs 40-60 minute to length which will be used later

    button = tk.Button(frame, text="Beginner", font=('Courier', 15), command=beginner)
    button.place(relx=0.3, rely=0.15, relwidth=0.4, relheight=0.15)
    #button that activates beginner() function when activated

    button = tk.Button(frame, text="Intermediate", font=('Courier', 15), command=intermediate)
    button.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.15)
    #button that activates intermediate() function when activated

    button = tk.Button(frame, text="Advanced", font=('Courier', 15), command=advanced)
    button.place(relx=0.3, rely=0.65, relwidth=0.4, relheight=0.15)
    #button that activates advanced() function when activated


def dump():
    #function thats dumps information from workouts.txt into

    with open('workouts.txt', 'r')as workouts:
        exc = eval(workouts.read())
        #makes workouts.txt a python dictionary

        for type, excercise in exc.items():
            data = (excercise[workout_value][length][difficulty])
            #data finds workout with workout_value (calisthenics or weights), length (20-40 minute or 40-60 minute), and diffuculty (beginner, intermediate, advanced)
        with open('save_workout_1.txt', 'w')as save:
            json.dump(data, save, indent=2)
            #dumps information from data into save_workout_1.txt


def beginner():

    delete()
    #clears widgets in frame

    global difficulty
    difficulty = 'Beginner'
    #assigns beginner to difficulty

    dump()
    #runs dump function to add chosen workout to save_workout_1.txt

    save_info()
    #dipslays info of saved workout


def intermediate():

    delete()
    #clears widgets in frame

    global difficulty
    difficulty = 'Intermediate'
    #assigns intermediate to difficulty

    dump()
    #runs dump function to add chosen workout to save_workout_1.txt

    save_info()
    #dipslays info of saved workout


def advanced():

    delete()
    #clears widgets in frame

    global difficulty
    difficulty = 'Advanced'
    #assigns advanced to difficulty

    dump()
    #runs dump function to add chosen workout to save_workout_1.txt

    save_info()
    #dipslays info of saved workout


def save_info():

    save_workout = open('save_workout_1.txt', 'r')
    program = eval(save_workout.read())
    global save_work
    #makes save_workout a global vairable which is the saved textfile being eval()
    save_work = ''
    for type, work in program.items():
        save_work += "\n"+ type+ "\n"
        for excercise in work:
            save_work += excercise + ": " + str(work[excercise])+ "\n"
            #save_work is used to print the information from the dictionary neatly in label files as they are variables that carry information

    label = tk.Label(frame, text=save_work)
    label.place(relx=0.10, rely=0.05, relwidth=0.8, relheight=0.8)
    #label that prints save_work

    button = tk.Button(frame, text="Exit", command=start)
    button.place(relx=0.3, rely=0.9, relwidth=0.4, relheight=0.04)
    #button that exits activates start command to take user back to main interface


def start():
    #ran after user has gone through an option in menu

    delete()
    #clears widgets in frame

    button_workout = tk.Button(frame, text="Create a workout", font=('Courier', 15), command=workout)
    button_workout.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.1)
    #button that activates workout function once activated

    button_calorie = tk.Button(frame, text="Calorie Counter", font=('Courier', 15), command=age_wid)
    button_calorie.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.1)
    #button that activates age_wild function when activated

    button_view = tk.Button(frame, text="View Current Workout", font=('Courier', 15), command=save_info)
    button_view.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.1)
    #button that activates save_info function when activated

    button_exit = tk.Button(frame, text="Exit Program", font=('Courier', 15), command=exit)
    button_exit.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.1)
    #button that activates exit function when activated


def age_wid():

    delete()
    #clears widgets in frame

    global frame_age
    frame_age = tk.Frame(root, bd=2)
    frame_age.place(relx=0.125, rely=0.1, relwidth=0.75, relheight=0.1)
    #frame made to hold entry_age and label_age

    entry_age = tk.Entry(frame_age, font=('Courier', 15))
    entry_age.place(relwidth=0.65, relheight=1)
    #entry that is used in age(entry_age) function

    button_age = tk.Button(frame_age, text="Confirm Age", font=('Courier', 15), command=lambda:age(entry_age.get()))
    button_age.place(relx=0.6, relheight=1, relwidth=0.4)
    #button that activates age(entry_age) to check if the user has corrected a value that works

    global frame_text
    frame_text = tk.Frame(root, bd=2, bg='black')
    frame_text.place(relx=0.125, rely=0.25, relwidth=0.75, relheight=0.6)
    #frame that holds label_age

    global label_age
    label_age = tk.Label(frame_text, text = "Enter your age", font=('Courier', 15))
    label_age.place(relx=0, rely=0, relwidth=1, relheight=1)
    #label that prints instructions to the user


def age(entry_age):

    try:
        if int(entry_age) > 0:
            global age_enter
            age_enter = int(entry_age)
            #age_enter will be used in another function, checks if a interger above 0 is unputted
        elif int(entry_age) < 0:
            label_age['text'] = 'Enter a integer greater than 0, try again'
            #checks if user inputted integer that is less than 0
    except:
        label_age['text'] = 'Enter a integer greater than 0, try again'
        #runs when integer is not inputted

    try:
        if int(entry_age) > 0:
            frame_age.destroy()
            frame_age.pack_forget()
            frame_text.destroy()
            frame_text.pack_forget()
            #destroys frames for age and text
            button_continue = tk.Button(frame, text="Continue", command=weight_wid, font=('Courier', 15))
            button_continue.place(relx=0.3, rely=0.3, relheight=0.1, relwidth=0.4)
            #if statement that runs if int(entry_age) is a integer greater than 0, in order to store an accurate value and allow the user to move on to the next function.
    except:
        return
        #exits function where user can enter a new age


def weight_wid():

    delete()
    #clears widgets in frame

    global frame_weight
    frame_weight = tk.Frame(root, bd=2)
    frame_weight.place(relx=0.125, rely=0.1, relwidth=0.75, relheight=0.1)
    #creates frame to hold entry and button

    entry_weight = tk.Entry(frame_weight, font=('Courier', 15))
    entry_weight.place(relwidth=0.65, relheight=1)
    #entry that is checked in weight(entry_weight)

    button_weight = tk.Button(frame_weight, text="Confirm Weight", font=('Courier', 15), command=lambda:weight(entry_weight.get()))
    button_weight.place(relx=0.6, relheight=1, relwidth=0.4)
    #button that runs weight(entry_weight)

    global frame_text
    frame_text = tk.Frame(root, bd=2, bg='black')
    frame_text.place(relx=0.125, rely=0.25, relwidth=0.75, relheight=0.6)
    #frame used to display label

    global label_weight
    label_weight = tk.Label(frame_text, text="Enter your weight in KG", font=('Courier', 15))
    label_weight.place(relx=0, rely=0, relwidth=1, relheight=1)
    #label is used to print instructions to user


def weight(entry_weight):

    try:
        if int(entry_weight) > 0:
            global weight_enter
            weight_enter = int(entry_weight)
            #checks if entry_weight is an integer > 0, where it stores weight_enter as int(entry_weight)
        elif int(entry_weight) <= 0:
            label_weight['text'] = 'Enter a integer greater than 0, try again'
            #runs if user inputs integer that is less than equal to 0 is inputted
    except:
        label_weight['text'] = 'Enter a integer greater than 0, try again'
        #runs if user doesn't inpute integer

    try:
        if int(entry_weight) > 0:
            frame_weight.destroy()
            frame_weight.pack_forget()
            frame_text.destroy()
            frame_text.pack_forget()
            #destroys frames for weight and text
            button_continue = tk.Button(frame, text="Continue", command=height_wid, font=('Courier', 15))
            button_continue.place(relx=0.3, rely=0.3, relheight=0.1, relwidth=0.4)
            #activates height_wid
    except:
        return
        #returns user to wid_age()


def height_wid():

    delete()
    #clears widgets in frame

    global frame_height
    frame_height = tk.Frame(root, bd=2)
    frame_height.place(relx=0.125, rely=0.1, relwidth=0.75, relheight=0.1)
    #frame that stores entry and button

    entry_height = tk.Entry(frame_height, font=('Courier', 15))
    entry_height.place(relwidth=0.65, relheight=1)
    #entry where number is inputted for height(entry_height)

    button_height = tk.Button(frame_height, text="Confirm Height", font=('Courier', 15), command=lambda:height(entry_height.get()))
    button_height.place(relx=0.6, relheight=1, relwidth=0.4)
    #button that runs height(entry_height)

    global frame_text
    frame_text = tk.Frame(root, bd=2, bg='black')
    frame_text.place(relx=0.125, rely=0.25, relwidth=0.75, relheight=0.6)
    #frame that stores label

    global label_height
    label_height = tk.Label(frame_text, text="Enter your height in cm", font=('Courier', 15))
    label_height.place(relx=0, rely=0, relwidth=1, relheight=1)
    #label that displays instructions for user


def height(entry_height):

    try:
        if int(entry_height) > 0:
            global height_enter
            height_enter = int(entry_height)
            #checks if int(entry_height) is greater than 0
        elif int(entry_height) < 0:
            label_height['text'] = 'Enter a integer greater than 0, try again'
            #checks if entry_height is less than 0
    except:
        label_height['text'] = 'Enter a integer greater than 0, try again'
        #runs if integer is not enterred

    try:
        if int(entry_height) > 0:
            frame_height.destroy()
            frame_height.pack_forget()
            frame_text.destroy()
            frame_text.pack_forget()
            #destroys frames height and text
            button_continue = tk.Button(frame, text="Continue", command=gender_wid, font=('Courier', 15))
            button_continue.place(relx=0.3, rely=0.3, relheight=0.1, relwidth=0.4)
            #button that runs gender_wid
    except:
        return
        #runs height_wid()


def gender_wid():

    delete()
    #clears widgets in frame

    global frame_gender
    frame_gender = tk.Frame(root, bd=2)
    frame_gender.place(relx=0.125, rely=0.1, relwidth=0.75, relheight=0.1)
    #frame that stores entry and button

    entry_gender = tk.Entry(frame_gender, font=('Courier', 15))
    entry_gender.place(relwidth=0.65, relheight=1)
    #entry that is checked in gender(entry_gender)

    button_gender = tk.Button(frame_gender, text="Confirm", font=('Courier', 15), command=lambda:gender(entry_gender.get()))
    button_gender.place(relx=0.6, relheight=1, relwidth=0.4)
    #button that runs gender(entry_gender)

    global frame_text
    frame_text = tk.Frame(root, bd=2, bg='black')
    frame_text.place(relx=0.125, rely=0.25, relwidth=0.75, relheight=0.6)
    #frame that stores label

    global label_gender
    label_gender = tk.Label(frame_text, text="Enter your sex, male('male') or female('female')", font=('Courier', 15))
    label_gender.place(relx=0, rely=0, relwidth=1, relheight=1)
    #label that prints instructions for user


def gender(entry_gender):

    try:
        if entry_gender == 'male' or entry_gender == 'Male':
            global gender_enter
            gender_enter = entry_gender
            #checks if user inputs male, where it adds that value to gender_enter
        elif entry_gender == 'female' or entry_gender == 'Female':
            gender_enter = entry_gender
            #checks if user inputs female, where it adds that value to gender_enter
        else:
            label_gender['text'] = "'Male' if you're male, or 'Female' if you're female"
    except:
        label_gender['text'] = "'Male' if you're male, or 'Female' if you're female"
        #runs if wrong value is inputted

    try:
        if entry_gender == 'male' or entry_gender == 'Male' or entry_gender == 'Female' or entry_gender == 'female':
            frame_gender.destroy()
            frame_gender.pack_forget()
            frame_text.destroy()
            frame_text.pack_forget()
            #destroys frames gender and text
            button_continue = tk.Button(frame, text="Continue", command=intensity_wid, font=('Courier', 15))
            button_continue.place(relx=0.3, rely=0.3, relheight=0.1, relwidth=0.4)
            #button that runs intensity_wid
    except:
        return
        #runs gender_wid


def intensity_wid():

    delete()
    #clears widgets in frame

    global intensity_choice
    intensity_choice = """1)Light: excercise 1-3 times/week
2)Moderate: excercise 4-5 times/week
3)Daily excercise or intense excercise 3-4 times/week
4)Very Active: intense excercise 6-7 times a week
5)Extra Active: intense excercise daily, or physical job"""
#variable used for text in label_intensity

    global frame_intensity
    frame_intensity = tk.Frame(root, bd=2)
    frame_intensity.place(relx=0.125, rely=0.1, relwidth=0.75, relheight=0.1)
    #frame that stores entry and button

    entry_intensity = tk.Entry(frame_intensity, font=('Courier', 15))
    entry_intensity.place(relwidth=0.65, relheight=1)
    #entry that gets checked in intensity (entry_intensity)

    button_intensity = tk.Button(frame_intensity, text="Confirm intensity", font=('Courier', 15), command=lambda: intensity(entry_intensity.get()))
    button_intensity.place(relx=0.6, relheight=1, relwidth=0.4)
    #button that runs intensity(entry_intensity)

    global frame_text
    frame_text = tk.Frame(root, bd=2, bg='black')
    frame_text.place(relx=0.125, rely=0.25, relwidth=0.75, relheight=0.6)
    #frame that stores label

    global label_intensity
    label_intensity = tk.Label(frame_text, text=intensity_choice, font=('Courier', 15))
    label_intensity.place(relx=0, rely=0, relwidth=1, relheight=1)
    #label that prints instructions to the user


def intensity(entry_intensity):

    try:
        if int(entry_intensity) == 1:
            global intensity_enter
            intensity_enter = entry_intensity
            global bmr
            bmr = 1.35
            #checks if int(entry_intensity) = 1, where it assigns the bmr value that will be used later
        elif int(entry_intensity) == 2:
            intensity_enter = entry_intensity
            bmr = 1.5
            #checks if int(entry_intensity) = 2
        elif int(entry_intensity) == 3:
            intensity_enter = entry_intensity
            bmr = 1.65
            #checks if int(entry_intensity) = 3
        elif int(entry_intensity) == 4:
            intensity_enter = entry_intensity
            bmr = 1.8
            #checks if int(entry_intensity) = 4
        elif int(entry_intensity) == 5:
            intensity_enter = entry_intensity
            bmr = 1.95
            #checks if int(entry_intensity) = 5
    except:
        label_intensity['text'] = 'Enter one of the selections below \n', intensity_choice
        #runs if something that is not 1-5 is inputted

    try:
        if int(entry_intensity) == 1 or int(entry_intensity) == 2 or int(entry_intensity) == 3 or int(entry_intensity) == 4 or int(entry_intensity) == 5:
            frame_intensity.destroy()
            frame_intensity.pack_forget()
            frame_text.destroy()
            frame_text.pack_forget()
            #destroys frame intensity and text
            button_continue = tk.Button(frame, text="Continue", command=calorie_print, font=('Courier', 15))
            button_continue.place(relx=0.3, rely=0.3, relheight=0.1, relwidth=0.4)
            #button that runs calorie_print

    except:
        return
        #returns user to intensity_wid function


def calorie_print():

    delete()
    #clears widgets in frame

    if gender_enter == 'male' or 'Male':
        calorie_total = 10*weight_enter + 6.25*height_enter - 5*age_enter + 5
        #checks if gender is male, where this function for calorie_total is run
    elif gender_enter == 'female' or 'Female':
        calorie_total = 10*weight_enter + 6.25*height_enter - 5*age_enter + 161
        #checks if gender is female, where this function for calorie_total is run

    if int(intensity_enter) == 1 or int(intensity_enter) == 2 or int(intensity_enter) == 3 or int(intensity_enter) == 4 or int(intensity_enter) == 5:
        calorie_total *= bmr
        #multiplies calorie_total by bmr

    label_cal_1 = tk.Label(frame, font=('Courier', 15))
    label_cal_1.place(relx=0.25, rely=0.25, relheight=0.1, relwidth=0.5)
    label_cal_1['text'] = "Calories to maintain weight:", calorie_total
    #label that prints calories to maintain weight

    label_cal_2 = tk.Label(frame, font=('Courier', 15))
    label_cal_2.place(relx=0.25, rely=0.45, relheight=0.1, relwidth=0.5)
    label_cal_2['text'] = "Calories to lose weight:", int(calorie_total) - 500
    #label that prints calories to lose weight

    label_cal_3 = tk.Label(frame, font=('Courier', 15))
    label_cal_3.place(relx=0.25, rely=0.65, relheight=0.1, relwidth=0.5)
    label_cal_3['text'] = "Calories to gain weight:", int(calorie_total) + 500
    #label that prints calories to gain weight

    button = tk.Button(frame, text="Exit", command=start)
    button.place(relx=0.3, rely=0.9, relwidth=0.4, relheight=0.04)
    #button that runs start function


def exit():
    sys.exit()
    #function that exits program




















root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

button_workout = tk.Button(frame, text="Create a workout", font=('Courier', 15), command=workout)
button_workout.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.1)

button_calorie = tk.Button(frame, text="Calorie Counter", font=('Courier', 15), command=age_wid)
button_calorie.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.1)

button_view = tk.Button(frame, text="View Current Workout", font=('Courier', 15), command=save_info)
button_view.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.1)

button_exit = tk.Button(frame, text="Exit Program", font=('Courier', 15), command=exit)
button_exit.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.1)

root.mainloop()
