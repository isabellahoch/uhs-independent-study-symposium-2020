from flask import Flask, render_template, request, redirect, url_for, make_response, abort, Response
import os
from flask_compress import Compress
import datetime
from flask_bootstrap import Bootstrap

app = Flask(__name__)
COMPRESS_MIMETYPES = ['text/html', 'text/css', 'application/json']
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500
Compress(app)
Bootstrap(app)

app.config['SECRET_KEY'] = os.urandom(24)

import gspread
gc = gspread.service_account(filename='service_account.json')
sh = gc.open("Independent Study Symposium Master Spreadsheet")
sheet = sh.sheet1

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()],render_kw = {"class":"form-control mr-sm-2", "type":"search","placeholder":"Search"})
    submit = SubmitField('GO', render_kw = {"class":"btn btn-outline-uhs my-2 my-sm-0"})

def get_info():
    info = {}
    info["form"] = SearchForm()
    info["categories"] = ["English", "History", "Math", "Science", "Languages", "Arts", "HD"]
    info["is_array"] = []
    info["is_dict"] = {}
    info["description"] = "get it from a different sheet perhaps?"
    info["is_names"] = []
    info["category_is_dict"] = {}
    all_info = sheet.get_all_values()
    all_info.pop(0)
    all_info.pop(0)
    for item in all_info:			
        this_item = {"timestamp":item[0], "email":item[1], "name":item[2], "graduation_year":item[3], "sponsor":item[4], "department":item[5], "title":item[6], "description":item[7], "link":item[8], "cover_photo":item[9], "profile_photo":item[10], "zoom_link":item[11], "proj_type":item[12], "sharing_confirmation":item[13], "if_synchronous":item[14], "additional_comments":item[15], "random":item[16], "group_names":item[17], "random_2":item[18], "link_2":item[19], "if_slideshow":item[20], "id":item[21], "new_link":item[22]}
        this_item["index"] = all_info.index(item)
        if "," in this_item["name"]:
            this_item["names"] = this_item["name"].split(", ")
        this_item["name_info"] = []
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
        this_item["short_description"] = this_item["description"][:250]
        for x in range(250, 0, -1):
            if this_item["short_description"][x-1] == " ":
                break
            else:
                this_item["short_description"] = this_item["short_description"][:x-1]
        this_item["short_description"] = this_item["short_description"].strip()+"..."
        info["is_array"].append(this_item)
        info["is_dict"][this_item["id"]] = this_item
        this_item["department_id"] = this_item["department"].lower().replace(" ","-")
        if this_item["department_id"] == "human-development":
            this_item["department_id"] = "hd"
        if this_item["department_id"] not in info["category_is_dict"]:
            info["category_is_dict"][this_item["department_id"]] = []
        info["category_is_dict"][this_item["department_id"]].append(this_item)
        # if len(item)>=11:
        #     if item[10] == "Yes":
        #         this_item["is_affinity_group"] = True
        if "?id=" in this_item["cover_photo"]:
            this_item["cover_photo"] = "https://drive.google.com/uc?export=view&id="+this_item["cover_photo"].split("?id=")[1]
        if "?id=" in this_item["profile_photo"]:
            this_item["profile_photo"] = "https://drive.google.com/uc?export=view&id="+this_item["profile_photo"].split("?id=")[1]
        if "presentation" in this_item["link"]:
            this_item["embed_link"] = '<iframe src="https://docs.google.com/presentation/d/e/'+this_item["link"].split("/presentation/d/")[1].split("/")[0]+'/embed?start=false&loop=true&delayms=5000" frameborder="0" width="1440" height="839" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>'
        if this_item["link_2"] == "":
            this_item["link_2"] = None
        if "/view" in this_item["link"]:
            this_item["link"] = this_item["link"].replace("view","preview")
        if this_item["new_link"] != "":
            this_item["link"] = this_item["new_link"]
        if this_item["cover_photo"] == "":
            this_item["cover_photo"] = "https://via.placeholder.com/150?text="+this_item["title"]+" ("+this_item["name"]+")"
    return info 

def get_by_id(proj_id):
    info = get_info()
    return info["is_dict"][proj_id]

@app.route('/old')
def generate_independent_study_symposium():
    info = get_info()
    return render_template('old_base.html', info = info)

@app.route('/projects/<proj_id>')
def get_independent_study(proj_id):
    info = get_info()
    project = info["is_dict"][proj_id]
    return render_template('project.html', info = info, project = project)

@app.route('/categories/<cat_id>')
def get_independent_studies_by_category(cat_id):
    info = get_info()
    if cat_id in info["category_is_dict"]:
        category = info["category_is_dict"][cat_id]
    else:
        category = []
    info["is_dict"] = category
    info["is_array"] = category
    return render_template('index.html', info = info, category_id = cat_id, category = cat_id.replace("-"," ").title())

@app.route('/search',methods=['GET','POST'])
def get_independent_studies_by_search():
    if request.method=="POST":
        print("post.")
    info = get_info()
    query = info["form"].search.data
    query = request.args.get('search')
    if query is None:
        query = " "
    matches = []
    for item in info["is_array"]:
        if query.lower() in item["title"].lower() or query in item["name"].lower():
            matches.append(item)
    info["is_dict"] = matches
    info["is_array"] = matches
    return render_template('index.html', info = info, category_id = "search", category = 'Search Results for "'+query+'"')


@app.route('/')
def index():
    info = get_info()
    return render_template('index.html', info = info)

@app.route('/slideshow')
def slideshow():
    info = get_info()
    return render_template('carousel.html', info = info)

@app.route('/stop')
def sorry():
    info = get_info()
    return render_template('bruh.html', info = info)



app.jinja_env.cache = {}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)