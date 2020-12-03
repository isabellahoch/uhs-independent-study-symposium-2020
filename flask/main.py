from flask import Flask, render_template, request, redirect, url_for, make_response, abort, Response
import os
from flask_compress import Compress
import datetime

app = Flask(__name__)
COMPRESS_MIMETYPES = ['text/html', 'text/css', 'application/json']
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500
Compress(app)

app.config['SECRET_KEY'] = os.urandom(24)

import gspread
gc = gspread.service_account(filename='service_account.json')
sh = gc.open("Independent Study Symposium Master Spreadsheet")
sheet = sh.sheet1

def get_info():
    info = {}
    info["categories"] = ["English", "History", "Math", "Science", "Languages", "Arts", "Human Development"]
    info["is_array"] = []
    info["is_dict"] = {}
    info["description"] = "get it from a different sheet perhaps?"
    info["is_names"] = []
    all_info = sheet.get_all_values()
    all_info.pop(0)
    for item in all_info:			
        this_item= {"timestamp":item[0], "email":item[1], "name":item[2],"graduation_year":item[3],"sponsor":item[4],"department":item[5],"title":item[6],"description":item[7],"link":item[8],"cover_photo":item[9],"profile_photo":item[10]}
        this_item["index"] = all_info.index(item)
        this_item["id"] = this_item["title"].lower().replace(" ","-")
        if "," in this_item["name"]:
            this_item["names"] = this_item["name"].split(", ")
        this_item["name_info"] = []
        print(this_item["title"])
        info["is_names"].append(this_item["title"].lower())
        # for leader in this_item["leader_array"]:
        #     leader_dict = {"name": leader,"link":"https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name="+leader.split(" ")[0]+"&const_search_last_name="+leader.split(" ")[1]}
        #     if "and " in leader:
        #         leader_dict["name"] = leader[4:]
        #     if this_item["leader_array"].index(leader) == len(this_item["leader_array"])-1 and len(this_item["leader_array"])!=1:
        #         leader_dict["is_not_last"] = False
        #     else:
        #         leader_dict["is_not_last"] = True
        #     if this_item["leader_array"].index(leader) != 0:
        #         leader_dict["is_not_first"] = True
        #     this_item["leader_info"].append(leader_dict)
        this_item["sponsor_array"] = [this_item["sponsor"]]
        this_item["sponsor_info"] = []
        for sponsor in this_item["sponsor_array"]:
            if " " in sponsor:
                sponsor_dict = {"name": sponsor,"link":"https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name="+sponsor.split(" ")[0]+"&const_search_last_name="+sponsor.split(" ")[1]}
            else:
                sponsor_dict = {"name": sponsor,"link":"https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name="+sponsor}
            if "and " in sponsor:
                sponsor_dict["name"] = sponsor[4:]
            if this_item["sponsor_array"].index(sponsor) == len(this_item["sponsor_array"])-1:
                sponsor_dict["is_not_last"] = False
            else:
                sponsor_dict["is_not_last"] = True
            if this_item["sponsor_array"].index(sponsor) != 0:
                sponsor_dict["is_not_first"] = True
            if len(this_item["sponsor_array"])==1:
                sponsor_dict["is_not_last"] = False
                sponsor_dict["is_not_first"] = False
            this_item["sponsor_info"].append(sponsor_dict)
        info["is_array"].append(this_item)
        info["is_dict"][this_item["title"]] = this_item
        # if len(item)>=11:
        #     if item[10] == "Yes":
        #         this_item["is_affinity_group"] = True
        if "?id=" in this_item["cover_photo"]:
            this_item["cover_photo"] = "https://drive.google.com/uc?export=view&id="+this_item["cover_photo"].split("?id=")[1]
        if "?id=" in this_item["profile_photo"]:
            this_item["profile_photo"] = "https://drive.google.com/uc?export=view&id="+this_item["profile_photo"].split("?id=")[1]
        if this_item["cover_photo"] == "":
            this_item["cover_photo"] = "https://via.placeholder.com/150?text="+this_item["title"]+" ("+this_item["name"]+")"
    return info 

@app.route('/')
def generate_independent_study_symposium():
    info = get_info()
    return render_template('old_base.html', info = info)


@app.route('/index')
def generate_independent_study_symposium2():
    info = get_info()
    return render_template('index.html', info = info)



app.jinja_env.cache = {}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)