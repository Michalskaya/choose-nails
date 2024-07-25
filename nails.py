import random
import webbrowser
import urllib.parse

# Lists of colors and designs
colors = ["Red", "Pink", "Orange", "Yellow", "Green", "Blue", "Purple", "Black", "White", "Lavender", "Nude", "Neon", "Pastel"]
designs = ["Floral", "French tips", "Wiggly lines", "Glitter", "3D texture", "Hearts", "Ombre", "Animal print", "Marble Effect", "Polka Dots", "Stripes", "Glitter Gradient",
"Watercolor", "Matte Finish", "Fruit Design"]

def generate_nail_idea():
    color = random.choice(colors)
    design = random.choice(designs)
    return color, design

def search_pinterest(color, design):
    query = f"{color} {design} nails"
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.pinterest.com/search/pins/?q={encoded_query}"
    webbrowser.open(url)

# Generate a nail idea
color, design = generate_nail_idea()

# Print the result
print(f"Your random nail design idea:\nColor: {color}\nDesign: {design}")

# Search on Pinterest
search_pinterest(color, design)