import os

workspace_dir = r"c:\Users\USER\Desktop\web_technology\Template 16"
html_files = [
    "index.html",
    "about.html",
    "services.html",
    "portfolio.html",
    "blog.html",
    "contact.html",
    "team.html",
    "blog-single.html",
    "portfolio-details.html",
    "index-2.html",
    "login.html",
    "basket.html"
]

for file_name in html_files:
    file_path = os.path.join(workspace_dir, file_name)
    if not os.path.exists(file_path):
        print(f"Skipping non-existent file: {file_name}")
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'cart.html' in content:
        new_content = content.replace('cart.html', 'basket.html')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated references in: {file_name}")
    else:
        print(f"No references to cart.html in: {file_name}")

# Delete cart.html if it exists
cart_path = os.path.join(workspace_dir, 'cart.html')
if os.path.exists(cart_path):
    try:
        os.remove(cart_path)
        print("Successfully deleted cart.html")
    except Exception as e:
        print(f"Error deleting cart.html: {e}")
