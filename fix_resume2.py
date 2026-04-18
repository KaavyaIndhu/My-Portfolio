with open("src/pages/Home.jsx", "r") as f:
    content = f.read()

# Replace the ConnectLink component to handle resume specially
old = '''function ConnectLink({ item }) {
  const [hovered, setHovered] = React.useState(false)
  const url = item.url
  const label = item.label
  return (
    <a href={url} target={item.download ? '_self' : '_blank'} rel="noreferrer" download={item.download ? 'KaavyaIndhu_Resume.pdf' : undefined}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      style={{ display: 'flex', alignItems: 'center', gap: '10px', padding: '13px 22px', borderRadius: '40px', border: hovered ? '1px solid #E8729A' : '1px solid #cec5b5', fontSize: '15px', fontWeight: 500, color: hovered ? '#fff' : '#3a3430', textDecoration: 'none', background: hovered ? '#E8729A' : 'transparent', transition: 'all 0.15s', width: 'fit-content', minWidth: '180px' }}>
      <span style={{ width: '5px', height: '5px', borderRadius: '50%', backgroundColor: hovered ? '#fff' : '#E8729A', flexShrink: 0 }} />
      {label}
    </a>
  )
}'''

new = '''function ConnectLink({ item }) {
  const [hovered, setHovered] = React.useState(false)
  const handleClick = (e) => {
    if (item.download) {
      e.preventDefault()
      const link = document.createElement('a')
      link.href = item.url
      link.download = 'KaavyaIndhu_Resume.pdf'
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
    }
  }
  return (
    <a href={item.url} target={item.download ? '_self' : '_blank'} rel="noreferrer"
      onClick={handleClick}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      style={{ display: 'flex', alignItems: 'center', gap: '10px', padding: '13px 22px', borderRadius: '40px', border: hovered ? '1px solid #E8729A' : '1px solid #cec5b5', fontSize: '15px', fontWeight: 500, color: hovered ? '#fff' : '#3a3430', textDecoration: 'none', background: hovered ? '#E8729A' : 'transparent', transition: 'all 0.15s', width: 'fit-content', minWidth: '180px' }}>
      <span style={{ width: '5px', height: '5px', borderRadius: '50%', backgroundColor: hovered ? '#fff' : '#E8729A', flexShrink: 0 }} />
      {item.label}
    </a>
  )
}'''

if old in content:
    content = content.replace(old, new)
    with open("src/pages/Home.jsx", "w") as f:
        f.write(content)
    print("Resume fix applied!")
else:
    print("Pattern not found")
    idx = content.find('ConnectLink')
    print(repr(content[idx:idx+600]))
