from flask import request, Flask, render_template, redirect, flash
import secrets
from pathlib import Path
import sqlitecloud
import settings

app = Flask(__name__)

app.config.from_pyfile('settings.py')

connection = sqlitecloud.connect("{}:{}/{}?apikey={}".format(settings.DB_HOST, settings.DB_PORT, settings.DB, settings.API_KEY))

@app.route("/", methods=["GET", "POST"])
def index():
    max_chars = 50
    
    if request.method == "POST":
        item = request.form.get("item")
                
        if not item:
            return render_template("error.html")
        
        connection.execute("INSERT INTO todo_lists (item) VALUES(?)", (item,))
        connection.commit()
        
        flash("Item Added!")
        
        return redirect("/")
    else:
        items = connection.execute("SELECT * FROM todo_lists")
          
        return render_template("index.html", max_chars=max_chars, items=items)


@app.route("/delete", methods=["GET", "POST"])
def delete():
  
  if request.method == "POST":
    id = request.form.getlist("id")
    
    
    print(id)
      
    if not id:
      return render_template("error.html")
    
    for id in id:
      connection.execute("DELETE FROM todo_lists WHERE id = ?", (id,))
    
    connection.commit()

    if len(id) > 1:
      flash("Items Deleted!")
    else:
      flash("Item Deleted!")
      
    return redirect("/")
  
  else:
    items = connection.execute("SELECT * FROM todo_lists")
    
    return render_template("delete.html", items=items)
  
  
@app.route("/edit", methods=["GET", "POST"])
def edit():
  max_chars = 50
  
  if request.method == "POST":
    
    id = request.form.get("id")
    item = request.form.get("item")
    
    print(id)
    print(item)
    
    if not id or not item:
      return render_template("error.html")
    
    connection.execute("UPDATE todo_lists SET item = ? WHERE id = ?", (item, id,))
    connection.commit()

    flash("Item Edited!")
    
    return redirect("/")
  
  else:
    items = connection.execute("SELECT * FROM todo_lists")
     
    return render_template("edit.html", max_chars=max_chars, items=items)