with open("src/pages/Home.jsx", "r") as f:
    content = f.read()

old = '''    <a href={url} target="_blank" rel="noreferrer"
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}'''

new = '''    <a href={url} target={item.download ? '_self' : '_blank'} rel="noreferrer" download={item.download ? 'KaavyaIndhu_Resume.pdf' : undefined}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}'''

if old in content:
    content = content.replace(old, new)
    with open("src/pages/Home.jsx", "w") as f:
        f.write(content)
    print("Resume fix applied!")
else:
    print("Pattern not found - share the output of: sed -n '10,25p' src/pages/Home.jsx")
