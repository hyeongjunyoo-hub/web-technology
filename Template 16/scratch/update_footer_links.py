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
    "register.html",
    "find_id.html",
    "find_pw.html",
    "basket.html"
]

target = '<a href="services.html">배달 야식 페어링</a>'
replacement = '<a href="pairing_delivery.html">배달 야식 페어링</a>'

for file_name in html_files:
    file_path = os.path.join(workspace_dir, file_name)
    if not os.path.exists(file_path):
        print(f"Skipping non-existent file: {file_name}")
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if target in content:
        new_content = content.replace(target, replacement)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated: {file_name}")
    else:
        print(f"Target not found in: {file_name}")
