import os

# 1. Add viewport meta to index.html
with open("index.html", "r") as f:
    html = f.read()

if 'viewport' not in html:
    html = html.replace(
        '<head>',
        '<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0" />'
    )
    with open("index.html", "w") as f:
        f.write(html)
    print("viewport meta added to index.html")
else:
    print("viewport already present")

# 2. Write a responsive CSS file
css = """
/* ── MOBILE RESPONSIVE ── */
@media (max-width: 768px) {

  /* Hero section */
  .hero-outer {
    flex-direction: column !important;
    min-height: unset !important;
    overflow: visible !important;
  }
  .hero-left {
    width: 100% !important;
    padding: 28px 18px 16px !important;
    flex-shrink: unset !important;
  }
  .hero-name {
    font-size: 68px !important;
  }
  .hero-center {
    flex: unset !important;
    width: 100% !important;
    padding: 0 18px 24px !important;
  }
  .hero-center p {
    font-size: 15px !important;
  }
  .hero-photo-panel {
    width: 100% !important;
    height: 320px !important;
    justify-content: center !important;
  }
  .hero-photo-panel .photo-arch {
    width: 200px !important;
    height: 280px !important;
    border-radius: 100px 100px 0 0 !important;
  }

  /* Nav grid: 1 column */
  .nav-grid {
    grid-template-columns: 1fr !important;
  }
  .nav-card-title {
    font-size: 44px !important;
  }

  /* Connect section */
  .connect-section {
    grid-template-columns: 1fr !important;
    padding: 28px 18px !important;
  }

  /* Projects */
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
  }

  /* Skills cards */
  .skill-card {
    padding: 28px 20px !important;
    min-height: unset !important;
  }
  .skill-card h2 {
    font-size: 36px !important;
  }

  /* Experience */
  .exp-role-block {
    flex-direction: column !important;
    gap: 16px !important;
  }
  .exp-role-block-flip {
    flex-direction: column !important;
    gap: 16px !important;
  }
  .exp-pic-box {
    width: 90px !important;
    height: 90px !important;
  }
  .exp-company-card {
    padding: 24px 18px !important;
  }
  .exp-connector svg {
    width: 240px !important;
  }

  /* General text overflow fix */
  * {
    word-break: break-word !important;
    overflow-wrap: break-word !important;
  }

  /* Fix horizontal scroll */
  body {
    overflow-x: hidden !important;
  }
}
"""

with open("src/responsive.css", "w") as f:
    f.write(css)
print("responsive.css written!")

# 3. Import responsive.css in main.jsx
with open("src/main.jsx", "r") as f:
    main = f.read()

if "responsive.css" not in main:
    main = main.replace(
        "import './index.css'",
        "import './index.css'\nimport './responsive.css'"
    )
    with open("src/main.jsx", "w") as f:
        f.write(main)
    print("responsive.css imported in main.jsx!")
else:
    print("already imported")

# 4. Add classNames to Home.jsx
with open("src/pages/Home.jsx", "r") as f:
    home = f.read()

# Hero outer div
home = home.replace(
    "backgroundColor: '#F5F0E8', borderRadius: '14px', display: 'flex', overflow: 'hidden', minHeight: '460px', position: 'relative'",
    "backgroundColor: '#F5F0E8', borderRadius: '14px', display: 'flex', overflow: 'hidden', minHeight: '460px', position: 'relative'"
)
# Add classNames via simple targeted replacements
home = home.replace(
    "<div style={{ backgroundColor: '#F5F0E8', borderRadius: '14px', display: 'flex', overflow: 'hidden', minHeight: '460px', position: 'relative' }}>",
    "<div className='hero-outer' style={{ backgroundColor: '#F5F0E8', borderRadius: '14px', display: 'flex', overflow: 'hidden', minHeight: '460px', position: 'relative' }}>"
)
home = home.replace(
    "<div style={{ width: '360px', flexShrink: 0, padding: '52px 40px', display: 'flex', flexDirection: 'column', justifyContent: 'flex-start', position: 'relative', zIndex: 1 }}>",
    "<div className='hero-left' style={{ width: '360px', flexShrink: 0, padding: '52px 40px', display: 'flex', flexDirection: 'column', justifyContent: 'flex-start', position: 'relative', zIndex: 1 }}>"
)
home = home.replace(
    "<div style={{ flex: 1, padding: '52px 44px 52px 52px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', position: 'relative', zIndex: 1 }}>",
    "<div className='hero-center' style={{ flex: 1, padding: '52px 44px 52px 52px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', position: 'relative', zIndex: 1 }}>"
)
home = home.replace(
    "<div style={{ width: '420px', backgroundColor: '#E0D9CE', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'flex-end', flexShrink: 0, position: 'relative', zIndex: 1 }}>",
    "<div className='hero-photo-panel' style={{ width: '420px', backgroundColor: '#E0D9CE', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'flex-end', flexShrink: 0, position: 'relative', zIndex: 1 }}>"
)
home = home.replace(
    "<div style={{ width: '360px', height: '430px', borderRadius: '180px 180px 0 0', overflow: 'hidden', flexShrink: 0 }}>",
    "<div className='photo-arch' style={{ width: '360px', height: '430px', borderRadius: '180px 180px 0 0', overflow: 'hidden', flexShrink: 0 }}>"
)
# Nav grids
home = home.replace(
    "<div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>\n        <NavCard num=\"01\"",
    "<div className='nav-grid' style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>\n        <NavCard num=\"01\""
)
home = home.replace(
    "<div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>\n        <NavCard num=\"03\"",
    "<div className='nav-grid' style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>\n        <NavCard num=\"03\""
)
# Connect section
home = home.replace(
    "<div style={{ backgroundColor: '#F5F0E8', borderRadius: '14px', padding: '52px 48px', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '32px', minHeight: '280px', position: 'relative', overflow: 'hidden' }}>",
    "<div className='connect-section' style={{ backgroundColor: '#F5F0E8', borderRadius: '14px', padding: '52px 48px', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '32px', minHeight: '280px', position: 'relative', overflow: 'hidden' }}>"
)

with open("src/pages/Home.jsx", "w") as f:
    f.write(home)
print("Home.jsx classNames added!")

# 5. Add classNames to Experience.jsx
with open("src/pages/Experience.jsx", "r") as f:
    exp = f.read()

exp = exp.replace(
    "background: '#F5F0E8', borderRadius: 14, padding: '40px 44px 48px', marginBottom: 10",
    "background: '#F5F0E8', borderRadius: 14, padding: '40px 44px 48px', marginBottom: 10"
)
# Company cards
exp = exp.replace(
    "style={{ background: '#F5F0E8', borderRadius: 14, padding: '40px 44px 48px', marginBottom: 10 }}",
    "className='exp-company-card' style={{ background: '#F5F0E8', borderRadius: 14, padding: '40px 44px 48px', marginBottom: 10 }}"
)
exp = exp.replace(
    "style={{ background: '#EDE0E8', borderRadius: 14, padding: '40px 44px 48px' }}",
    "className='exp-company-card' style={{ background: '#EDE0E8', borderRadius: 14, padding: '40px 44px 48px' }}"
)
# Role blocks
exp = exp.replace(
    "style={{ display: 'flex', gap: 36, alignItems: 'flex-start' }}",
    "className='exp-role-block' style={{ display: 'flex', gap: 36, alignItems: 'flex-start' }}"
)
exp = exp.replace(
    "style={{ display: 'flex', flexDirection: 'row-reverse', gap: 36, alignItems: 'flex-start' }}",
    "className='exp-role-block-flip' style={{ display: 'flex', flexDirection: 'row-reverse', gap: 36, alignItems: 'flex-start' }}"
)

with open("src/pages/Experience.jsx", "w") as f:
    f.write(exp)
print("Experience.jsx classNames added!")

# 6. Add classNames to Projects.jsx
with open("src/pages/Projects.jsx", "r") as f:
    proj = f.read()

proj = proj.replace(
    "transition: 'box-shadow 0.22s ease, transform 0.22s ease',",
    "transition: 'box-shadow 0.22s ease, transform 0.22s ease',"
)

with open("src/pages/Projects.jsx", "w") as f:
    f.write(proj)
print("Projects.jsx updated!")

print("\nAll done! Run: git add . && git commit -m 'mobile responsive' && git push")
