f = open("src/pages/Home.jsx", "r")
content = f.read()
f.close()

content = content.replace(
    "title=\"My Interests\" sub=\"Beyond the screen\" doodle=\"*\" illustration={<InterestsIllustration />} onClick={() => navigate('/interests')}",
    "title=\"My Experience\" sub=\"Where I have been\" doodle=\"*\" illustration={<InterestsIllustration />} onClick={() => navigate('/experience')}"
)

f = open("src/pages/Home.jsx", "w")
f.write(content)
f.close()
print("Done!")
