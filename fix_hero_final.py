with open("src/pages/Home.jsx", "r") as f:
    content = f.read()

# Fix resume link
content = content.replace(
    "{ label: 'Resume', url: '/resume.pdf', download: true },",
    "{ label: 'Resume', url: 'https://drive.google.com/uc?export=download&id=1-YJ68EkPAiWkS1jSFd_5jh7EgYcfAHsO', download: false },"
)

# Fix the entire hero box
old = '''      <div style={{ backgroundColor: '#F5F0E8', borderRadius: '14px', display: 'flex', overflow: 'hidden', minHeight: '460px', position: 'relative' }}>
        <div style={{ position: 'absolute', bottom: '-30px', left: '-10px', fontFamily: 'DM Serif Display, serif', fontSize: '200px', color: '#E8729A', opacity: 0.055, lineHeight: 1, userSelect: 'none', pointerEvents: 'none', whiteSpace: 'nowrap' }}>KaavyaIndhu</div>
        <div style={{ flex: 1, padding: '52px 48px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', position: 'relative', zIndex: 1 }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', padding: '5px 14px', borderRadius: '30px', border: '1px solid #E8729A', fontFamily: 'Caveat, cursive', fontSize: '14px', color: '#E8729A', width: 'fit-content', marginBottom: '8px' }}>
              <span style={{ width: '6px', height: '6px', borderRadius: '50%', background: '#E8729A', display: 'inline-block' }}></span>
              available for projects
            </div>
            <div style={{ fontFamily: 'Caveat, cursive', fontSize: '17px', color: '#9a9285' }}>Hi, since you are new here</div>
            <div style={{ fontFamily: 'DM Serif Display, serif', fontSize: '96px', color: '#E8729A', lineHeight: '0.88' }}>Kaavya<br />Indhu</div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginTop: '14px' }}>
              <div style={{ fontSize: '11px', color: '#7a7065', letterSpacing: '0.14em', textTransform: 'uppercase', fontWeight: 500 }}>Full Stack Developer</div>
              <div style={{ width: '24px', height: '1px', background: '#E8729A', opacity: 0.4 }}></div>
              <div style={{ fontSize: '11px', color: '#7a7065', letterSpacing: '0.14em', textTransform: 'uppercase', fontWeight: 500 }}>Tech . Marketing . HR . RnD</div>
            </div>
            <div style={{ fontFamily: 'Caveat, cursive', fontSize: '24px', color: '#8a8075', marginTop: '4px' }}>Bridging technology, people, and ideas.</div>
          </div>
          <div>
            <div style={{ fontSize: '15px', color: '#7a7065', lineHeight: 1.8, maxWidth: '380px', borderLeft: '2px solid #E8729A', paddingLeft: '16px' }}>I am a full stack developer who loves building things at the intersection of design and technology. I care deeply about creating experiences that feel good to use. Always learning, always building.</div>
            <div style={{ fontFamily: 'Caveat, cursive', fontSize: '14px', color: '#9a9285', marginTop: '10px' }}>Based in India</div>
          </div>
        </div>'''

new = '''      <div style={{ backgroundColor: '#F5F0E8', borderRadius: '14px', display: 'flex', overflow: 'hidden', minHeight: '460px', position: 'relative' }}>
        <div style={{ position: 'absolute', bottom: '-30px', left: '-10px', fontFamily: 'DM Serif Display, serif', fontSize: '200px', color: '#E8729A', opacity: 0.055, lineHeight: 1, userSelect: 'none', pointerEvents: 'none', whiteSpace: 'nowrap' }}>KaavyaIndhu</div>

        {/* LEFT — name only */}
        <div style={{ width: '340px', flexShrink: 0, padding: '52px 40px', display: 'flex', flexDirection: 'column', justifyContent: 'flex-start', position: 'relative', zIndex: 1 }}>
          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', padding: '5px 14px', borderRadius: '30px', border: '1px solid #E8729A', fontFamily: 'Caveat, cursive', fontSize: '14px', color: '#E8729A', width: 'fit-content', marginBottom: '14px' }}>
            <span style={{ width: '6px', height: '6px', borderRadius: '50%', background: '#E8729A', display: 'inline-block' }}></span>
            available for projects
          </div>
          <div style={{ fontFamily: 'Caveat, cursive', fontSize: '17px', color: '#9a9285', marginBottom: '6px' }}>Hi, since you are new here</div>
          <div style={{ fontFamily: 'DM Serif Display, serif', fontSize: '96px', color: '#E8729A', lineHeight: '0.88' }}>Kaavya<br />Indhu</div>
        </div>

        {/* CENTER — all details */}
        <div style={{ flex: 1, padding: '52px 36px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', position: 'relative', zIndex: 1 }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
              <div style={{ fontSize: '11px', color: '#7a7065', letterSpacing: '0.14em', textTransform: 'uppercase', fontWeight: 500 }}>Full Stack Developer</div>
              <div style={{ width: '24px', height: '1px', background: '#E8729A', opacity: 0.4 }}></div>
              <div style={{ fontSize: '11px', color: '#7a7065', letterSpacing: '0.14em', textTransform: 'uppercase', fontWeight: 500 }}>Tech . Marketing . HR . RnD</div>
            </div>
            <div style={{ fontFamily: 'Caveat, cursive', fontSize: '26px', color: '#8a8075' }}>Bridging technology, people, and ideas.</div>
            <div style={{ fontSize: '15px', color: '#7a7065', lineHeight: 1.85, maxWidth: '400px', borderLeft: '2px solid #E8729A', paddingLeft: '16px' }}>I am a full stack developer who loves building things at the intersection of design and technology. I care deeply about creating experiences that feel good to use. Always learning, always building.</div>
            <div style={{ fontFamily: 'Caveat, cursive', fontSize: '16px', color: '#9a9285' }}>Based in India</div>
          </div>

          {/* doodle at bottom of center */}
          <div style={{ opacity: 0.18, marginTop: '24px' }}>
            <svg width="180" height="60" viewBox="0 0 180 60" fill="none">
              <polyline points="10,45 30,25 50,38 75,15 100,28 125,10 150,22 170,14" stroke="#E8729A" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"/>
              <circle cx="75" cy="15" r="3.5" fill="#E8729A"/>
              <circle cx="125" cy="10" r="3.5" fill="#E8729A"/>
              <line x1="10" y1="52" x2="170" y2="52" stroke="#E8729A" strokeWidth="1" strokeLinecap="round"/>
            </svg>
          </div>
        </div>'''

if old in content:
    content = content.replace(old, new)
    with open("src/pages/Home.jsx", "w") as f:
        f.write(content)
    print("Hero layout updated!")
else:
    print("Pattern not found")
    idx = content.find("minHeight: '460px'")
    print(repr(content[idx-50:idx+200]))

# Also fix the photo panel width and remove the old middle section
content2_read = open("src/pages/Home.jsx").read()

old2 = '''        <div style={{ width: '240px', flexShrink: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', position: 'relative', zIndex: 1, padding: '28px 16px' }}>
          <svg width="200" height="300" viewBox="0 0 200 300" fill="none">
            <text x="10" y="48" fontFamily="DM Serif Display,serif" fontSize="64" fill="#E8729A" fillOpacity="0.12">"</text>
            <text x="20" y="84" fontFamily="Caveat,cursive" fontSize="18" fill="#5a4a42">Doing it before</text>
            <text x="20" y="108" fontFamily="Caveat,cursive" fontSize="18" fill="#5a4a42">you are ready is</text>
            <text x="20" y="132" fontFamily="Caveat,cursive" fontSize="18" fill="#E8729A">what makes</text>
            <text x="20" y="156" fontFamily="Caveat,cursive" fontSize="18" fill="#E8729A">you ready.</text>
            <text x="124" y="174" fontFamily="DM Serif Display,serif" fontSize="64" fill="#E8729A" fillOpacity="0.12">"</text>
            <line x1="20" y1="194" x2="60" y2="194" stroke="#E8729A" strokeWidth="1" opacity="0.3"/>
            <text x="20" y="210" fontFamily="Caveat,cursive" fontSize="14" fill="#c4a0b0">— Kaavya</text>
            <rect x="30" y="228" width="80" height="50" rx="5" stroke="#E8729A" strokeWidth="1.4" opacity="0.25"/>
            <rect x="30" y="228" width="80" height="11" rx="5" fill="#E8729A" fillOpacity="0.06" stroke="#E8729A" strokeWidth="1.4" opacity="0.25"/>
            <line x1="18" y1="278" x2="124" y2="278" stroke="#E8729A" strokeWidth="1.4" strokeLinecap="round" opacity="0.22"/>
            <polyline points="42,252 52,244 62,250 75,238 88,244" stroke="#E8729A" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round" opacity="0.3"/>
            <rect x="134" y="232" width="22" height="24" rx="3" stroke="#E8729A" strokeWidth="1.3" opacity="0.22"/>
            <path d="M156 239 Q163 239 163 245 Q163 251 156 251" stroke="#E8729A" strokeWidth="1.3" fill="none" opacity="0.2"/>
            <line x1="130" y1="256" x2="160" y2="256" stroke="#E8729A" strokeWidth="1.3" strokeLinecap="round" opacity="0.2"/>
            <path d="M140 231 Q142 226 140 221" stroke="#E8729A" strokeWidth="1.1" fill="none" strokeLinecap="round" opacity="0.18"/>
            <path d="M147 231 Q149 224 147 218" stroke="#E8729A" strokeWidth="1.1" fill="none" strokeLinecap="round" opacity="0.15"/>
            <text x="158" y="218" fontFamily="Caveat,cursive" fontSize="16" fill="#E8729A" opacity="0.2">&#10022;</text>
            <text x="8" y="234" fontFamily="Caveat,cursive" fontSize="12" fill="#E8729A" opacity="0.18">*</text>
            <text x="168" y="268" fontFamily="Caveat,cursive" fontSize="12" fill="#E8729A" opacity="0.15">*</text>
            <text x="100" y="298" textAnchor="middle" fontFamily="Caveat,cursive" fontSize="13" fill="#c4a0b0">always building &#9825;</text>
          </svg>
        </div>

        <div style={{ width: '360px', backgroundColor: '#E0D9CE', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'flex-end', flexShrink: 0, position: 'relative', zIndex: 1 }}>
          <span style={{ position: 'absolute', top: '20px', right: '28px', fontFamily: 'Caveat, cursive', fontSize: '28px', color: '#E8729A', opacity: 0.38 }}>*</span>
          <span style={{ position: 'absolute', top: '58px', left: '20px', fontFamily: 'Caveat, cursive', fontSize: '14px', color: '#E8729A', opacity: 0.25 }}>*</span>
          <span style={{ position: 'absolute', top: '100px', right: '18px', fontFamily: 'Caveat, cursive', fontSize: '18px', color: '#E8729A', opacity: 0.2 }}>o</span>
          <div style={{ position: 'absolute', top: '32px', left: '-36px', fontFamily: 'Caveat, cursive', fontSize: '15px', color: '#E8729A', opacity: 0.45, transform: 'rotate(-6deg)' }}>that is me \u2192</div>
          <div style={{ width: '300px', height: '420px', borderRadius: '150px 150px 0 0', overflow: 'hidden', flexShrink: 0 }}>
            <img src="/photo.png" alt="Kaavya Indhu" style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center top', display: 'block' }} />
          </div>
        </div>'''

new2 = '''        <div style={{ width: '400px', backgroundColor: '#E0D9CE', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'flex-end', flexShrink: 0, position: 'relative', zIndex: 1 }}>
          <span style={{ position: 'absolute', top: '20px', right: '28px', fontFamily: 'Caveat, cursive', fontSize: '28px', color: '#E8729A', opacity: 0.38 }}>*</span>
          <span style={{ position: 'absolute', top: '58px', left: '20px', fontFamily: 'Caveat, cursive', fontSize: '14px', color: '#E8729A', opacity: 0.25 }}>*</span>
          <span style={{ position: 'absolute', top: '100px', right: '18px', fontFamily: 'Caveat, cursive', fontSize: '18px', color: '#E8729A', opacity: 0.2 }}>o</span>
          <div style={{ width: '340px', height: '420px', borderRadius: '170px 170px 0 0', overflow: 'hidden', flexShrink: 0 }}>
            <img src="/photo.png" alt="Kaavya Indhu" style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center top', display: 'block' }} />
          </div>
        </div>'''

if old2 in content2_read:
    content2_read = content2_read.replace(old2, new2)
    with open("src/pages/Home.jsx", "w") as f:
        f.write(content2_read)
    print("Photo panel widened!")
else:
    print("Photo pattern not found - may need manual check")

