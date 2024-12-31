from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    # Initialize variables to hold form data
    designation = ""
    resource_allocation = ""
    mental_fatigue_score = ""
    company_type = "Service"
    wfh_setup_available = "Yes"
    gender = "Male"
    prediction = None

    if request.method == "POST":
        # Retrieve form data from the request
        designation = request.form.get("designation", "")
        resource_allocation = request.form.get("resource_allocation", "")
        mental_fatigue_score = request.form.get("mental_fatigue_score", "")
        company_type = request.form.get("company_type", "Service")
        wfh_setup_available = request.form.get("wfh_setup_available", "Yes")
        gender = request.form.get("gender", "Male")

        # Perform prediction logic (replace this with your actual model)
        burnout_score = (
            float(designation) * 0.1
            + float(resource_allocation) * 0.2
            + float(mental_fatigue_score) * 0.7
        ) / 100

        prediction = round(burnout_score, 2)

    return render_template(
        "index.html",  # Ensure your template file is named `index.html`
        designation=designation,
        resource_allocation=resource_allocation,
        mental_fatigue_score=mental_fatigue_score,
        company_type=company_type,
        wfh_setup_available=wfh_setup_available,
        gender=gender,
        prediction=prediction,
    )


if __name__ == "__main__":
    app.run(debug=True)
