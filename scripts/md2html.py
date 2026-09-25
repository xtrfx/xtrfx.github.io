#!/usr/bin/env python3.8
# Modified claude python routine for MD to HTML transition

import markdown
from pathlib import Path
import sys

output_dir = "./drafts/"
Path(output_dir).mkdir(exist_ok=True)

# Only the extensions you actually need
extensions = [
    'fenced_code',      # Enables ```code blocks```
    'codehilite',       # Syntax highlighting in those blocks
    'tables'            # Markdown table support
]

md_file = sys.argv[1]
with open(md_file, 'r', encoding='utf-8') as f:
  content = f.read()
  html_content = markdown.markdown(content, extensions=extensions)

# move this format into separate file    
  full_html = f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{md_file[:-3]}</title>
  <link rel="stylesheet" href="/styles/style.css">
</head>
<body>
  <div class="container">
    <header>
      <h1>XTRFX</h1>
      <p>Hardware and Security Project write-ups</p>
      <nav>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="#about">About</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <a href="/" class="back-link">Home</a>
      <article>
       {html_content}
      </article>

    <footer>
      <p>&copy; 2026. Gleb Solomentsev</p>
    </footer>

</body>
</html>"""
    
output_file = f"{output_dir}{md_file[:-3]}.html"
with open(output_file, 'w', encoding='utf-8') as f:
  f.write(full_html)
  print(f"{md_file} → {output_file}")
