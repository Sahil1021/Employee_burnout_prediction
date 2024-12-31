from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    # Default values for form fields
    designation = ""
    resource_allocation = ""
    mental_fatigue_score = ""
    company_type = "Service"
    wfh_setup_available = "Yes"
    gender = "Male"
    prediction = None  # Default for burnout prediction

    if request.method == "POST":
        # Retrieve form data
        try:
            designation = float(request.form.get("designation", 0))
            resource_allocation = float(request.form.get("resource_allocation", 0))
            mental_fatigue_score = float(request.form.get("mental_fatigue_score", 0))
            company_type = request.form.get("company_type", "Service")
            wfh_setup_available = request.form.get("wfh_setup_available", "Yes")
            gender = request.form.get("gender", "Male")

            # Calculate burnout prediction (replace with your actual formula if different)
            # Example formula: Weighted sum of the inputs
            burnout_score = (
                (designation * 0.2) +
                (resource_allocation * 0.4) +
                (mental_fatigue_score * 0.4)
            ) / 10  # Normalize to a scale of 0-1

            # Ensure prediction is between 0 and 1
            prediction = round(min(max(burnout_score, 0), 1), 2)

        except ValueError:
            # Handle invalid input gracefully
            prediction = None

    return render_template(
        "index.html",
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
