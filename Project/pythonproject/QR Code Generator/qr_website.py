import qrcode

# Website URL
url = "https://www.youtube.com/results?search_query=kahani+suno+2.0"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code
qr_img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
qr_img.save("/Users/gunjandhurde/PycharmProjects/Project/pythonproject/QR Code Generator/Output/website_qr_code.png")

print("QR Code for the website generated and saved as website_qr_code.png")
