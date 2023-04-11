from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
from werkzeug.datastructures import MultiDict
from views.forms import CompanyForm
import pycountry

company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # don't do SELECT *
    
    query = "SELECT c.id, c.name, c.address, c.city, c.country, c.state, c.zip, c.website, COUNT(e.id) AS Employees from IS601_MP3_Companies c LEFT JOIN IS601_MP3_Employees e ON e.company_id = c.id WHERE 1=1"
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    allowed_columns_tuples = [(c, c) for c in allowed_columns]
    # TODO search-2 get name, country, state, column, order, limit request args
    name = request.args.get("name",None)
    country = request.args.get("country",None)
    state = request.args.get("state",None)
    column = request.args.get("column",None)
    order = request.args.get("order",None)
    limit = request.args.get("limit", 10)
    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " AND name like %(name)s"
        args['name'] = (f"%{name}%")
    # TODO search-4 append an equality filter for country if provided
    if country:
        query += f" AND country = '{country}'"
    # TODO search-5 append an equality filter for state if provided
    if state:
        query += f" AND state = '{state}'"

    query += " GROUP BY c.id"
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    if column and order:
        print(column, order)
        if column in allowed_columns \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
    
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    try:
        if limit and int(limit) > 0 and int(limit) <= 100:
            query += " LIMIT %(limit)s"
            args["limit"] = int(limit)
        else:
            flash("Limit entered is out of bounds. Limit should be in between 0 and 100", "error")
    except Exception as e:
        flash("ValueError, the limit entered is not a number", "error")
    # try:
    #     type(int(limit))
    # except Exception as e:
    #     flash("ValueError, the limit entered is not a number", "error")

    # if not int(limit) > 0 and int(limit) <= 100:
    #     flash("Limit entered is out of bounds. Limit should be in between 0 and 100", "error")
    

    # TODO change this per the above requirements
    # query += " LIMIT %(limit)s"
    # args["limit"] = (limit)
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        #print(f"result {result.rows}")
        if result.status:
            rows = result.rows
            print(f"rows {rows}")
    except Exception as e:
        # TODO search-9 make message user friendly
        flash(f"Following exception occured while fetching the company list:{str(e)}", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns_tuples)

@company.route("/add", methods=["GET","POST"])
def add():
    form = CompanyForm(request.form)
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        name = request.form.get("name",None)
        address = request.form.get("address",None)
        city = request.form.get("city",None)
        zipcode = request.form.get("zip",None)
        website = request.form.get("website",None)
        state = request.form.get("state", None)
        country = request.form.get("country", None)
        # TODO add-2 name is required (flash proper error message)
        if name == '' or name == None:
            flash("Name is required", "danger")
            return redirect("add")
        # TODO add-3 address is required (flash proper error message)
        if address == '' or address == None:
            flash("Address is required", "danger")
            return redirect("add")
        # TODO add-4 city is required (flash proper error message)
        if city == '' or city == None:
            flash("City is required", "danger")
            return redirect("add")
        # TODO add-5 state is required (flash proper error message)
        if state == '' or state == None:
            flash("State is required", "danger")
            return redirect("add")
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        try:
            pycountry.subdivisions.get(code=state)
        except:
            flash("Invalid State")
            return redirect("add")
        # hint see geography.py and pycountry documentation
        # TODO add-6 country is required (flash proper error message)
        if country == '' or country == None:
            flash("Country is required", "danger")
            return redirect("add")
        # TODO add-6a country should be a valid country mentioned in pycountry
        try:
            pycountry.countries.get(alpha_2=country)
        except:
            flash("Invalid Country")
            return redirect("add")
                
        # hint see geography.py and pycountry documentation
        # TODO add-7 website is not required
        if website == '':
            website = 'N/A'
        # TODO add-8 zipcode is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        if zipcode == '' or zipcode == None:
            flash("Zipcode is required","danger")
            return redirect("add")

        has_error = False # use this to control whether or not an insert occurs
        data = {'name': name, 'address': address, 'city': city, 'country': country, 'state': state, 'zip': zipcode, 'website': website}

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Companies (name, address, city, country, state, zip, website)
                            VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                            ON DUPLICATE KEY UPDATE name=%(name)s, address = %(address)s, city = %(city)s, country = %(country)s, state = %(state)s, zip = %(zip)s, website = %(website)s
                """, data)# <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash(str(e), "danger")
        
    return render_template("add_company.html",form = form)

@company.route("/edit", methods=["GET", "POST"])
def edit():
    form = CompanyForm(request.form)
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    if id is None:
        flash("ID is missing", "danger")
        return redirect("company.search")
    else:
        if request.method == "POST":
            # data = (id,) # use this as needed, can convert to tuple if necessary
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            name = request.form.get("name",None)
            address = request.form.get("address",None)
            city = request.form.get("city",None)
            zipcode = request.form.get("zip",None)
            website = request.form.get("website",None)
            state = request.form.get("state", None)
            country = request.form.get("country", None)
            # TODO edit-2 name is required (flash proper error message)
            if name == '' or name == None:
                flash("Name is required", "danger")
                return redirect("add")
            # TODO edit-3 address is required (flash proper error message)
            if address == '' or address == None:
                flash("Address is required", "danger")
                return redirect("add")
            # TODO edit-4 city is required (flash proper error message)
            if city == '' or city == None:
                flash("City is required", "danger")
                return redirect("add")
            # TODO edit-5 state is required (flash proper error message)
            if state == '' or state == None:
                flash("State is required", "danger")
                return redirect("add")
            # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
            try:
                pycountry.subdivisions.get(code=state)
            except:
                flash("Invalid State")
                return redirect("add")
            # hint see geography.py and pycountry documentation
            # TODO edit-6 country is required (flash proper error message)
            if country == '' or country == None:
                flash("Country is required", "danger")
                return redirect("edit")
            # TODO edit-6a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            try:
                pycountry.countries.get(alpha_2=country)
            except:
                flash("Invalid Country")
                return redirect("add")
            # TODO edit-7 website is not required
            if website == '' or website == None:
                website = 'N/A'
            # TODO edit-8 zipcode is required (flash proper error message)
            if zipcode == '' or zipcode == None:
                flash("Zipcode is required","danger")
                return redirect("add")
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            data = [name, address, city, state, country, zipcode, website, id]
            has_error = False # use this to control whether or not an insert occurs

            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website
                    result = DB.update("""
                UPDATE IS601_MP3_Companies SET name = %s, address = %s, city = %s, state = %s, country = %s, zip = %s, website = %s WHERE id = %s
                """, *data)
                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    flash(f" Following exception occured while updating the company: {str(e)}", "danger")
                    print(f"{e}")
                    # flash(str(e), "danger")
        result = None
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT name, address, city, state, country, zip, website FROM IS601_MP3_Companies WHERE id = %s", id)
            if result.status:
                form.process(MultiDict(result.row))
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash(f" Following exception occured while fetching the updated company record: {str(e)}", "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", form=form, state=result.row['state'], country=result.row['country'])

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees see delete-5)
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 for all employees assigned to this company set their company_id to None/null
    # TODO delete-6 if id is missing, flash necessary message and redirect to search
    id = request.args.get("id")
    args = {**request.args}
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_MP3_Companies WHERE id = %s", id)
            if result.status:
                flash("Deleted Company record", "success")
        except Exception as e:
            flash(f" Following exception occured while deleting the company record: {str(e)}", "danger")
        del args["id"]
    return redirect(url_for("company.search", **args))
    