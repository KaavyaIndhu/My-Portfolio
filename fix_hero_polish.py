with open("src/pages/Home.jsx", "r") as f:
    content = f.read()

old = '''        {/* LEFT — name only */}
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
        </div>
        <div style={{ width: '400px', backgroundColor: '#E0D9CE', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'flex-end', flexShrink: 0, position: 'relative', zIndex: 1 }}>
          <span style={{ position: 'absolute', top: '20px', right: '28px', fontFamily: 'Caveat, cursive', fontSize: '28px', color: '#E8729A', opacity: 0.38 }}>*</span>
          <span style={{ position: 'absolute', top: '58px', left: '20px', fontFamily: 'Caveat, cursive', fontSize: '14px', color: '#E8729A', opacity: 0.25 }}>*</span>
          <span style={{ position: 'absolute', top: '100px', right: '18px', fontFamily: 'Caveat, cursive', fontSize: '18px', color: '#E8729A', opacity: 0.2 }}>o</span>
          <div style={{ width: '340px', height: '420px', borderRadius: '170px 170px 0 0', overflow: 'hidden', flexShrink: 0 }}>
            <img src="/photo.png" alt="Kaavya Indhu" style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center top', display: 'block' }} />
          </div>
        </div>'''

new = '''        {/* LEFT — name only */}
        <div style={{ width: '360px', flexShrink: 0, padding: '52px 40px', display: 'flex', flexDirection: 'column', justifyContent: 'flex-start', position: 'relative', zIndex: 1 }}>
          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', padding: '6px 16px', borderRadius: '30px', border: '1px solid #E8729A', fontFamily: 'Caveat, cursive', fontSize: '17px', color: '#E8729A', width: 'fit-content', marginBottom: '14px' }}>
            <span style={{ width: '7px', height: '7px', borderRadius: '50%', background: '#E8729A', display: 'inline-block' }}></span>
            available for projects
          </div>
          <div style={{ fontFamily: 'Caveat, cursive', fontSize: '20px', color: '#9a9285', marginBottom: '8px' }}>Hi, since you are new here</div>
          <div style={{ fontFamily: 'DM Serif Display, serif', fontSize: '110px', color: '#E8729A', lineHeight: '0.88' }}>Kaavya<br />Indhu</div>
        </div>

        {/* CENTER — all details */}
        <div style={{ flex: 1, padding: '52px 44px 52px 52px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', position: 'relative', zIndex: 1 }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
              <div style={{ fontSize: '13px', color: '#7a7065', letterSpacing: '0.14em', textTransform: 'uppercase', fontWeight: 500 }}>Full Stack Developer</div>
              <div style={{ width: '28px', height: '1px', background: '#E8729A', opacity: 0.4 }}></div>
              <div style={{ fontSize: '13px', color: '#7a7065', letterSpacing: '0.14em', textTransform: 'uppercase', fontWeight: 500 }}>Tech . Marketing . HR . RnD</div>
            </div>
            <div style={{ fontFamily: 'Caveat, cursive', fontSize: '32px', color: '#8a8075' }}>Bridging technology, people, and ideas.</div>
            <div style={{ fontSize: '18px', color: '#7a7065', lineHeight: 2, maxWidth: '420px', borderLeft: '2px solid #E8729A', paddingLeft: '20px' }}>I am a full stack developer who loves building things at the intersection of design and technology. I care deeply about creating experiences that feel good to use. Always learning, always building.</div>
            <div style={{ fontFamily: 'Caveat, cursive', fontSize: '20px', color: '#9a9285', display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ width: '7px', height: '7px', borderRadius: '50%', background: '#E8729A', display: 'inline-block', opacity: 0.6 }}></span>
              Based in India
            </div>
          </div>

          {/* bottom doodle */}
          <div style={{ opacity: 0.2, marginTop: '28px' }}>
            <svg width="220" height="60" viewBox="0 0 220 60" fill="none">
              <polyline points="10,45 35,22 58,36 88,12 115,26 148,8 178,20 210,12" stroke="#E8729A" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <circle cx="88" cy="12" r="4" fill="#E8729A"/>
              <circle cx="148" cy="8" r="4" fill="#E8729A"/>
              <line x1="10" y1="54" x2="210" y2="54" stroke="#E8729A" strokeWidth="1" strokeLinecap="round"/>
            </svg>
          </div>
        </div>

        {/* RIGHT — photo panel */}
        <div style={{ width: '420px', backgroundColor: '#E0D9CE', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'flex-end', flexShrink: 0, position: 'relative', zIndex: 1 }}>
          
          {/* pink doodles around photo */}
          <span style={{ position: 'absolute', top: '18px', right: '32px', fontFamily: 'Caveat, cursive', fontSize: '32px', color: '#E8729A', opacity: 0.35 }}>✦</span>
          <span style={{ position: 'absolute', top: '62px', left: '18px', fontFamily: 'Caveat, cursive', fontSize: '16px', color: '#E8729A', opacity: 0.28 }}>✦</span>
          <span style={{ position: 'absolute', top: '110px', right: '16px', fontFamily: 'Caveat, cursive', fontSize: '20px', color: '#E8729A', opacity: 0.2 }}>*</span>
          <span style={{ position: 'absolute', bottom: '120px', left: '14px', fontFamily: 'Caveat, cursive', fontSize: '14px', color: '#E8729A', opacity: 0.22 }}>*</span>

          {/* curved squiggle top left */}
          <svg style={{ position: 'absolute', top: '30px', left: '10px', opacity: 0.2 }} width="60" height="30" viewBox="0 0 60 30" fill="none">
            <path d="M0 20 Q15 0 30 15 Q45 30 60 10" stroke="#E8729A" strokeWidth="1.8" strokeLinecap="round" fill="none"/>
          </svg>

          {/* small hearts */}
          <svg style={{ position: 'absolute', bottom: '140px', right: '12px', opacity: 0.25 }} width="22" height="20" viewBox="0 0 22 20" fill="#E8729A">
            <path d="M11 18 C11 18 1 11 1 5.5 C1 2.5 3.5 1 6 1 C8 1 10 2.5 11 4 C12 2.5 14 1 16 1 C18.5 1 21 2.5 21 5.5 C21 11 11 18 11 18Z"/>
          </svg>
          <svg style={{ position: 'absolute', top: '80px', left: '26px', opacity: 0.18 }} width="16" height="14" viewBox="0 0 22 20" fill="#E8729A">
            <path d="M11 18 C11 18 1 11 1 5.5 C1 2.5 3.5 1 6 1 C8 1 10 2.5 11 4 C12 2.5 14 1 16 1 C18.5 1 21 2.5 21 5.5 C21 11 11 18 11 18Z"/>
          </svg>

          {/* circle outline doodle */}
          <svg style={{ position: 'absolute', top: '140px', right: '10px', opacity: 0.15 }} width="36" height="36" viewBox="0 0 36 36" fill="none">
            <circle cx="18" cy="18" r="14" stroke="#E8729A" strokeWidth="1.5" strokeDasharray="4 4"/>
          </svg>

          <div style={{ width: '360px', height: '430px', borderRadius: '180px 180px 0 0', overflow: 'hidden', flexShrink: 0 }}>
            <img src="/photo.png" alt="Kaavya Indhu" style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center top', display: 'block' }} />
          </div>
        </div>'''

if old in content:
    content = content.replace(old, new)
    with open("src/pages/Home.jsx", "w") as f:
        f.write(content)
    print("All done!")
else:
    print("Pattern not found")
    idx = content.find("LEFT — name only")
    print(repr(content[idx-20:idx+100]))
