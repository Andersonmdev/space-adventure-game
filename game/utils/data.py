import os


def save(data):
    path = os.getcwd() + "/score.txt"
    try:
        f = open(path, "a+")
        f.write(data)
        f.close()
    except:
        return False
    return True


def load():
    path = os.getcwd() + "/score.txt"
    line = ""
    try:
        f = open(path, "r")
        line = f.readline()
        f.close()
    except:
        return False, []
    return True, line
