import constants
import utilities
import sys

class Guardian:
    def __init__(self):
        self.guardian_list = utilities.read_json_data(constants.BULLYALERT_DATA_PATH+"guardians.json")
    
    def draw_pie_chart(self, key):
        dictionary = dict()
        for g in self.guardian_list:
            dictionary[g[key]] = dictionary.get(g[key],0)+1
        utilities.draw_pie_chart([(key,dictionary[key]) for key in dictionary.keys()])       
        
g = Guardian()
g.draw_pie_chart(sys.argv[1])