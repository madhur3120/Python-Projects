import qrcode
import matplotlib.pyplot as plt

# Ask the user for a website link
website_link = input("Enter the website link: ")

# Generate the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(website_link)
qr.make(fit=True)

# Create an image from the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

image_path = "qr_code.png"
qr_image.save(image_path)
print(f"QR code saved as PNG: {image_path}")
# Display the QR code     
plt.imshow(qr_image)     
plt.axis('off')    
plt.show()     
        
        
        