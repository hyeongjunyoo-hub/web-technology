import os
import re

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
    "index-2.html"
]

target_pattern = re.compile(
    r'(<li><a\s+(?:class="[^"]*"\s+)?href="blog\.html">자취방 라운지</a></li>)'
)

replacement = (
    r'\1\n          '
    r'<li><a id="nav-login" href="login.html">로그인</a></li>\n          '
    r'<li><a href="cart.html">장바구니</a></li>'
)

for file_name in html_files:
    file_path = os.path.join(workspace_dir, file_name)
    if not os.path.exists(file_path):
        print(f"Skipping non-existent file: {file_name}")
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if already updated
    if 'id="nav-login"' in content or 'cart.html' in content:
        print(f"File already updated: {file_name}")
        continue
        
    # We want to replace standard occurrences of blog.html item
    new_content, count = target_pattern.subn(replacement, content)
    if count > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated: {file_name} ({count} replacements)")
    else:
        # Try with double spaces if any
        target_pattern_spaces = re.compile(
            r'(<li><a\s+(?:class="[^"]*"\s+)?href="blog\.html">\s*자취방 라운지\s*</a></li>)'
        )
        new_content, count = target_pattern_spaces.subn(replacement, content)
        if count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully updated (with spaces): {file_name}")
        else:
            # Try plain text replacement for safety
            # Let's search for blog.html link and insert login/cart after it manually
            idx = content.find('href="blog.html"')
            if idx == -1:
                # Try double space
                idx = content.find('href="blog.html"')
            if idx != -1:
                # Find end of this li
                end_li_idx = content.find('</li>', idx)
                if end_li_idx != -1:
                    insert_pos = end_li_idx + 5
                    new_content = (
                        content[:insert_pos] +
                        '\n          <li><a id="nav-login" href="login.html">로그인</a></li>' +
                        '\n          <li><a href="cart.html">장바구니</a></li>' +
                        content[insert_pos:]
                    )
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated via string matching: {file_name}")
                else:
                    print(f"Could not find end of li in: {file_name}")
            else:
                print(f"Could not find blog.html in: {file_name}")
