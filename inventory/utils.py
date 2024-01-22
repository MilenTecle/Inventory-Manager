from django.conf import settings
from django.urls import reverse
import qrcode
import cloudinary.uploader
from io import BytesIO

def generate_qrcode(data, inventory_id):
    inventory_url = f"{settings.SITE_URL}{reverse('saved_list', kwargs={'pk': inventory_id})}"
    # Generate the QR code
    qr = qrcode.QRCode (
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=4,
    )
    qr.add_data(inventory_url)
    qr.make(fit=True)

    # Create an image from the QR code
    image = qr.make_image(fill_color='black', back_color='#E37F4D')

    # Save image to a BytesIO object
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)

    # Upload image to Cloudinary
    response = cloudinary.uploader.upload(buffer, format='png')

    print(f"Generated URL: {inventory_url}")
    return response['url']
    print(f"Cloudinary response: {response['url']}")

