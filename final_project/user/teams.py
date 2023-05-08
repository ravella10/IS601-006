from flask import Blueprint, flash, render_template, request, redirect, url_for, session, current_app
from flask_login import login_user, login_required, logout_user, current_user
from sql.db import DB
from roles.forms import RoleForm
from werkzeug.datastructures import MultiDict
from roles.permissions import admin_permission
import json
import http.client
import sql.config as config
teams = Blueprint('teams', __name__, url_prefix='/teams',template_folder='templates')



@teams.route("/test", methods=["GET","POST"])
def test():
    return render_template('test.html')

@teams.route("/view", methods=["GET","POST"])
def view():
    rows = []
    team_list = []
    league_list = []
    filtr = ''
    email = request.args.get("email",None)
    print(email)
    if email:
        filtr = f"AND U.email like '%{email}%'"
    try:
        result_1 = DB.selectAll(f"SELECT U.id as user_id ,U.username, U.email, T.id as team_id, T.name FROM IS601_Users U JOIN IS601_UserTeams UT on U.id = UT.user_id JOIN IS601_Teams T on T.id = UT.team_id WHERE 1=1 {filtr} LIMIT 100")
        if result_1.status and result_1.rows:
            team_list = result_1.rows
        result_2 = DB.selectAll(f"SELECT U.id as user_id ,U.username, U.email, L.id as league_id, L.name FROM IS601_Users U JOIN IS601_UserLeagues UL on U.id = UL.user_id JOIN IS601_Leagues L on L.id = UL.league_id WHERE 1=1 {filtr} LIMIT 100")
        if result_2.status and result_2.rows:
            league_list = result_2.rows
    except Exception as e:
        print(e)
        flash("Error getting user data", "danger")
    return render_template("team_list.html", team_list=team_list, league_list=league_list)

@teams.route("/delete", methods=["GET","POST"])
def delete():
    id = request.args.get("id", None)
    user_id = request.args.get("user_id", None)
    type_of = request.args.get("type",None)
    email = request.args.get("email",'')
    
    apply_where = '' if type_of=='league' else type_of
    try:
        if type_of == 'league':
            result = DB.selectAll("""
                Select * FROM IS601_UserLeagues WHERE user_id = %s and league_id = %s
                """, user_id, id)
            print(result.rows)
            if not result.rows:
                flash("Invalid ID! Unable to Delete League from watchlist","danger")
                return redirect(url_for("teams.view"))
        else:
            result = DB.selectAll("""
                Select * FROM IS601_UserTeams WHERE user_id = %s and team_id = %s
                """, user_id, id )
            if not result.rows:
                flash("Invalid ID! Unable to Delete League from watchlist","danger")
                return redirect(url_for("teams.view"))
    except Exception as e:
        if 'Duplicate' in str(e):
            flash('Duplicate record','danger')
        else: 
            flash(f" Following exception occured while Modfiying the record from watchlist: {str(e)}", "danger")
    
    if not id:
        flash('Id is missing','danger')
        redirect(url_for("teams.view"))
    else:
        if type_of == 'league':
            try:
                result = DB.delete("DELETE FROM IS601_UserLeagues WHERE league_id = %s and user_id = %s", id, user_id)
                if result.status:
                    flash("Deleted League from watchlist","success")
            except Exception as e:
                    flash(f" Following exception occured while deleting the League from watchlist: {str(e)}", "danger")
        else:
            try:
                result = DB.delete("DELETE FROM IS601_UserTeams WHERE team_id = %s and user_id = %s", id, user_id)
                if result.status:
                    flash("Deleted Team from watchlist","success")
            except Exception as e:
                    flash(f" Following exception occured while deleting the Team from watchlist: {str(e)}", "danger")
    return redirect(url_for("teams.view",email = email))
        

@teams.route("/users", methods=["GET","POST"])
def users():
    rows = [] 
    try:
        result = DB.selectAll("SELECT id, username, email FROM IS601_Users LIMIT 100")
        if result.status and result.rows:
            rows = result.rows
        print(rows)
    except Exception as e:
        print(e)
        flash("Error getting roles", "danger")
    return render_template("user_list.html", rows=rows)


@teams.route("/add", methods=["GET","POST"])
def add():
    if request.method == "GET":
        id = request.args.get("user_id",None)
        print(id)
        if not id:
            return redirect(url_for("teams.users"))
        return render_template("watchlist_add.html", id = id)

    if request.method == "POST":
        #pr457 date - 04/25/2023
        user_id = request.form.get("user_id",None)
        if not user_id:
            return redirect(url_for("teams.users"))

        type_attr = request.form.get("type", None)
        print(type_attr)
        if type_attr == 'league':
            league_id = request.form.get('name', None)
            if league_id == '':
                flash("No League was selected","danger")
                return render_template("watchlist.html",apply_where = '')
        else:
            team_id = request.form.get('name', None)
            print(team_id)
            if team_id == '':
                flash("No Team was selected","danger")
                return render_template("watchlist.html",apply_where = 'team')
        
        #pr457 date - 04/25/2023
        has_error = False # use this to control whether or not an insert occurs
        if not has_error and type_attr == 'league':
            try:
                type_attr = ''
                result = DB.insertOne("""
            INSERT INTO IS601_UserLeagues (user_id, league_id)
                        VALUES (%(id)s, %(league_id)s)
                        ON DUPLICATE KEY UPDATE user_id=%(id)s, league_id = %(league_id)s
            """, {'id':user_id,'league_id':league_id}
                )
                #pr457 date - 04/25/2023
                if result.status:
                    flash("Added to Watchlist", "success")
                else:
                    flash("not added","danger")
            except Exception as e:
                #pr457 date - 04/25/2023
                flash(f" Following exception occured while adding the Watchlist record: {str(e)}", "danger")
        else:
            try:
                print('here we go')
                result = DB.insertOne("""
            INSERT INTO IS601_UserTeams (user_id, team_id)
                        VALUES (%(id)s, %(team_id)s)
                        ON DUPLICATE KEY UPDATE user_id=%(id)s, team_id = %(team_id)s
            """, {'id':user_id,'team_id':team_id}
                )
                #pr457 date - 04/25/2023
                if result.status:
                    flash("Added to Watchlist", "success")
                else:
                    flash("not added","danger")
            except Exception as e:
                #pr457 date - 04/25/2023
                flash(f" Following exception occured while adding the Watchlist record: {str(e)}", "danger")

    return redirect(url_for('teams.view'))

@teams.route("/associate", methods=["GET","POST"])
def associate():
    rows = []
    team_list = []
    league_list = []
    type_of = request.args.get('type_of','')
    league_name = request.args.get('league_name', None)
    team_name = request.args.get('team_name', None)

    
    if team_name:
        query1 = f"AND T.name like '%{team_name}%' GROUP BY UT.team_id LIMIT 100"
        type_of = 'team'
    else:
        query1 = 'GROUP BY UT.team_id LIMIT 100'
    if league_name:
        query2 = f"AND L.name like '%{league_name}%' GROUP BY UL.league_id LIMIT 100"
        type_of = 'league'
    else:
        query2 = 'GROUP BY UL.league_id LIMIT 100'
    if team_name and league_name:
        type_of = ''
    try:
        if type_of == '' or type_of == 'team':
            result_1 = DB.selectAll(f"SELECT T.name, COUNT(UT.user_id) as `count` FROM IS601_UserTeams UT JOIN IS601_Teams T on UT.team_id = T.id WHERE 1=1 {query1} ")
            if result_1.status and result_1.rows:
                team_list = result_1.rows
            else:
                flash('No teams found')
        if type_of == '' or type_of == 'league':
            result_2 = DB.selectAll(f"SELECT L.name, COUNT(UL.user_id) as `count` FROM IS601_UserLeagues UL JOIN IS601_Leagues L on UL.league_id = L.id WHERE 1=1 {query2} ")
            if result_2.status and result_2.rows:
                league_list = result_2.rows
            else:
                flash('No leagues found')
    except Exception as e:
        print(e)
        flash("Error getting user data", "danger")
    return render_template("association_list.html", team_list=team_list, league_list=league_list, type_of=type_of)

