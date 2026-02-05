from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form["data"]

        # Generate QR code
        img = qrcode.make(data)

        # Ensure static folder exists
        os.makedirs("static", exist_ok=True)

        # Save QR code
        img.save("static/qr.png")

        # 👉 THIS IS WHERE IT GOES
        return render_template("index.html", qr=True)

    # For normal page load (GET request)
    return render_template("index.html", qr=False)


@app.route("/download")
def download():
    return send_file("static/qr.png", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
