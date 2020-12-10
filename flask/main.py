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

from forms import SearchForm, LoginForm


from flask_login import LoginManager, current_user, login_user, login_required, logout_user
login = LoginManager(app)
login.login_view = 'login'
ACCESS_CODE = "gobigred"

from flask_sqlalchemy import SQLAlchemy

sql_db = SQLAlchemy()

sql_db.init_app(app)

class User(sql_db.Model):
    """An admin user capable of viewing reports.

    :param str email: UHS email address of user

    """
    __tablename__ = 'user'

    email = sql_db.Column(sql_db.String, primary_key=True)
    authenticated = sql_db.Column(sql_db.Boolean, default=False)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

# @app.route('/temporary-test')
# def temporary_test():
#     sql_db.create_all()
#     test_user = User(email="studentitteam@sfuhs.org")
#     sql_db.session.add(test_user)
#     sql_db.session.commit()

@login.user_loader
def load_user(user_id):
    # return User.query.get(int(id))
    return User.query.filter_by(email=user_id).first()

@app.route('/', methods=['GET', 'POST'])
def login():
    sql_db.create_all()
    alert = request.args.get('alert')
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    print("here")
    if form.validate_on_submit():
        next_url = request.args.get("next")
        if next_url:
            print("aha")
        else:
            print("whyyy")
            print(request.form.get("next"))
            if request.form.get("next"):
                next_url = request.form.get("next")
            print(request.path)
        print(next_url)
        if form.password.data != ACCESS_CODE:
            print(form.password.data)
            alert='Invalid access code. Please try again or contact UHS administration for help.'
            return redirect(url_for('login', alert=alert, next=next_url))
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            user = User(email=form.email.data)
            sql_db.session.add(user)
            sql_db.session.commit()
            login_user(user, remember=True)
        else:
            login_user(user, remember=True)
        if next_url and next_url.strip() != "" and next_url.strip() != "/":
            return redirect(next_url)
        else:
            return redirect(url_for('dashboard'))
        # return redirect(url_for('index'))
        return redirect(url_for('dashboard'))
    if alert:
        return render_template('login.html', form=form, info = get_truncated_info(), if_alert = True, alert = alert)
    next_url = request.args.get("next")
    return render_template('login.html', next=next_url, form=form, info = get_truncated_info())

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import DataRequired

def get_info():
    info = {}
    if current_user.is_authenticated:
        info["user"] = {"email":current_user.email}
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
        this_item = {"timestamp":item[0], "email":item[1], "name":item[2], "graduation_year":item[3], "sponsor":item[4], "department":item[5], "title":item[6], "description":item[7], "link":item[8], "cover_photo":item[9], "profile_photo":item[10], "zoom_link":item[11], "proj_type":item[12], "sharing_confirmation":item[13], "if_synchronous":item[14], "additional_comments":item[15], "random":item[16], "group_names":item[17], "random_2":item[18], "link_2":item[19], "if_slideshow":item[20], "id":item[21], "new_link":item[22], "david":item[23]}
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
            if len(this_item["short_description"]) > 2:
                try:
                    new_variable = this_item["short_description"][x-1]
                    if  new_variable == " ":
                        break
                    else:
                        this_item["short_description"] = this_item["short_description"][:x-1]
                except:
                    print(this_item["title"]+" description error")

               
        this_item["short_description"] = this_item["short_description"].strip()+"..."
        # if len(item)>=11:
        #     if item[10] == "Yes":
        #         this_item["is_affinity_group"] = True
        if "?id=" in this_item["cover_photo"]:
            this_item["cover_photo"] = "https://drive.google.com/uc?export=view&id="+this_item["cover_photo"].split("?id=")[1]
        if "?id=" in this_item["profile_photo"]:
            this_item["profile_photo"] = "https://drive.google.com/uc?export=view&id="+this_item["profile_photo"].split("?id=")[1]
        # if "presentation" in this_item["link"]:
        #     this_item["embed_link"] = '<iframe src="https://drive.google.com/embeddedfolderview?id='+this_item["link"].split("/folders/")[1].split("?")[0]+'/#grid" frameborder="0" width="1440" height="839" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>'
        if this_item["new_link"] != "":
            this_item["link"] = this_item["new_link"]
        if "folder" in this_item["link"]:
            this_item["link"] = "https://drive.google.com/embeddedfolderview?id="+this_item["link"].split("/folders/")[1].split("?")[0]+"#grid"
        if "/pub" in this_item["link"]:
            this_item["link"] = this_item["link"].split("/pub")[0]+"/embed?start=true&loop=true&delayms=3000"
        if this_item["link_2"] == "":
            this_item["link_2"] = None
        if this_item["david"] == "":
            this_item["david"] = None
        if "/view" in this_item["link"]:
            this_item["link"] = this_item["link"].replace("view","preview")
        if this_item["cover_photo"] == "":
            this_item["cover_photo"] = "https://via.placeholder.com/150?text="+this_item["title"]+" ("+this_item["name"]+")"
        info["is_array"].append(this_item)
        info["is_dict"][this_item["id"]] = this_item
        this_item["department_id"] = this_item["department"].lower().replace(" ","-")
        if this_item["department_id"] == "human-development":
            this_item["department_id"] = "hd"
        if this_item["department_id"] not in info["category_is_dict"]:
            info["category_is_dict"][this_item["department_id"]] = []
        info["category_is_dict"][this_item["department_id"]].append(this_item)
        if "user" in info and info["user"]["email"] == this_item["email"]:
            if "independent_studies" not in info["user"]:
                info["user"]["independent_studies"] = []
            info["user"]["independent_studies"].append(this_item)
    return info 

def get_truncated_info():
    info = {}
    if current_user.is_authenticated:
        info["user"] = {"email":current_user.email}
    info["form"] = SearchForm()
    info["categories"] = ["English", "History", "Math", "Science", "Languages", "Arts", "HD"]
    return info

def get_by_id(proj_id):
    info = get_info()
    return info["is_dict"][proj_id]

@app.route('/old')
@login_required
def generate_independent_study_symposium():
    info = get_info()
    return render_template('old_base.html', info = info)

@app.route('/dashboard')
@login_required
def dashboard():
    info = get_info()
    return render_template('dashboard.html', info = info)

@app.route('/projects/<proj_id>')
@login_required
def get_independent_study(proj_id):
    info = get_info()
    project = info["is_dict"][proj_id]
    return render_template('project.html', info = info, project = project)

@app.route('/categories/<cat_id>')
@login_required
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
@login_required
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


@app.route('/view-all')
@login_required
def index():
    info = get_info()
    return render_template('index.html', info = info)

@app.route('/slideshow')
@login_required
def slideshow():
    info = get_info()
    return render_template('carousel.html', info = info)

@app.route('/agenda')
@login_required
def agenda():
    info = get_info()
    return render_template('agenda.html', info = info)

@app.route('/stop')
@login_required
def sorry():
    info = get_info()
    return render_template('bruh.html', info = info)



app.jinja_env.cache = {}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)