from flask import Flask, render_template, request

from day2_langgraph import run_task_planner


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    error = None
    user_tasks = ""


    from day2_langgraph import run_task_planner

 
    if request.method == "POST":

        user_tasks = request.form.get("tasks", "").strip()

        if not user_tasks:
            error = "Please enter at least one task."

        else:
            try:
                result = run_task_planner(user_tasks)

            except Exception as exc:
                print(f"Error: {exc}")
                error = "An error occurred while processing the tasks."

    return render_template(
        "index.html",
        result=result,
        error=error,
        user_tasks=user_tasks
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)