import random
import requests
from PIL import Image, ImageDraw, ImageFont

# Download a random quote
response = requests.get("https://api.quotable.io/random")
data = response.json()
quote = data["content"]
author = data["author"]

# Download a random background image
background_image_url = "https://source.unsplash.com/random"
background_image = Image.open(requests.get(background_image_url, stream=True).raw)

# Create a transparent layer for text
text_layer = Image.new("RGBA", background_image.size, (0, 0, 0, 0))

# Set up the font and text size
font = ImageFont.truetype("arial.ttf", 32)

# Set up the drawing context
draw = ImageDraw.Draw(text_layer)

# Calculate the text position to center it horizontally and vertically
text_width, text_height = draw.textsize(quote, font=font)
x = (background_image.width - text_width) / 2
y = (background_image.height - text_height) / 2

# Draw the quote and author on the transparent layer
draw.text((x, y), f"{quote}\n{author}", font=font, fill=(255, 255, 255, 255))

# Combine the background image and the text layer
final_image = Image.alpha_composite(background_image, text_layer)

# Save the final image to a file
final_image.save("quote_image.png")

# Display the final image
final_image.show()
