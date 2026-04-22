with open("src/responsive.css", "r") as f:
    css = f.read()

# Replace the projects section completely
old = """  /* Projects */
  .proj-card-inner {
    flex-direction: column !important;
    padding: 24px 18px !important;
    min-height: unset !important;
  }
  .proj-carousel {
    width: 100% !important;
  }
  .proj-carousel > div:first-child {
    width: 100% !important;
    height: 200px !important;
  }"""

new = """  /* Projects */
  .proj-card-inner {
    flex-direction: column !important;
    padding: 24px 18px !important;
    min-height: unset !important;
  }
  .proj-card-inner h2 {
    font-size: 22px !important;
    line-height: 1.2 !important;
    word-break: normal !important;
    overflow-wrap: break-word !important;
  }
  .proj-card-inner p {
    font-size: 14px !important;
    line-height: 1.65 !important;
    max-width: 100% !important;
    word-break: normal !important;
    overflow-wrap: break-word !important;
  }
  .proj-card-inner span {
    font-size: 12px !important;
  }
  .proj-carousel {
    width: 100% !important;
  }
  .proj-carousel > div:first-child {
    width: 100% !important;
    height: 180px !important;
  }"""

if old in css:
    css = css.replace(old, new)
    print("Projects CSS updated!")
else:
    print("Pattern not found, appending...")
    css += """
  /* Projects mobile fix */
  .proj-card-inner {
    flex-direction: column !important;
    padding: 24px 18px !important;
    min-height: unset !important;
  }
  .proj-card-inner h2 {
    font-size: 22px !important;
    line-height: 1.2 !important;
    word-break: normal !important;
    overflow-wrap: break-word !important;
  }
  .proj-card-inner p {
    font-size: 14px !important;
    line-height: 1.65 !important;
    max-width: 100% !important;
    word-break: normal !important;
    overflow-wrap: break-word !important;
  }"""

# Fix the general override that was breaking everything
css = css.replace(
    "  p, h1, h2, h3, span {\n    overflow-wrap: break-word !important;\n    word-break: normal !important;\n  }",
    "  p, h1, h2, h3 {\n    overflow-wrap: break-word !important;\n    word-break: normal !important;\n  }"
)

with open("src/responsive.css", "w") as f:
    f.write(css)
print("responsive.css saved!")

# Fix Projects.jsx — the real issue is the inline lineHeight: 1.85 on paragraphs
# and paddingRight: 8 on the content div — both need className overrides
with open("src/pages/Projects.jsx", "r") as f:
    proj = f.read()

# Add className to carousel wrapper
proj = proj.replace(
    "<ImageCarousel images={p.images} imgBg={p.imgBg} arrowBg={p.arrowBg} arrowText={p.arrowText} dotBg={p.dotBg} dotActive={p.dotActive} />",
    "<div className='proj-carousel'><ImageCarousel images={p.images} imgBg={p.imgBg} arrowBg={p.arrowBg} arrowText={p.arrowText} dotBg={p.dotBg} dotActive={p.dotActive} /></div>"
)

with open("src/pages/Projects.jsx", "w") as f:
    f.write(proj)
print("Projects.jsx carousel wrapped!")

# Now fix the name size — try 58px which should fit Kaavya on one line
with open("src/responsive.css", "r") as f:
    css2 = f.read()

css2 = css2.replace(
    ".hero-name {\n    font-size: 52px !important;\n  }",
    ".hero-name {\n    font-size: 58px !important;\n  }"
)

with open("src/responsive.css", "w") as f:
    f.write(css2)
print("Name size bumped to 58px!")
