import qrcode
import cloudinary.uploader
from io import BytesIO
from django.urls import reverse


def generate_qrcode(data):
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=5,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    image = qr.make_image(fill_color='black', back_color='#E37F4D')

    # Save image to a BytesIO object
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)

    # Upload image to Cloudinary
    response = cloudinary.uploader.upload(buffer, format='png')

    secure_url = cloudinary.CloudinaryImage(
        response['public_id']).build_url(secure=True)

    return secure_url
