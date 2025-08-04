from flask import Blueprint, render_template, request, redirect, url_for, current_app
from todo_app.models import MyTask
from todo_app import db

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task_content = request.form['content']
        new_task = MyTask(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
        except Exception as e:
            current_app.logger.error(f"Failed to add task: {e}")
        return redirect("/")

    tasks = MyTask.query.order_by(MyTask.created).all()
    return render_template('index.html', tasks=tasks)


@main.route("/delete/<int:id>")
def delete(id:int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"ERROR: {e}"


@main.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id:int):
    task = MyTask.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form['content']
        try: 
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"ERROR: {e}"
    else:
        return render_template('edit.html',task=task)
