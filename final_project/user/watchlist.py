from flask import Blueprint, flash, render_template, request, redirect, url_for, session, current_app
from flask_login import login_user, login_required, logout_user, current_user
from sql.db import DB
from roles.forms import RoleForm
from werkzeug.datastructures import MultiDict
from roles.permissions import admin_permission
import json
import http.client
import sql.config as config
watchlist = Blueprint('watchlist', __name__, url_prefix='/watchlist',template_folder='templates')

# uses admin_permission from roles.permissions (flask_principal way)
# https://stackoverflow.com/a/20069821 (for http_exception)


@watchlist.route("/add", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("watchlist.html")

    if request.method == "POST":
        #pr457 date - 04/25/2023
        user_id = json.loads(session['user'])['id']

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

    return redirect(url_for('watchlist.view',apply_where=type_attr))

#pr457 date - 04/25/2023
@watchlist.route("/view", methods=["GET","POST"])
def view():
    result_list = ''
    league_list = []
    team_list = []
    apply_where = request.args.get("apply_where",'')
    league_id = request.args.get("name",None)
    league_name = request.args.get("league_name",None)
    team_name = request.args.get("team_name",None)
    country_name = request.args.get("country_name",None)
    column = request.args.get("column",None)
    order = request.args.get("order",None)
    limit = request.args.get("limit", 10)
    print(limit)
    allowed_columns = ['name','country']
    allowed_columns_tuples = [(c, c) for c in allowed_columns]
    print(apply_where)
    if request.method == "GET" or request.method == "POST":

        user_id = json.loads(session['user'])['id']
            
        has_error = False # use this to control whether or not an insert occurs
        #pr457 date - 04/25/2023
        if not has_error:
            try:
                query = ''
                if apply_where == '':
                    if league_name:
                        query+= f''' AND L.name like '%{league_name}%' '''
                    if country_name:
                        query+= f" AND L.country like '%{country_name}%' "
                    try:
                        if limit and int(limit) > 0 and int(limit) <= 100:
                            query += f" LIMIT {limit}"
                        else:
                            flash("Limit entered is out of bounds. Limit should be in between 0 and 100", "error")
                    except Exception as e:
                            flash("ValueError, the limit entered is not a number", "error")
                result_1 = DB.selectAll("""
           Select id, name, country, logo from IS601_Leagues L JOIN 
           (Select league_id from IS601_UserLeagues WHERE user_id=%(id)s) U on U.league_id = L.id Where 1=1
            """+query, {'id':user_id}
                )
                if not result_1.rows and apply_where == '':
                    flash("Couldn't find any Watchlist records", "danger")
                league_list = result_1.rows
                query = ''
                if apply_where == 'team':
                    if team_name:
                        query+=f" AND L.name like '%{team_name}%'"
                    if country_name:
                        query+=f" AND L.country like '%{country_name}%'"
                    if league_id:
                        query+=f" AND L.league_id = '%{league_id}%'"
                    if column and order:
                        print(column, order)
                    if column in allowed_columns \
                        and order in ["asc", "desc"]:
                        query += f" ORDER BY {column} {order}"
                    try:
                        if limit and int(limit) > 0 and int(limit) <= 100:
                            query += f" LIMIT {limit}"
                        else:
                            flash("Limit entered is out of bounds. Limit should be in between 0 and 100", "error")
                    except Exception as e:
                            flash("ValueError, the limit entered is not a number", "error")

                result_2 = DB.selectAll("""
           Select id, name, country, logo, league_id from IS601_Teams L JOIN 
           (Select team_id from IS601_UserTeams WHERE user_id=%(id)s) U on U.team_id = L.id Where 1=1
            """+query, {'id':user_id})
                team_list = result_2.rows
                #pr457 date - 04/25/2023
                if not result_2.rows and apply_where == 'team':
                    flash("Couldn't find any Watchlist records", "danger")
            except Exception as e:
                #pr457 date - 04/25/2023
                flash(f" Following exception occured while Fetching the Watchlist record: {str(e)}", "danger")
    return render_template("watchlist_view.html",league_list = league_list, team_list = team_list, allowed_columns = allowed_columns_tuples,apply_where=apply_where)

#pr457 date - 04/25/2023
@watchlist.route("/delete", methods=["GET","POST"])
def delete():
    country_name = request.args.get("country_name",None)
    print(country_name)
    id = request.args.get("id",None)
    user_id = json.loads(session['user'])['id']
    type_of = request.args.get("type",None)
    apply_where = '' if type_of=='league' else type_of
    try:
        if type_of == 'league':
            result = DB.selectAll("""
                Select * FROM IS601_UserLeagues WHERE user_id = %s and league_id = %s
                """,user_id, id)
            print(result.rows)
            if not result.rows:
                flash("Invalid ID! Unable to Delete League from watchlist","danger")
                return redirect(url_for("watchlist.view",apply_where=apply_where,did=id))
        else:
            result = DB.selectAll("""
                Select * FROM IS601_UserTeams WHERE user_id = %s and team_id = %s
                """, user_id, id )
            if not result.rows:
                flash("Invalid ID! Unable to Delete League from watchlist","danger")
                return redirect(url_for("watchlist.view",apply_where=apply_where,did=id))
    except Exception as e:
        if 'Duplicate' in str(e):
            flash('Duplicate record','danger')
        else:
            flash(f" Following exception occured while Modfiying the record from watchlist: {str(e)}", "danger")
    
    if not id:
        flash('Id is missing','danger')
        redirect(url_for("watchlist.view",apply_where=apply_where))
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
    return redirect(url_for("watchlist.view",apply_where=apply_where,country_name=country_name,did=id))

#pr457 date - 04/25/2023
@watchlist.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get("id",None)
    user_id = json.loads(session['user'])['id']
    type_of = request.args.get("type",None)
    apply_where = '' if type_of=='league' else type_of
    button_type = request.args.get("submit_button",'')
    print(id)
    print(user_id)
    print(button_type)
    if button_type == "edit":
        if not id:
            flash('Id is missing','danger')
            redirect(url_for("watchlist.view",apply_where=apply_where))
        else:
            try:
                if type_of == 'league':
                    result = DB.selectAll("""
                        Select * FROM IS601_UserLeagues WHERE user_id = %s and league_id = %s
                        """,user_id, id)
                    print(result.rows)
                    if result.rows:
                        flash("Fecthed League from watchlist","success")
                    else:
                        flash("Invalid ID! Unable to Fetch League from watchlist","danger")
                        return redirect(url_for("watchlist.view",apply_where=apply_where))
                else:
                    result = DB.selectAll("""
                        Select * FROM IS601_UserTeams WHERE user_id = %s and team_id = %s
                        """, user_id, id )
                    if result.rows:
                        flash("Fetched League from watchlist","success")
                    else:
                        flash("Invalid ID! Unable to Fetch League from watchlist","danger")
                        return redirect(url_for("watchlist.view",apply_where=apply_where))
            except Exception as e:
                if 'Duplicate' in str(e):
                    flash('Duplicate record','danger')
                else:
                    flash(f" Following exception occured while Modfiying the record from watchlist: {str(e)}", "danger")
            return render_template("watchlist_edit.html",id=id,type=type_of)
    else:
        user_id = json.loads(session['user'])['id']
        id = request.args.get('id',None)
        type_of = request.args.get("type",None)
        previous = (request.args.get("previous",None))
        print(id)
        if not id or not previous:
            flash("Invalid id, Please select an option","danger")
            return render_template("watchlist_edit.html",id=id,type=type_of)
        else:
            try:
                if type_of == 'league':
                    result = DB.update("""
                        UPDATE IS601_UserLeagues SET league_id = %s WHERE user_id = %s and league_id = %s
                        """,id, user_id, previous)
                    print(result)
                    if result.status:
                        flash("Modified League from watchlist","success")
                    else:
                        flash("Unable to modify League from watchlist")
                        return redirect(url_for("watchlist.view",apply_where=apply_where))
                else:
                    result = DB.update("""
                        UPDATE IS601_UserTeams SET team_id = %s WHERE user_id = %s and team_id = %s
                        """,id, user_id, previous )
                    if result.status:
                        flash("Modified League from watchlist","success")
                    else:
                        flash("Unable to modify League from watchlist",'danger')
                        return redirect(url_for("watchlist.view",apply_where=apply_where))
            except Exception as e:
                if 'Duplicate' in str(e):
                    flash('Duplicate record','danger')
                else:
                    flash(f" Following exception occured while Modfiying the record from watchlist: {str(e)}", "danger")
            return redirect(url_for("watchlist.view", apply_where=apply_where))
        
#pr457 date - 04/25/2023
@watchlist.route("/viewstatistics", methods=["GET", "POST"])
def viewstatistics():
    league_id = request.args.get("league_id")
    team_id = request.args.get('id')
    print(team_id)
    print(league_id)
    headers = {
    'x-rapidapi-host': config.host,
    'x-rapidapi-key': config.key
    }
    conn = http.client.HTTPSConnection(config.host)
    conn.request("GET", f"/teams/statistics?team={team_id}&season=2022&league={league_id}", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    response = json.loads(data)['response']
    print(response)
    fixtures = response['fixtures']
    goals_for = response['goals']['for']
    goals_against = response['goals']['against']
    team_info = response['team']
    response_info = response['league']
    return render_template("view.html",fixtures=fixtures,goals_for=goals_for,goals_against=goals_against,team_info=team_info,response_info=response_info)

            
#pr457 date - 04/25/2023
@current_app.template_global()
def get_leagues():
        from sql.db import DB
        try:
            print("get leagues")
            # note this triggers for GET and POST
            result = DB.selectAll("SELECT id, name FROM IS601_Leagues")
            if result.status:
                return result.rows or []
        except Exception as e:
            print(e)
        return []

#pr457 date - 04/25/2023
@current_app.template_global()
def get_teams():
    from sql.db import DB
    try:
        print("get Teams")
        # note this triggers for GET and POST
        result = DB.selectAll("SELECT id, name, code, logo, country FROM IS601_Teams")
        if result.status:
            return result.rows or []
    except Exception as e:
        print(e)
    return []

#pr457 date - 04/25/2023
@watchlist.route('/getall', methods=["GET","POST"])
def store_teams():
    league_ids = []
    from sql.db import DB
    try:
        print("get leagues")
        result = DB.selectAll("SELECT id, name FROM IS601_Leagues")
        if result.status:
            league_ids = result.rows
    except Exception as e:
        print(e)
    query = '''INSERT INTO IS601_Teams (id, name, country, code, logo, league_id)
                        VALUES (%(id)s, %(name)s, %(country)s, %(code)s, %(logo)s, %(league_id)s)
                        ON DUPLICATE KEY UPDATE 
                        id=values(id),
                        name=values(name),
                        country=values(country),
                        code=values(code),
                        logo=values(logo),
                        league_id=values(league_id) '''
    #pr457 date - 04/25/2023
    headers = {
    'x-rapidapi-host': config.host,
    'x-rapidapi-key': config.key
    }
    conn = http.client.HTTPSConnection(config.host)
    for league in league_ids:

        conn.request("GET", f"/teams?league={league['id']}&season=2022", headers=headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        response = json.loads(data)['response']
        teams = [x['team'] for x in response]
        for team in teams:
            del team['national'],team['founded']
        teams = [dict(item, **{'league_id':league['id']}) for item in teams]
        if len(teams) > 0:
            print(f'Inserting or updating teams {len(teams)}')
            try:
                result = DB.insertMany(query,teams)
                flash(f"Inserted {len(teams)} teams records successfully!", "success")
            except Exception as e:
                flash("There was an error loading the data", "danger")

#pr457 date - 04/26/2023 
@watchlist.route('/getstandings', methods=["GET","POST"])
def getstandings():
    league_id = request.args.get("name")
    headers = {
    'x-rapidapi-host': config.host,
    'x-rapidapi-key': config.key
    }
    conn = http.client.HTTPSConnection(config.host)
    conn.request("GET", f"/standings/league?league={league_id}&season=2022", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    response = json.loads(data)
    print(response['response'][0].keys())
    standings = response['response'][0]['league']['standings'][0]
    return render_template("standings.html",standings=standings)
    


@watchlist.route('/getfixtures', methods=["GET","POST"])
def getfixtures():
    league_id = request.args.get("name")
    key = config.key
    return render_template('fixtures.html',key = key, league_id = league_id)

