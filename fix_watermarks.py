with open("src/pages/Home.jsx", "r") as f:
    content = f.read()

old = '''      <div style={{ backgroundColor: '#F5F0E8', borderRadius: '14px', display: 'flex', overflow: 'hidden', minHeight: '460px', position: 'relative' }}>
        <div style={{ position: 'absolute', bottom: '-30px', left: '-10px', fontFamily: 'DM Serif Display, serif', fontSize: '200px', color: '#E8729A', opacity: 0.055, lineHeight: 1, userSelect: 'none', pointerEvents: 'none', whiteSpace: 'nowrap' }}>KaavyaIndhu</div>'''

new = '''      <div style={{ backgroundColor: '#F5F0E8', borderRadius: '14px', display: 'flex', overflow: 'hidden', minHeight: '460px', position: 'relative' }}>

        {/* bottom watermark — KaavyaIndhu */}
        <div style={{ position: 'absolute', bottom: '-30px', left: '-10px', fontFamily: 'DM Serif Display, serif', fontSize: '200px', color: '#E8729A', opacity: 0.055, lineHeight: 1, userSelect: 'none', pointerEvents: 'none', whiteSpace: 'nowrap' }}>KaavyaIndhu</div>

        {/* center watermark — portfolio */}
        <div style={{ position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', fontFamily: 'DM Serif Display, serif', fontSize: '130px', color: '#E8729A', opacity: 0.04, lineHeight: 1, userSelect: 'none', pointerEvents: 'none', whiteSpace: 'nowrap', letterSpacing: '0.08em' }}>portfolio</div>

        {/* top doodles layer */}
        <svg style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', pointerEvents: 'none', zIndex: 0 }} viewBox="0 0 1200 460" fill="none" preserveAspectRatio="xMidYMid meet">
          {/* top left arrow cluster */}
          <path d="M40 40 Q80 20 120 45" stroke="#E8729A" strokeWidth="1.4" strokeLinecap="round" opacity="0.14"/>
          <polyline points="108,36 120,45 109,54" stroke="#E8729A" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round" opacity="0.14"/>
          <path d="M55 70 Q100 50 140 72" stroke="#E8729A" strokeWidth="1.2" strokeLinecap="round" opacity="0.1"/>
          <polyline points="128,63 140,72 129,81" stroke="#E8729A" strokeWidth="1.2" strokeLinecap="round" strokeLinejoin="round" opacity="0.1"/>

          {/* top center squiggles */}
          <path d="M480 18 Q510 8 540 18 Q570 28 600 18 Q630 8 660 18" stroke="#E8729A" strokeWidth="1.3" strokeLinecap="round" fill="none" opacity="0.1"/>
          <path d="M500 36 Q530 24 560 36 Q590 48 620 36 Q650 24 680 36" stroke="#E8729A" strokeWidth="1.1" strokeLinecap="round" fill="none" opacity="0.08"/>

          {/* top right arrow */}
          <path d="M980 30 Q1040 12 1100 35" stroke="#E8729A" strokeWidth="1.4" strokeLinecap="round" opacity="0.13"/>
          <polyline points="1088,26 1100,35 1089,44" stroke="#E8729A" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round" opacity="0.13"/>
          <path d="M1000 55 Q1055 38 1110 58" stroke="#E8729A" strokeWidth="1.2" strokeLinecap="round" opacity="0.09"/>

          {/* scattered small stars top */}
          <text x="320" y="32" fontFamily="Caveat,cursive" fontSize="20" fill="#E8729A" opacity="0.12">✦</text>
          <text x="760" y="28" fontFamily="Caveat,cursive" fontSize="14" fill="#E8729A" opacity="0.1">✦</text>
          <text x="870" y="42" fontFamily="Caveat,cursive" fontSize="10" fill="#E8729A" opacity="0.1">*</text>
          <text x="180" y="28" fontFamily="Caveat,cursive" fontSize="12" fill="#E8729A" opacity="0.1">*</text>
          <text x="440" y="44" fontFamily="Caveat,cursive" fontSize="10" fill="#E8729A" opacity="0.09">*</text>
          <text x="1140" y="30" fontFamily="Caveat,cursive" fontSize="16" fill="#E8729A" opacity="0.1">✦</text>

          {/* curved arrow pointing toward center from left */}
          <path d="M260 80 Q340 30 420 60" stroke="#E8729A" strokeWidth="1.3" strokeLinecap="round" opacity="0.1"/>
          <polyline points="408,50 420,60 408,70" stroke="#E8729A" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round" opacity="0.1"/>

          {/* curved arrow pointing toward center from right */}
          <path d="M940 80 Q860 30 780 60" stroke="#E8729A" strokeWidth="1.3" strokeLinecap="round" opacity="0.1"/>
          <polyline points="792,50 780,60 792,70" stroke="#E8729A" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round" opacity="0.1"/>

          {/* small circles scattered */}
          <circle cx="370" cy="22" r="2.5" fill="#E8729A" opacity="0.1"/>
          <circle cx="820" cy="18" r="2" fill="#E8729A" opacity="0.09"/>
          <circle cx="700" cy="48" r="2" fill="#E8729A" opacity="0.08"/>
        </svg>'''

if old in content:
    content = content.replace(old, new)
    with open("src/pages/Home.jsx", "w") as f:
        f.write(content)
    print("Watermarks and doodles added!")
else:
    print("Pattern not found")
    idx = content.find("F5F0E8', borderRadius: '14px', display: 'flex'")
    print(repr(content[idx-20:idx+120]))
