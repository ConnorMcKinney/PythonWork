import os

def write_score(seed, num_col, num_row, score):
    """(seed, score)"""
    if os.path.isdir("Scores"):
        file = open("Scores\\high scores.txt", "a")
        file.write("%i,%i,%i,%.2f\n" % (seed, num_col, num_row, score))
    else:
        os.mkdir("Scores")
        file = open("Scores\\high scores.txt", "a")
        file.write("%i,%i,%i,%.2f\n" % (seed, num_col, num_row, score))
    file.close()

def get_high_score(played_seed, played_col, played_row):
    try:
        file = open("Scores\\high scores.txt", "r")
    except:
        print("Scores file not found. First time playing?")
        return False
    best_score = {"best": 9999999}
    for line in file:
        seed, num_col, num_row, score = line.strip().split(",")
        if int(seed) == played_seed and int(num_col) == played_col and int(num_row) == played_row:
            if float(score) < best_score["best"]:
                best_score["best"] = float(score)
    file.close()
    return best_score["best"]
