import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Extract footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# match everything from <!-- Compact Footer --> to </footer>
footer_match = re.search(r'<!-- Compact Footer -->\s*<footer.*?>.*?</footer>', content, re.DOTALL)
if not footer_match:
    footer_match = re.search(r'<footer.*?>.*?</footer>', content, re.DOTALL)

if footer_match:
    footer_content = footer_match.group(0)
    print("Found footer in index.html")
    
    for file in html_files:
        if file == 'index.html':
            continue
        
        with open(file, 'r', encoding='utf-8') as f:
            file_content = f.read()
            
        # replace the footer
        # match existing footer
        new_content = re.sub(r'<!-- Compact Footer -->\s*<footer.*?>.*?</footer>', footer_content, file_content, flags=re.DOTALL)
        if new_content == file_content:
            new_content = re.sub(r'<footer.*?>.*?</footer>', footer_content, file_content, flags=re.DOTALL)
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
else:
    print("Footer not found in index.html")
