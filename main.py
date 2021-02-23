import random
from time import perf_counter

keys = ["C", "G", "D", "A", "E", "B", "F#/Gb", "Db", "Ab", "Eb", "Bb", "F"]
step = [1, 2, 3, 4, 5, 6, 7]
cKey = ["Cmaj7", "Dm7", "Em7", "Fmaj7", "G7", "Am7", "Bm7b5"]
gKey = ["Gmaj7", "Am7", "Bm7", "Cmaj7", "D7", "Em7", "F#m7b5"]
dKey = ["Dmaj7", "Em7", "F#m7", "Gmaj7", "A7", "Bm7", "C#m7b5"]
aKey = ["Amaj7", "Bm7", "C#m7", "Dmaj7", "E7", "F#m7", "G#m7b5"]
eKey = ["Emaj7", "F#m7", "G#m7", "Amaj7", "B7", "C#m7", "D#m7b5"]
bKey = ["Bmaj7", "C#m7", "D#m7", "Emaj7", "F#7", "G#m7", "A#m7b5"]
fisKey = ["F#maj7", "G#m7", "A#m7", "Bmaj7", "C#7", "D#m7", "E#m7b5"]
dbKey = ["Dbmaj7", "Ebm7", "Fm7", "Gbmaj7", "Ab7", "Bbm7", "Cm7b5"]
abKey = ["Abmaj7", "Bbm7", "Cm7", "Dbmaj7", "Eb7", "Fm7", "Gm7b5"]
ebKey = ["Ebmaj7", "Fm7", "Gm7", "Abmaj7", "Bb7", "Cm7", "Dm7b5"]
bbKey = ["Bbmaj7", "Cm7", "Dm7", "Ebmaj7", "F7", "Gm7", "Am7b5"]
fKey = ["Fmaj7", "Gm7", "Am7", "Bbmaj7", "C7", "Dm7", "Em7b5"]


def chords():
    count = 0
    while True:
        chord = random.choice(step)

        highscore = 0
        chosenKey = random.choice(keys)
        print(chosenKey, chord)
        answer = input("Which Chord is it? ")
        if answer == cKey[chord - 1]:
            print("Right!")
            count += 1
        elif answer == gKey[chord - 1]:
            print("Right!")
            count += 1
        elif answer == dKey[chord - 1]:
            print("Right!")
            count += 1
        elif answer == aKey[chord - 1]:
            print("Right!")
            count += 1
        elif answer == eKey[chord - 1]:
            print("Right!")
            count += 1
        elif answer == bKey[chord - 1]:
            print("Right!")
            count += 1
        elif answer == fisKey[chord - 1]:
            print("Right!")
            count += 1
        elif answer == dbKey[chord - 1]:
            print("Right!")
            count += 1
        elif answer == abKey[chord - 1]:
            print("Right!")
            count += 1
        elif answer == ebKey[chord - 1]:
            print("Right!")
            count += 1
        elif answer == bbKey[chord - 1]:
            print("Right!")
            count += 1
        elif answer == fKey[chord - 1]:
            print("Right!")
            count += 1
        elif answer == 0:
            print("Wrong!")
        elif answer == "Menu":
            menu(input("What you wanna do? (Chords/ Signs/ Time/ Test) "))
            break
        elif answer == "Quit":
            break
        else:
            print("Wrong!")
            if count > highscore:
                highscore = count
            print("Your high-score: " + str(highscore))
            print("Your score: " + str(count))
            count = 0


def time():
    right = 0
    wrong = 0
    rounds = int(input("How many rounds? "))
    go = perf_counter()
    while rounds != 0:

        chord = random.choice(step)

        print(random.choice(keys), chord)
        answer = input("Which Chord is it? ")

        if answer == cKey[chord - 1]:
            right += 1
            rounds -= 1
        elif answer == gKey[chord - 1]:
            right += 1
            rounds -= 1
        elif answer == dKey[chord - 1]:
            right += 1
            rounds -= 1
        elif answer == aKey[chord - 1]:
            right += 1
            rounds -= 1
        elif answer == eKey[chord - 1]:
            right += 1
            rounds -= 1
        elif answer == bKey[chord - 1]:
            right += 1
            rounds -= 1
        elif answer == fisKey[chord - 1]:
            right += 1
            rounds -= 1
        elif answer == dbKey[chord - 1]:
            right += 1
            rounds -= 1
        elif answer == abKey[chord - 1]:
            right += 1
            rounds -= 1
        elif answer == ebKey[chord - 1]:
            right += 1
            rounds -= 1
        elif answer == bbKey[chord - 1]:
            right += 1
            rounds -= 1
        elif answer == fKey[chord - 1]:
            right += 1
            rounds -= 1
        elif answer is None:
            wrong += 1
            rounds -= 1
        elif answer == "menu":
            menu(input("What you wanna do? (Chords/ Signs/ Time/ Test) "))
            rounds = 0
        elif answer == "quit":
            break
        else:
            wrong += 1
            rounds -= 1
    notGo = perf_counter()
    print("Your time is: ", notGo - go)
    print("Right: " + str(right) + ", Wrong: " + str(wrong))
    menu(input("What you wanna do? (Chords/ Signs/ Time/ Test) "))


def signs():
    while True:
        signsnumber = [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
        i = random.randint(0, 11)
        answer2 = input("How many signs does " + keys[i] + " have?: ")
        if answer2 == str(signsnumber[i]):
            print("Right!")
        elif answer2 == "Menu":
            menu(input("What you wanna do? (Chords/ Signs/ Time/ Test) "))
            break
        elif answer2 == "Quit":
            break
        else:
            print("Wrong!")


def test():
    roundsTest = 0
    rightTest = 0
    wrongTest = 0

    input("This is a test. It will start when you type anything: ")
    t = perf_counter()

    while perf_counter() - t < 30:

        chord = random.choice(step)

        print(random.choice(keys), chord)
        testAnswer = input("Answer: ")
        if testAnswer == cKey[chord - 1]:
            rightTest += 1
            roundsTest += 1
        elif testAnswer == gKey[chord - 1]:
            rightTest += 1
            roundsTest += 1
        elif testAnswer == dKey[chord - 1]:
            rightTest += 1
            roundsTest += 1
        elif testAnswer == aKey[chord - 1]:
            rightTest += 1
            roundsTest += 1
        elif testAnswer == eKey[chord - 1]:
            rightTest += 1
            roundsTest += 1
        elif testAnswer == bKey[chord - 1]:
            rightTest += 1
            roundsTest += 1
        elif testAnswer == fisKey[chord - 1]:
            rightTest += 1
            roundsTest += 1
        elif testAnswer == dbKey[chord - 1]:
            rightTest += 1
            roundsTest += 1
        elif testAnswer == abKey[chord - 1]:
            rightTest += 1
            roundsTest += 1
        elif testAnswer == ebKey[chord - 1]:
            rightTest += 1
            roundsTest += 1
        elif testAnswer == bbKey[chord - 1]:
            rightTest += 1
            roundsTest += 1
        elif testAnswer == fKey[chord - 1]:
            rightTest += 1
            roundsTest += 1
        elif testAnswer is None:
            wrongTest += 1
            roundsTest += 1
        elif testAnswer == "Menu":
            menu(input("What you wanna do? (Chords/ Signs/ Time/ Test) "))
        elif testAnswer == "Quit":
            break
        else:
            wrongTest += 1
            roundsTest += 1
    print("The Test is over, you had " + str(rightTest) + "/" + str(roundsTest) + " right!")
    menu(input("What you wanna do? (Chords/ Signs/ Time/ Test) "))


def menu(start):
    if start == "Chords":
        chords()
    elif start == "Signs":
        signs()
    elif start == "Time":
        time()
    elif start == "Test":
        test()
    else:
        print("Wrong command")


menu(input("What you wanna do? (Chords/ Signs/ Time/ Test) "))
