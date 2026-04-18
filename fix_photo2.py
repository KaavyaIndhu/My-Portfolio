with open("src/pages/Home.jsx", "r") as f:
    content = f.read()

old = 'src="/photo.jpg"'
new = 'src="/photo.png"'

if old in content:
    content = content.replace(old, new)
    with open("src/pages/Home.jsx", "w") as f:
        f.write(content)
    print("Fixed! Changed photo.jpg to photo.png")
else:
    print("Pattern not found")
