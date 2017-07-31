import json
import os
class Config:
    def __init__(self):
        with open('settings.json') as data_file:
            settings = json.load(data_file)

        self.hostname = settings["hostname"]
        if os.path.exists('./' + settings["csv"]) and settings["csv"] != "":
            self.csv = settings["csv"]

        else:
            print("ERROR Cannot find "+str(settings["csv"])+", please provide the correct file name in the settings.json")
            exit()

        if isinstance(settings["position"]["oldUrlPos"], int) and isinstance(settings["position"]["newUrlPos"], int):
            self.oldUrlPos = settings["position"]["oldUrlPos"]
            self.newUrlPos = settings["position"]["newUrlPos"]
        else:
            print("ERROR Url positions are not numbers or not set")
            exit()

        self.ignoreFirstLine = settings["ignorefirstLine"] in ['true', True, 1, '1', 'True', 'yes', 'Yes']

    def __str__(self):
        return "Hostname set: "+ self.hostname +"\n CSV file set: "+self.csv+ "\n Is the first line of the CSV ignored? "+ str(self.ignoreFirstLine) + "\n Url Positions set: Old Url Pos "+ str(self.oldUrlPos) + ". New Url Pos "+ str(self.newUrlPos)
    # def replaceHost(self, newhostname):
    #     with open('settings.json') as data_file:
    #         settings = json.load(data_file)


