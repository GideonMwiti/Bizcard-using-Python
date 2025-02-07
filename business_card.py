from PIL import Image, ImageDraw, ImageFont

# Define the dimensions and create a new white image
width, height = 600, 400
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Attempt to load a TrueType font; fallback to the default if not available
try:
    title_font = ImageFont.truetype("arial.ttf", 36)
    header_font = ImageFont.truetype("arial.ttf", 20)
    text_font = ImageFont.truetype("arial.ttf", 16)
except IOError:
    title_font = ImageFont.load_default()
    header_font = ImageFont.load_default()
    text_font = ImageFont.load_default()

# Define text content
name = "GIDEON MWITI"
title = "IT Project Manager"
phone = "Phone: +254-798-985-389"
email = "Email: mwitigideon002@gmail.com"
linkedin = "LinkedIn: linkedin.com/in/GIDEONMWITI"
location = "Location: Kisii, Kenya"

services_title = "Services Offered:"
services = [
    "Agile Project Management",
    "Software Development Oversight",
    "Digital Transformation Execution",
    "Process Automation & Data Analytics",
    "Cloud Solutions",
    "Open to full-time employment & contract opportunities"
]

# Starting positions for text
padding = 20
current_y = padding

# Draw Name and Title
draw.text((padding, current_y), name, font=title_font, fill="black")
current_y += 50
draw.text((padding, current_y), title, font=header_font, fill="black")
current_y += 50

# Draw Contact Details
draw.text((padding, current_y), phone, font=text_font, fill="black")
current_y += 20
draw.text((padding, current_y), email, font=text_font, fill="black")
current_y += 20
draw.text((padding, current_y), linkedin, font=text_font, fill="black")
current_y += 20
draw.text((padding, current_y), location, font=text_font, fill="black")
current_y += 30

# Draw a horizontal line
draw.line((padding, current_y, width - padding, current_y), fill="black", width=2)
current_y += 10

# Draw Services Title
draw.text((padding, current_y), services_title, font=header_font, fill="black")
current_y += 30

# Draw each service item
for service in services:
    draw.text((padding + 20, current_y), f"- {service}", font=text_font, fill="black")
    current_y += 20

# Save the image as PNG
image.save("business_card.png")
print("Business card generated and saved as 'business_card.png'.")
