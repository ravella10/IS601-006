from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
from views.forms import EmployeeForm
import re
from werkzeug.datastructures import MultiDict
import json
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    query = """SELECT e.id, e.first_name, e.last_name, e.email, e.company_id, IF(c.name is not null, c.name,'N/A') AS company_name
    FROM  IS601_MP3_Employees e LEFT JOIN IS601_MP3_Companies c ON e.company_id = c.id WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    allowed_columns_tuples = [(c, c) for c in allowed_columns]

    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    fn = request.args.get("fn",None)
    ln = request.args.get("ln",None)
    email = request.args.get("email",None)
    company = request.args.get("company",None)
    column = request.args.get("column",None)
    order = request.args.get("order",None)
    limit = request.args.get("limit", 10)
    # TODO search-3 append like filter for first_name if provided
    if fn:
        query += " AND first_name like %(fn)s"
        args['fn'] = (f"%{fn}%")
    # TODO search-4 append like filter for last_name if provided
    if ln:
        query += " AND last_name like %(ln)s"
        args['ln'] = (f"%{ln}%")
    # TODO search-5 append like filter for email if provided
    if email:
        query += " AND email like %(email)s"
        args['email'] = (f"%{email}%")
    # TODO search-6 append equality filter for company_id if provided
    if company:
        query += f" AND company_id = {company}"
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if column and order:
        print(column, order)
        if column in allowed_columns \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    try:
        if limit and int(limit) > 0 and int(limit) <= 100:
            query += " LIMIT %(limit)s"
            args["limit"] = int(limit)
        else:
            flash("Limit entered is out of bounds. Limit should be in between 0 and 100", "error")
    except Exception as e:
        flash("ValueError, the limit entered is not a number", "error")
        
    # TODO change this per the above requirements
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        flash(f"Following exception occured while fetching the Employee list: {str(e)}", "error")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation

    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns_tuples)

@employee.route("/add", methods=["GET","POST"])
def add():
    form = EmployeeForm(request.form)
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        company_id = request.form.get("company", None)
        # TODO add-2 first_name is required (flash proper error message)
        if first_name == '' or first_name == None:
            flash("first name is required", "danger")
            return redirect(url_for("employee.add"))
        # TODO add-3 last_name is required (flash proper error message)
        if last_name == '' or last_name == None:
            flash("last name is required", "danger")
            return redirect(url_for('employee.add'))
        # TODO add-4 company (may be None)
        if company_id == '':
            company_id = None
        # TODO add-5 email is required (flash proper error message)
        if email == '' or email == None:
            flash("email is required", "danger")
            return redirect("add")
        # TODO add-5a verify email is in the correct format
        regex = re.compile(r'[^@]+@[^@]+\.[^@]+')
        if not re.fullmatch(regex, email):
            flash("Invalid email", "warning")
            return redirect("add")
        has_error = False # use this to control whether or not an insert occurs
        data = {'first_name': first_name, 'last_name': last_name, 'email': email, 'company_id': company_id}
        if not has_error:
            try:
                result = DB.insertOne("""
            INSERT INTO IS601_MP3_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(company_id)s)
                        ON DUPLICATE KEY UPDATE first_name=%(first_name)s, last_name = %(last_name)s, email = %(email)s, company_id = %(company_id)s
            """, data
                ) # <-- TODO add-6 add query and add arguments
                if result.status:
                    flash("Created Employee Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                flash(f" Following exception occured while adding the employee record: {str(e)}", "danger")
    return render_template("add_employee.html",form = form)

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    form = EmployeeForm(request.form)
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    if not id: # TODO update this for TODO edit-1
        flash("ID is missing", "danger")
        return redirect("employee.search")
    else:
        if request.method == "POST":
            
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            company_id = request.form.get("company", '')
            # TODO edit-2 first_name is required (flash proper error message)
            if first_name == '' or first_name == None:
                flash("first name is required", "danger")
                return redirect("add")
            # TODO edit-3 last_name is required (flash proper error message)
            if last_name == '' or last_name == None:
                flash("last name is required", "danger")
                return redirect("add")
            # TODO edit-4 company (may be None)
            if company_id == '':
                company_id = None
            # TODO edit-5 email is required (flash proper error message)
            if email == '' or email == None:
                flash("email is required", "danger")
                return redirect("add")
            # TODO edit-5a verify email is in the correct format
            regex = re.compile(r'[^@]+@[^@]+\.[^@]+')
            if not re.fullmatch(regex, email):
                flash("Invalid email", "warning")
                return redirect("add")
            has_error = False # use this to control whether or not an insert occurs
            data = [first_name, last_name, company_id, email, id]

                
            if not has_error:
                try:
                    # TODO edit-6 fill in proper update query
                    result = DB.update("""
                UPDATE IS601_MP3_Employees SET first_name = %s, last_name = %s, company_id = %s, email = %s WHERE id = %s
                """, *data)
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    flash(f" Following exception occured while updating the employee: {str(e)}", "danger")
        row = {}
        try:
            # TODO edit-8 fetch the updated data 
            result = DB.selectOne("SELECT e.first_name, e.last_name, e.email, e.company_id, IF(c.name is not null, c.name,'N/A') AS company_name from IS601_MP3_Employees e LEFT JOIN IS601_MP3_Companies c ON e.company_id = c.id WHERE e.id = %s", id)
            if result.status:
                row = result.row
                if row:
                    form.process(MultiDict(row))
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash(f" Following exception occured while fetching the updated employee record: {str(e)}", "danger")
    # TODO edit-10 pass the employee data to the render template
    if row:
        company_id = row['company_id']
    else:
        company_id = ''
    return render_template("edit_employee.html", form=form, company_id=company_id)

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 if id is missing, flash necessary message and redirect to search
    #pr457 date - 3/11/2023
    id = request.args.get("id")
    args = {**request.args}
    
    if not id:
        flash("Id is missing","danger")
        redirect(url_for("employee.search"))
    else:
        try:
            result = DB.delete("DELETE FROM IS601_MP3_Employees WHERE id = %s", id)
            if result.status:
                flash("Deleted Employee record", "success")
        except Exception as e:
            flash(f" Following exception occured while deleting the employee record: {str(e)}", "danger")
        del args["id"]
    return redirect(url_for("employee.search", **args))