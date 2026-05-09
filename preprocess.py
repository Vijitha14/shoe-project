from rembg import remove
from PIL import Image

print("Starting program...")

input_path = "../raw-images/shoe.png"
output_path = "../processed-images/final_shoe.png"

print("Opening image...")
input_image = Image.open(input_path)

print("Removing background...")
output_image = remove(input_image)

print("Resizing...")
output_image = output_image.resize((800, 800))

print("Creating white background...")
bg = Image.new("RGBA", output_image.size, (255,255,255,255))

print("Combining...")
final = Image.alpha_composite(bg, output_image.convert("RGBA"))

print("Saving...")
final.save(output_path)

print("Processing completed!")