import re

# Fix 1: disney-cruise-hantavirus.html - Add nav and footer to redirect page
with open('articles/disney-cruise-hantavirus.html', 'r') as f:
    content = f.read()

# Add nav before the box div
nav_html = '''<nav class="nav">
  <a class="nav-logo" href="../index.html">Tony<span>Wolf</span></a>
  <ul class="nav-links">
    <li><a href="../index.html">Home</a></li>
    <li><a href="index.html">All Articles</a></li>
    <li><a href="../search.html">Search</a></li>
  </ul>
</nav>
'''

# Add footer before </body>
footer_html = '''<footer class="footer">
  <p>
    &copy; 2026 TonyWolf.press &nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="../index.html">Home</a> &nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="index.html">All Articles</a>
  </p>
</footer>
'''

# Insert nav before <div class="box">
content = content.replace('<div class="box">', nav_html + '<div class="box">')

# Insert footer before </body>
content = content.replace('</body>', footer_html + '\n</body>')

with open('articles/disney-cruise-hantavirus.html', 'w') as f:
    f.write(content)
print("Fixed: disney-cruise-hantavirus.html - added nav and footer")

# Fix 2: digital-surveillance-privacy-war.html - Add missing footer
with open('articles/digital-surveillance-privacy-war.html', 'r') as f:
    content = f.read()

# Check if footer already exists
if '<footer' not in content:
    # Add footer before the first <script> tag that starts ninja removal (before </body>)
    footer_html = '''
<footer class="footer">
  <p>
    &copy; 2026 TonyWolf.press &nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="../index.html">Home</a> &nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="index.html">All Articles</a>
  </p>
</footer>

'''
    # Insert before the hideNinjaElements script block near end
    # Find the last </article> or main content end, then add footer before scripts
    # Actually, let's add it right before the first script that contains hideNinjaElements near the end
    # Better approach: add before </body>
    content = content.replace('</body>', footer_html + '</body>')
    with open('articles/digital-surveillance-privacy-war.html', 'w') as f:
        f.write(content)
    print("Fixed: digital-surveillance-privacy-war.html - added footer")
else:
    print("digital-surveillance-privacy-war.html already has footer")

# Fix 3: wealth-taxation-global-controversy.html - Add missing footer
with open('articles/wealth-taxation-global-controversy.html', 'r') as f:
    content = f.read()

if '<footer' not in content:
    footer_html = '''
<footer class="footer">
  <p>
    &copy; 2026 TonyWolf.press &nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="../index.html">Home</a> &nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="index.html">All Articles</a>
  </p>
</footer>

'''
    content = content.replace('</body>', footer_html + '</body>')
    with open('articles/wealth-taxation-global-controversy.html', 'w') as f:
        f.write(content)
    print("Fixed: wealth-taxation-global-controversy.html - added footer")
else:
    print("wealth-taxation-global-controversy.html already has footer")

