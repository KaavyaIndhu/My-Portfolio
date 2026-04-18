f = open("src/pages/Home.jsx", "r")
content = f.read()
f.close()

content = content.replace(
    "illustration={<InterestsIllustration />} onClick={() => navigate('/experience')}",
    "illustration={<ExperienceIllustration />} onClick={() => navigate('/experience')}"
)

f = open("src/pages/Home.jsx", "w")
f.write(content)
f.close()
print("Done!")
