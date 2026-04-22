with open("src/responsive.css", "r") as f:
    css = f.read()

# Fix name font size — smaller so Kaavya fits on one line
css = css.replace(
    ".hero-name {\n    font-size: 68px !important;\n  }",
    ".hero-name {\n    font-size: 52px !important;\n  }"
)

# Fix the word-break override that's breaking project text word by word
css = css.replace(
    "  /* General text overflow fix */\n  * {\n    word-break: break-word !important;\n    overflow-wrap: break-word !important;\n  }",
    "  /* General text overflow fix — only for elements that need it */\n  p, h1, h2, h3, span {\n    overflow-wrap: break-word !important;\n    word-break: normal !important;\n  }\n  /* Project title specifically needs to wrap cleanly */\n  .proj-card-inner h2 {\n    word-break: normal !important;\n    overflow-wrap: anywhere !important;\n    font-size: 26px !important;\n  }\n  .proj-card-inner p {\n    font-size: 14px !important;\n    line-height: 1.7 !important;\n    max-width: 100% !important;\n  }"
)

with open("src/responsive.css", "w") as f:
    f.write(css)
print("responsive.css updated!")

# Fix Projects.jsx — add classNames to the inner card and content
with open("src/pages/Projects.jsx", "r") as f:
    proj = f.read()

# Add className to the main card inner flex div
proj = proj.replace(
    "style={{ background: p.bg, borderRadius: 14, padding: '36px 40px',\n              display: 'flex', flexDirection: 'row', gap: 0,\n              alignItems: 'center', minHeight: 300, position: 'relative', overflow: 'hidden',",
    "className='proj-card-inner' style={{ background: p.bg, borderRadius: 14, padding: '36px 40px',\n              display: 'flex', flexDirection: 'row', gap: 0,\n              alignItems: 'center', minHeight: 300, position: 'relative', overflow: 'hidden',"
)

# Fix maxWidth on paragraph so it doesn't cause word-per-line on mobile
proj = proj.replace(
    "fontSize: 16, color: p.aboutColor, lineHeight: 1.85, margin: 0 }}",
    "fontSize: 16, color: p.aboutColor, lineHeight: 1.85, margin: 0, maxWidth: '100%' }}"
)

with open("src/pages/Projects.jsx", "w") as f:
    f.write(proj)
print("Projects.jsx updated!")

# Also fix the hero name — it uses inline fontSize 110px, override via className
with open("src/pages/Home.jsx", "r") as f:
    home = f.read()

home = home.replace(
    "<div style={{ fontFamily: 'DM Serif Display, serif', fontSize: '110px', color: '#E8729A', lineHeight: '0.88' }}>Kaavya<br />Indhu</div>",
    "<div className='hero-name' style={{ fontFamily: 'DM Serif Display, serif', fontSize: '110px', color: '#E8729A', lineHeight: '0.88' }}>Kaavya<br />Indhu</div>"
)

with open("src/pages/Home.jsx", "w") as f:
    f.write(home)
print("Home.jsx hero-name className added!")
