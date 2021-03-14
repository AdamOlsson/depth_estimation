import json, sys, getopt

def loadJson(path):
    with open(path) as jsfile:
        config = json.load(jsfile)
    return config


def parseArgs(argv):
    def printHelp():
        print("Help")
    try:
        opts, _ = getopt.getopt(argv, 'c:h:d', ['config=', 'help', 'default'])
    except getopt.GetoptError:
       sys.exit(2)
    config_path = ""
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            printHelp()
            sys.exit()
        elif opt in ('-d', '--default'):
            config_path = "config.json"
        elif opt in ("-c", "--config"):
            config_path = arg
    return config_path
