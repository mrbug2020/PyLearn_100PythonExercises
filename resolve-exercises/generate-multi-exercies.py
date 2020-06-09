SELF_PATH = "./resolve-exercises/"
PRE_FILE_NAME = "Ex"
FILE_EXT = ".py"
FIRST_LINE = "#! python3"

for fileNum in range(1, 99):
    fileName = SELF_PATH + PRE_FILE_NAME + str(f"{fileNum:02d}") + FILE_EXT
    with open(fileName, 'a') as wFile:
        wFile.write(FIRST_LINE)
