SELF_PATH = "./resolve-exercises/"
PRE_FILE_NAME = "Ex"
FILE_EXT = ".py"
FIRST_LINE = "#! python3"
TEMPLATE_FILE_NAME = "ExTemplate.txt"

templateData = ''
with open(SELF_PATH + TEMPLATE_FILE_NAME, "r") as rFile:
    templateData = rFile.read()

for fileNum in range(5, 99):
    fileName = SELF_PATH + PRE_FILE_NAME + str(f"{fileNum:02d}") + FILE_EXT
    with open(fileName, 'a') as wFile:
        wFile.write(templateData)
