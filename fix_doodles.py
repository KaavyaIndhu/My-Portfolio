with open("src/pages/Home.jsx", "r") as f:
    content = f.read()

old = '''        {/* center watermark — portfolio */}
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

new = '''        {/* center watermark — portfolio */}
        <div style={{ position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', fontFamily: 'DM Serif Display, serif', fontSize: '130px', color: '#E8729A', opacity: 0.05, lineHeight: 1, userSelect: 'none', pointerEvents: 'none', whiteSpace: 'nowrap', letterSpacing: '0.08em' }}>portfolio</div>

        {/* full doodle layer */}
        <svg style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', pointerEvents: 'none', zIndex: 0 }} viewBox="0 0 1200 460" fill="none" preserveAspectRatio="xMidYMid meet">

          {/* TOP LEFT — arrow cluster */}
          <path d="M30 38 Q75 14 118 40" stroke="#E8729A" strokeWidth="2" strokeLinecap="round" opacity="0.22"/>
          <polyline points="104,30 118,40 105,50" stroke="#E8729A" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" opacity="0.22"/>
          <path d="M48 66 Q95 42 138 66" stroke="#E8729A" strokeWidth="1.6" strokeLinecap="round" opacity="0.16"/>
          <polyline points="124,56 138,66 125,76" stroke="#E8729A" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" opacity="0.16"/>
          <path d="M62 90 Q108 70 148 90" stroke="#E8729A" strokeWidth="1.3" strokeLinecap="round" opacity="0.11"/>
          <polyline points="136,82 148,90 136,100" stroke="#E8729A" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round" opacity="0.11"/>

          {/* TOP CENTER — squiggles */}
          <path d="M430 16 Q460 4 490 16 Q520 28 550 16 Q580 4 610 16 Q640 28 670 16 Q700 4 730 16" stroke="#E8729A" strokeWidth="1.8" strokeLinecap="round" fill="none" opacity="0.18"/>
          <path d="M450 36 Q480 22 510 36 Q540 50 570 36 Q600 22 630 36 Q660 50 690 36 Q720 22 750 36" stroke="#E8729A" strokeWidth="1.4" strokeLinecap="round" fill="none" opacity="0.13"/>
          <path d="M470 54 Q500 40 530 54 Q560 68 590 54 Q620 40 650 54 Q680 68 710 54" stroke="#E8729A" strokeWidth="1.1" strokeLinecap="round" fill="none" opacity="0.09"/>

          {/* TOP RIGHT — arrow cluster */}
          <path d="M1170 38 Q1125 14 1082 40" stroke="#E8729A" strokeWidth="2" strokeLinecap="round" opacity="0.22"/>
          <polyline points="1096,30 1082,40 1095,50" stroke="#E8729A" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" opacity="0.22"/>
          <path d="M1152 66 Q1105 42 1062 66" stroke="#E8729A" strokeWidth="1.6" strokeLinecap="round" opacity="0.16"/>
          <polyline points="1076,56 1062,66 1075,76" stroke="#E8729A" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" opacity="0.16"/>
          <path d="M1138 90 Q1092 70 1052 90" stroke="#E8729A" strokeWidth="1.3" strokeLinecap="round" opacity="0.11"/>
          <polyline points="1064,82 1052,90 1064,100" stroke="#E8729A" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round" opacity="0.11"/>

          {/* STARS scattered across top */}
          <text x="200" y="30" fontFamily="Caveat,cursive" fontSize="22" fill="#E8729A" opacity="0.2">✦</text>
          <text x="280" y="52" fontFamily="Caveat,cursive" fontSize="13" fill="#E8729A" opacity="0.16">*</text>
          <text x="355" y="24" fontFamily="Caveat,cursive" fontSize="16" fill="#E8729A" opacity="0.14">✦</text>
          <text x="395" y="48" fontFamily="Caveat,cursive" fontSize="11" fill="#E8729A" opacity="0.12">*</text>
          <text x="760" y="22" fontFamily="Caveat,cursive" fontSize="18" fill="#E8729A" opacity="0.16">✦</text>
          <text x="800" y="46" fontFamily="Caveat,cursive" fontSize="11" fill="#E8729A" opacity="0.12">*</text>
          <text x="860" y="28" fontFamily="Caveat,cursive" fontSize="13" fill="#E8729A" opacity="0.14">✦</text>
          <text x="940" y="50" fontFamily="Caveat,cursive" fontSize="11" fill="#E8729A" opacity="0.11">*</text>
          <text x="1000" y="24" fontFamily="Caveat,cursive" fontSize="16" fill="#E8729A" opacity="0.14">✦</text>

          {/* SMALL CIRCLES dotted top */}
          <circle cx="240" cy="18" r="3" fill="#E8729A" opacity="0.15"/>
          <circle cx="320" cy="40" r="2" fill="#E8729A" opacity="0.12"/>
          <circle cx="410" cy="18" r="2.5" fill="#E8729A" opacity="0.13"/>
          <circle cx="740" cy="44" r="2" fill="#E8729A" opacity="0.11"/>
          <circle cx="830" cy="16" r="3" fill="#E8729A" opacity="0.13"/>
          <circle cx="910" cy="38" r="2" fill="#E8729A" opacity="0.11"/>
          <circle cx="1040" cy="18" r="2.5" fill="#E8729A" opacity="0.13"/>

          {/* CURVED ARROWS from sides toward center mid-height */}
          <path d="M220 200 Q300 160 380 190" stroke="#E8729A" strokeWidth="1.6" strokeLinecap="round" opacity="0.14"/>
          <polyline points="367,180 380,190 368,200" stroke="#E8729A" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" opacity="0.14"/>

          <path d="M980 200 Q900 160 820 190" stroke="#E8729A" strokeWidth="1.6" strokeLinecap="round" opacity="0.14"/>
          <polyline points="833,180 820,190 832,200" stroke="#E8729A" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" opacity="0.14"/>

          {/* BOTTOM scattered doodles */}
          <text x="160" y="420" fontFamily="Caveat,cursive" fontSize="18" fill="#E8729A" opacity="0.14">✦</text>
          <text x="240" y="440" fontFamily="Caveat,cursive" fontSize="11" fill="#E8729A" opacity="0.1">*</text>
          <circle cx="200" cy="400" r="2.5" fill="#E8729A" opacity="0.12"/>

          {/* small hand-drawn circle outline near center-right */}
          <circle cx="820" cy="240" r="18" stroke="#E8729A" strokeWidth="1.4" strokeDasharray="4 4" opacity="0.13"/>
          <circle cx="820" cy="240" r="4" fill="#E8729A" opacity="0.1"/>

          {/* tiny cross / plus signs */}
          <line x1="178" y1="140" x2="178" y2="154" stroke="#E8729A" strokeWidth="1.5" strokeLinecap="round" opacity="0.18"/>
          <line x1="171" y1="147" x2="185" y2="147" stroke="#E8729A" strokeWidth="1.5" strokeLinecap="round" opacity="0.18"/>
          <line x1="1022" y1="140" x2="1022" y2="154" stroke="#E8729A" strokeWidth="1.5" strokeLinecap="round" opacity="0.16"/>
          <line x1="1015" y1="147" x2="1029" y2="147" stroke="#E8729A" strokeWidth="1.5" strokeLinecap="round" opacity="0.16"/>
          <line x1="590" y1="80" x2="590" y2="92" stroke="#E8729A" strokeWidth="1.4" strokeLinecap="round" opacity="0.14"/>
          <line x1="584" y1="86" x2="596" y2="86" stroke="#E8729A" strokeWidth="1.4" strokeLinecap="round" opacity="0.14"/>

        </svg>'''

if old in content:
    content = content.replace(old, new)
    with open("src/pages/Home.jsx", "w") as f:
        f.write(content)
    print("Doodles updated — much more visible now!")
else:
    print("Pattern not found")
    idx = content.find("center watermark")
    print(repr(content[idx-20:idx+100]))
