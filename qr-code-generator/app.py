from flask import (
    Flask,
    render_template,
    request,
    send_file,
    send_from_directory
)

import os
import uuid
import qrcode


app = Flask(__name__)


# =========================================
# QR CODE FOLDER
# =========================================

QR_FOLDER = "generated_qr"

os.makedirs(
    QR_FOLDER,
    exist_ok=True
)


# =========================================
# HOME PAGE
# =========================================

@app.route(
    "/",
    methods=["GET", "POST"]
)
def home():

    qr_image = None
    error = None
    qr_text = ""

    if request.method == "POST":

        qr_text = request.form.get(
            "qr_text",
            ""
        ).strip()

        if not qr_text:

            error = (
                "Please enter text or a URL."
            )

        else:

            # Create a unique image filename
            filename = (
                f"{uuid.uuid4().hex}.png"
            )

            filepath = os.path.join(
                QR_FOLDER,
                filename
            )

            # Create QR Code
            qr = qrcode.QRCode(
                version=1,
                error_correction=(
                    qrcode.constants.ERROR_CORRECT_M
                ),
                box_size=10,
                border=4
            )

            qr.add_data(
                qr_text
            )

            qr.make(
                fit=True
            )

            image = qr.make_image(
                fill_color="black",
                back_color="white"
            )

            image.save(
                filepath
            )

            qr_image = filename

    return render_template(
        "index.html",
        qr_image=qr_image,
        error=error,
        qr_text=qr_text
    )


# =========================================
# DISPLAY QR CODE
# =========================================

@app.route(
    "/qr/<filename>"
)
def show_qr(filename):

    return send_from_directory(
        QR_FOLDER,
        filename
    )


# =========================================
# DOWNLOAD QR CODE
# =========================================

@app.route(
    "/download/<filename>"
)
def download_qr(filename):

    filepath = os.path.join(
        QR_FOLDER,
        filename
    )

    return send_file(
        filepath,
        as_attachment=True,
        download_name=(
            "raremotion-qr-code.png"
        )
    )


# =========================================
# START APPLICATION
# =========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )