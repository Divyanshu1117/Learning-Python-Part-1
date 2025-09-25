def game():
    return 664

score = game()
with open("095_hiscore.txt") as f:
    hiScoreStr = f.read()

if hiScoreStr == "":
    with open("095_hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScoreStr) < score:
    with open("095_hiscore.txt", "w") as f:
        f.write(str(score))