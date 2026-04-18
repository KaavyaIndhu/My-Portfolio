with open("src/pages/Home.jsx", "r") as f:
    content = f.read()

old = '          <div style={{ width: \'200px\', height: \'290px\', borderRadius: \'100px 100px 0 0\', overflow: \'hidden\', flexShrink: 0 }}>\n            <img src="/photo.png" alt="Kaavya Indhu" style={{ width: \'100%\', height: \'100%\', objectFit: \'cover\', objectPosition: \'center top\', display: \'block\' }} />\n          </div>'

new = '          <div style={{ width: \'100%\', height: \'100%\', position: \'absolute\', top: 0, left: 0, overflow: \'hidden\', borderRadius: \'14px\' }}>\n            <img src="/photo.png" alt="Kaavya Indhu" style={{ width: \'100%\', height: \'100%\', objectFit: \'cover\', objectPosition: \'center top\', display: \'block\' }} />\n          </div>'

if old in content:
    content = content.replace(old, new)
    with open("src/pages/Home.jsx", "w") as f:
        f.write(content)
    print("Photo size fixed!")
else:
    print("Pattern not found - trying alternative...")
    # try finding and printing what's there
    idx = content.find('photo.png')
    print(repr(content[idx-200:idx+200]))
