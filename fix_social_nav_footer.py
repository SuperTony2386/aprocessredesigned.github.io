# Fix social-posts.html - Add nav and footer

with open('social-posts.html', 'r') as f:
    content = f.read()

# Add nav after <body> tag
nav_html = '''
<nav class="nav" style="background:#fff;border-bottom:2px solid #8b0000;padding:12px 24px;display:flex;align-items:center;gap:24px;">
  <a class="nav-logo" href="index.html" style="font-family:'Playfair Display',Georgia,serif;font-size:1.4rem;font-weight:900;color:#1a1a1a;text-decoration:none;">Tony<span style="color:#8b0000;">Wolf</span></a>
  <ul class="nav-links" style="list-style:none;display:flex;gap:18px;margin:0;padding:0;">
    <li><a href="index.html" style="color:#1a1a1a;text-decoration:none;font-weight:600;">Home</a></li>
    <li><a href="articles/index.html" style="color:#1a1a1a;text-decoration:none;font-weight:600;">All Articles</a></li>
    <li><a href="search.html" style="color:#1a1a1a;text-decoration:none;font-weight:600;">Search</a></li>
  </ul>
</nav>
'''

# Add footer before </body>
footer_html = '''
<footer class="footer" style="background:#1a1a1a;color:#f8f5f0;text-align:center;padding:24px;margin-top:40px;">
  <p style="margin:0;">
    &copy; 2026 TonyWolf.press &nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="index.html" style="color:#c9963a;text-decoration:none;">Home</a> &nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="articles/index.html" style="color:#c9963a;text-decoration:none;">All Articles</a>
  </p>
</footer>
'''

# Insert nav after <body>
content = content.replace('<body>', '<body>' + nav_html, 1)

# Insert footer before </body>
content = content.replace('</body>', footer_html + '\n</body>')

with open('social-posts.html', 'w') as f:
    f.write(content)
print("Fixed: social-posts.html - added nav and footer")
