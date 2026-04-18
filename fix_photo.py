with open("src/pages/Home.jsx", "r") as f:
    content = f.read()

old = '''          <div style={{ width: '200px', height: '290px', backgroundColor: '#ccc4b5', borderRadius: '100px 100px 0 0', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <span style={{ fontSize: '52px', opacity: 0.22 }}>:)</span>
          </div>
          <div style={{ position: 'absolute', bottom: '14px', fontSize: '10px', color: '#9a9285', letterSpacing: '0.07em' }}>your photo here</div>'''

new = '''          <div style={{ width: '200px', height: '290px', borderRadius: '100px 100px 0 0', overflow: 'hidden', flexShrink: 0 }}>
            <img src="/photo.jpg" alt="Kaavya Indhu" style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center top', display: 'block' }} />
          </div>'''

if old in content:
    content = content.replace(old, new)
    with open("src/pages/Home.jsx", "w") as f:
        f.write(content)
    print("Photo added successfully!")
else:
    print("Pattern not found")
