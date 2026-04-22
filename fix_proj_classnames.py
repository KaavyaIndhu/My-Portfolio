with open("src/pages/Projects.jsx", "r") as f:
    content = f.read()

# Find the main card div and add className
old = "key={p.id} onMouseEnter={() => setHovered(idx)} onMouseLeave={() => setHovered(null)}"
new = "key={p.id} className='proj-card-inner' onMouseEnter={() => setHovered(idx)} onMouseLeave={() => setHovered(null)}"

if old in content:
    content = content.replace(old, new)
    print("className added to project card!")
else:
    print("Pattern not found, searching...")
    idx = content.find("onMouseEnter={() => setHovered")
    print(repr(content[idx-50:idx+100]))

with open("src/pages/Projects.jsx", "w") as f:
    f.write(content)

# Also clean up duplicate CSS rules in responsive.css
with open("src/responsive.css", "r") as f:
    css = f.read()

# Remove the duplicate block at bottom
duplicate = """  /* Project title specifically needs to wrap cleanly */
  .proj-card-inner h2 {
    word-break: normal !important;
    overflow-wrap: anywhere !important;
    font-size: 26px !important;
  }
  .proj-card-inner p {
    font-size: 14px !important;
    line-height: 1.7 !important;
    max-width: 100% !important;
  }"""

if duplicate in css:
    css = css.replace(duplicate, "")
    print("Duplicate CSS removed!")

with open("src/responsive.css", "w") as f:
    f.write(css)
print("Done!")
