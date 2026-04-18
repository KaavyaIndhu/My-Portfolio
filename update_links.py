f = open("src/pages/Home.jsx", "r")
content = f.read()
f.close()

content = content.replace(
    "{ label: 'LinkedIn', url: 'https://linkedin.com' }",
    "{ label: 'LinkedIn', url: 'https://www.linkedin.com/in/kaavyaindhu' }"
)
content = content.replace(
    "{ label: 'GitHub', url: 'https://github.com' }",
    "{ label: 'GitHub', url: 'https://github.com/KaavyaIndhu' }"
)
content = content.replace(
    "{ label: 'Resume', url: '#' }",
    "{ label: 'Resume', url: '/resume.pdf' }"
)
content = content.replace(
    "{ label: 'Instagram', url: 'https://instagram.com' }",
    "{ label: 'Instagram', url: 'https://www.instagram.com/itsme_kaavya._/' }"
)
content = content.replace(
    "fontSize: '12px', fontWeight: 500, color: hovered ? '#fff' : '#3a3430', textDecoration: 'none', background: hovered ? '#E8729A' : 'transparent', transition: 'all 0.15s', width: 'fit-content', minWidth: '150px'",
    "fontSize: '15px', fontWeight: 500, color: hovered ? '#fff' : '#3a3430', textDecoration: 'none', background: hovered ? '#E8729A' : 'transparent', transition: 'all 0.15s', width: 'fit-content', minWidth: '180px'"
)
content = content.replace(
    "padding: '10px 18px', borderRadius: '40px', border: hovered ? '1px solid #E8729A' : '1px solid #cec5b5'",
    "padding: '13px 22px', borderRadius: '40px', border: hovered ? '1px solid #E8729A' : '1px solid #cec5b5'"
)
content = content.replace(
    "fontSize: '17px', color: '#9a9285', marginBottom: '20px'",
    "fontSize: '20px', color: '#9a9285', marginBottom: '20px'"
)
content = content.replace(
    "fontSize: '13px', color: '#9a9285', marginTop: '16px'",
    "fontSize: '17px', color: '#9a9285', marginTop: '16px'"
)
content = content.replace(
    "fontSize: '26px', color: '#3a3430'",
    "fontSize: '30px', color: '#3a3430'"
)
content = content.replace(
    "fontSize: '12px', color: '#7a7065', lineHeight: 1.7, marginTop: '8px'",
    "fontSize: '15px', color: '#7a7065', lineHeight: 1.7, marginTop: '8px'"
)
content = content.replace(
    "fontSize: '18px', color: '#E8729A', marginTop: '14px'",
    "fontSize: '22px', color: '#E8729A', marginTop: '14px'"
)
content = content.replace(
    "fontSize: '13px', color: '#E8729A', opacity: 0.5, marginTop: '2px'",
    "fontSize: '17px', color: '#E8729A', opacity: 0.5, marginTop: '2px'"
)

f = open("src/pages/Home.jsx", "w")
f.write(content)
f.close()
print("Done!")
