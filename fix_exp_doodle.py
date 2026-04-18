f = open("src/pages/Home.jsx", "r")
content = f.read()
f.close()

content = content.replace(
    'title="My Experience" sub="Where I have been" doodle="*"',
    'title="My Experience" sub="Where I have been" doodle="~ work ~"'
)

f = open("src/pages/Home.jsx", "w")
f.write(content)
f.close()
print("Done!")
