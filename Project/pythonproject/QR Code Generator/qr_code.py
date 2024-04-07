import qrcode

# Text or data you want to encode in the QR code
data = "Hello, World! This is a QR Code."

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
qr_img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
qr_img.save("/Users/gunjandhurde/PycharmProjects/Project/pythonproject/QR Code Generator/Output/qrcode.png")

print("QR Code generated and saved as qrcode.png")
