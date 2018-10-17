

import constants
import utilities
import matplotlib.pyplot as plt
import csv

def print_collection_bullyalert():
    filepath = constants.BULLYALERT_DATA_PATH+"/instagram_monitoring_users.json"
    data = utilities.read_json_data(filepath)
    num_private = 0
    num_public = 0
    medias = []
    followed_bys = []
    followings = []
    print("code running...")
    for d in data:
        username = d["username"]
        try:
            status_code, profile_json = utilities.get_instagram_profile_webpage_json(username)
            if profile_json["is_private"] == True:
                num_private +=1
                #medias.append(float(profile_json["edge_owner_to_timeline_media"]["count"]))
                #followed_bys.append(float(profile_json["edge_followed_by"]["count"]))
                #followings.append(float(profile_json["edge_follow"]["count"]))
            else:
                num_public +=1
                medias.append(float(profile_json["edge_owner_to_timeline_media"]["count"]))
                followed_bys.append(float(profile_json["edge_followed_by"]["count"]))
                followings.append(float(profile_json["edge_follow"]["count"]))  
        except Exception as e:
            continue
    plt.boxplot([x for x in [followings]], 0, 'rs', 1)
    plt.xticks([y+1 for y in range(len([followings]))], ['followings'])
    plt.show()
    
    plt.boxplot([x for x in [followed_bys]], 0, 'rs', 1)
    plt.xticks([y+1 for y in range(len([followed_bys]))], ['followed_bys'])
    plt.show()
    
    plt.boxplot([x for x in [medias]], 0, 'rs', 1)
    plt.xticks([y+1 for y in range(len([medias]))], ['medias'])
    plt.show()
        
        
def print_collection_instagram_labeled():
    filenames = ["sessions_10plus_to_40_metadata.csv","sessions_0plus_to_10_metadata.csv","sessions_40plus_metadata.csv"]
    usernames = set()
    num_private = 0
    num_public = 0
    for filename in filenames:
        with open(constants.LABELED_DATA_PATH_INSTAGRAM+"//"+filename, encoding="'latin-1'") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["question2"] == "bullying" and float(row["question2:confidence"])> 0.9:
                    username = row["owner_id"].strip()
                    index1 = username.index(">")+1
                    index2 = username.index("</font>")
                    username = username[index1:index2].strip()
                    usernames.add(username)
    print(len(usernames))
    for username in list(usernames):
        try:
            status_code, profile_json = utilities.get_instagram_profile_webpage_json(username)
            if profile_json["is_private"] == True:
                num_private +=1
            else:
                num_public +=1  
        except Exception as e:
            continue
    print("private: "+str(num_private))
    print("public: "+str(num_public))
        

print_collection_bullyalert()

print("done")