with open("src/pages/Home.jsx", "r") as f:
    content = f.read()

old = '''        <div style={{ width: '300px', backgroundColor: '#E0D9CE', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'flex-end', flexShrink: 0, position: 'relative', zIndex: 1 }}>
          <span style={{ position: 'absolute', top: '20px', right: '28px', fontFamily: 'Caveat, cursive', fontSize: '28px', color: '#E8729A', opacity: 0.38 }}>*</span>
          <span style={{ position: 'absolute', top: '58px', right: '58px', fontFamily: 'Caveat, cursive', fontSize: '14px', color: '#E8729A', opacity: 0.25 }}>*</span>
          <span style={{ position: 'absolute', top: '100px', right: '24px', fontFamily: 'Caveat, cursive', fontSize: '18px', color: '#E8729A', opacity: 0.2 }}>o</span>
          <span style={{ position: 'absolute', bottom: '80px', left: '16px', fontFamily: 'Caveat, cursive', fontSize: '13px', color: '#E8729A', opacity: 0.22 }}>+</span>
          <div style={{ width: '100%', height: '100%', position: 'absolute', top: 0, left: 0, overflow: 'hidden', borderRadius: '14px' }}>
            <img src="/photo.png" alt="Kaavya Indhu" style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center top', display: 'block' }} />
          </div>
        </div>'''

new = '''        <div style={{ width: '240px', flexShrink: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', position: 'relative', zIndex: 1, padding: '28px 16px' }}>
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

if old in content:
    content = content.replace(old, new)
    with open("src/pages/Home.jsx", "w") as f:
        f.write(content)
    print("Hero middle + photo panel updated!")
else:
    print("Pattern not found - checking what's there...")
    idx = content.find("E0D9CE")
    print(repr(content[idx-100:idx+300]))
