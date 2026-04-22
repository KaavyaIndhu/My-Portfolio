import React from 'react'
import { useNavigate } from 'react-router-dom'

const connectLinks = [
  { label: 'LinkedIn', url: 'https://www.linkedin.com/in/kaavyaindhu' },
  { label: 'GitHub', url: 'https://github.com/KaavyaIndhu' },
  { label: 'Resume', url: 'https://drive.google.com/uc?export=download&id=1-YJ68EkPAiWkS1jSFd_5jh7EgYcfAHsO', download: false },
  { label: 'Instagram', url: 'https://www.instagram.com/itsme_kaavya._/' },
]

function ConnectLink({ item }) {
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
}

function MessageButton() {
  const [hovered, setHovered] = React.useState(false)
  return (
    <a href="mailto:kaavyaindhu06@gmail.com"
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      style={{ marginTop: '20px', padding: '11px 24px', borderRadius: '40px', backgroundColor: '#E8729A', color: '#fff', fontSize: '12px', fontWeight: 500, textDecoration: 'none', width: 'fit-content', display: 'inline-block', transition: 'transform 0.18s ease, box-shadow 0.18s ease', transform: hovered ? 'translateY(-4px)' : 'translateY(0)', boxShadow: hovered ? '0 8px 20px rgba(232,114,154,0.4)' : 'none' }}>
      Send me a message
    </a>
  )
}

function NavCard({ num, title, sub, illustration, squiggle, doodle, onClick }) {
  const [hovered, setHovered] = React.useState(false)
  return (
    <div onClick={onClick} onMouseEnter={() => setHovered(true)} onMouseLeave={() => setHovered(false)}
      style={{ background: '#F5F0E8', borderRadius: '20px', height: '300px', display: 'flex', flexDirection: 'column', justifyContent: 'flex-end', padding: '32px', position: 'relative', overflow: 'hidden', cursor: 'pointer', transition: 'transform 0.18s ease, box-shadow 0.18s ease', transform: hovered ? 'translateY(-5px) scale(1.015)' : 'none', boxShadow: hovered ? '0 12px 32px rgba(0,0,0,0.10)' : 'none' }}>
      <div style={{ position: 'absolute', top: '24px', left: '28px', fontFamily: 'DM Serif Display, serif', fontSize: '13px', color: '#E8729A', opacity: 0.4, letterSpacing: '0.1em' }}>{num}</div>
      <div style={{ position: 'absolute', top: '20px', right: '28px', fontFamily: 'Caveat, cursive', fontSize: '22px', color: '#E8729A', opacity: 0.35 }}>{doodle}</div>
      <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', pointerEvents: 'none' }}>{illustration}</div>
      {squiggle && <svg style={{ position: 'absolute', bottom: '78px', left: '32px' }} width="60" height="8" viewBox="0 0 60 8" fill="none"><path d="M0 4 Q7.5 0 15 4 Q22.5 8 30 4 Q37.5 0 45 4 Q52.5 8 60 4" stroke="#E8729A" strokeWidth="1.5" fill="none" opacity="0.28"/></svg>}
      <div style={{ fontFamily: 'DM Serif Display, serif', fontSize: '58px', color: '#E8729A', lineHeight: 0.95, position: 'relative', zIndex: 1 }}>{title}</div>
      <div style={{ fontFamily: 'Caveat, cursive', fontSize: '20px', color: '#c4a0b0', marginTop: '6px', position: 'relative', zIndex: 1 }}>{sub}</div>
    </div>
  )
}

const SkillsIllustration = () => (
  <svg width="340" height="240" viewBox="0 0 260 180" fill="none">
    <path d="M90 55 L65 90 L90 125" stroke="#E8729A" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" opacity="0.18"/>
    <path d="M170 55 L195 90 L170 125" stroke="#E8729A" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" opacity="0.18"/>
    <path d="M148 50 L112 130" stroke="#E8729A" strokeWidth="2.5" strokeLinecap="round" opacity="0.18"/>
    <rect x="5" y="10" width="52" height="20" rx="10" fill="#E8729A" opacity="0.09"/>
    <text x="31" y="24" fontFamily="Inter,sans-serif" fontSize="9" fill="#E8729A" textAnchor="middle" fontWeight="500" opacity="0.6">Python</text>
    <rect x="198" y="8" width="50" height="20" rx="10" fill="#E8729A" opacity="0.09"/>
    <text x="223" y="22" fontFamily="Inter,sans-serif" fontSize="9" fill="#E8729A" textAnchor="middle" fontWeight="500" opacity="0.6">React</text>
    <rect x="200" y="150" width="50" height="20" rx="10" fill="#E8729A" opacity="0.09"/>
    <text x="225" y="164" fontFamily="Inter,sans-serif" fontSize="9" fill="#E8729A" textAnchor="middle" fontWeight="500" opacity="0.6">SQL</text>
    <rect x="5" y="148" width="55" height="20" rx="10" fill="#E8729A" opacity="0.09"/>
    <text x="32" y="162" fontFamily="Inter,sans-serif" fontSize="9" fill="#E8729A" textAnchor="middle" fontWeight="500" opacity="0.6">Node.js</text>
    <rect x="88" y="155" width="72" height="20" rx="10" fill="#E8729A" opacity="0.09"/>
    <text x="124" y="169" fontFamily="Inter,sans-serif" fontSize="9" fill="#E8729A" textAnchor="middle" fontWeight="500" opacity="0.6">JavaScript</text>
  </svg>
)

const ProjectsIllustration = () => (
  <svg width="340" height="240" viewBox="0 0 260 180" fill="none">
    <rect x="20" y="25" width="160" height="118" rx="10" stroke="#E8729A" strokeWidth="2" fill="#E8729A" fillOpacity="0.04" opacity="0.4"/>
    <rect x="20" y="25" width="160" height="28" rx="10" fill="#E8729A" fillOpacity="0.08" opacity="0.55"/>
    <circle cx="38" cy="39" r="4" fill="#E8729A" opacity="0.22"/>
    <circle cx="54" cy="39" r="4" fill="#E8729A" opacity="0.22"/>
    <circle cx="70" cy="39" r="4" fill="#E8729A" opacity="0.22"/>
    <rect x="32" y="67" width="80" height="6" rx="3" fill="#E8729A" opacity="0.1"/>
    <rect x="32" y="79" width="60" height="6" rx="3" fill="#E8729A" opacity="0.08"/>
    <rect x="32" y="91" width="95" height="6" rx="3" fill="#E8729A" opacity="0.08"/>
    <path d="M200 165 L220 105 L240 165" stroke="#E8729A" strokeWidth="2" strokeLinejoin="round" fill="#E8729A" fillOpacity="0.06" opacity="0.4"/>
    <ellipse cx="220" cy="104" rx="10" ry="14" fill="#E8729A" fillOpacity="0.1" stroke="#E8729A" strokeWidth="1.8" opacity="0.4"/>
    <circle cx="220" cy="108" r="4" fill="#E8729A" opacity="0.2"/>
    <circle cx="190" cy="45" r="2.5" fill="#E8729A" opacity="0.2"/>
    <circle cx="245" cy="65" r="2" fill="#E8729A" opacity="0.16"/>
  </svg>
)

const BlogIllustration = () => (
  <svg width="340" height="240" viewBox="0 0 260 180" fill="none">
    <rect x="55" y="12" width="110" height="145" rx="8" stroke="#E8729A" strokeWidth="2" fill="#E8729A" fillOpacity="0.04" opacity="0.4"/>
    <rect x="55" y="12" width="16" height="145" rx="5" fill="#E8729A" fillOpacity="0.09" opacity="0.55"/>
    <line x1="82" y1="40" x2="155" y2="40" stroke="#E8729A" strokeWidth="1.5" opacity="0.14"/>
    <line x1="82" y1="57" x2="155" y2="57" stroke="#E8729A" strokeWidth="1.5" opacity="0.12"/>
    <line x1="82" y1="74" x2="155" y2="74" stroke="#E8729A" strokeWidth="1.5" opacity="0.12"/>
    <line x1="82" y1="91" x2="140" y2="91" stroke="#E8729A" strokeWidth="1.5" opacity="0.12"/>
    <line x1="82" y1="108" x2="148" y2="108" stroke="#E8729A" strokeWidth="1.5" opacity="0.1"/>
    <path d="M114 130 C114 126 109 122 105 126 C101 122 96 126 96 130 C96 135 105 142 105 142 C105 142 114 135 114 130Z" fill="#E8729A" opacity="0.15"/>
    <rect x="130" y="8" width="8" height="55" rx="4" transform="rotate(25 130 8)" fill="#E8729A" fillOpacity="0.12" stroke="#E8729A" strokeWidth="1.2" opacity="0.32"/>
    <text x="180" y="25" fontFamily="sans-serif" fontSize="16" fill="#E8729A" opacity="0.18">&#10022;</text>
    <text x="195" y="125" fontFamily="Caveat,cursive" fontSize="13" fill="#E8729A" opacity="0.18">story...</text>
    <text x="20" y="100" fontFamily="Caveat,cursive" fontSize="11" fill="#E8729A" opacity="0.15">&#10022;</text>
  </svg>
)

const ExperienceIllustration = () => (
  <svg width="340" height="240" viewBox="0 0 280 180" fill="none">
    <line x1="40" y1="130" x2="240" y2="130" stroke="#E8729A" strokeWidth="1.5" strokeLinecap="round" opacity="0.2"/>
    <rect x="80" y="95" width="120" height="35" rx="4" stroke="#E8729A" strokeWidth="1.5" fill="#E8729A" fillOpacity="0.05" opacity="0.4"/>
    <line x1="80" y1="108" x2="200" y2="108" stroke="#E8729A" strokeWidth="1" opacity="0.15"/>
    <line x1="80" y1="118" x2="180" y2="118" stroke="#E8729A" strokeWidth="1" opacity="0.12"/>
    <rect x="115" y="115" width="50" height="15" rx="3" stroke="#E8729A" strokeWidth="1.2" fill="#E8729A" fillOpacity="0.06" opacity="0.35"/>
    <circle cx="140" cy="55" r="14" stroke="#E8729A" strokeWidth="1.8" fill="#E8729A" fillOpacity="0.08" opacity="0.45"/>
    <path d="M120 95 Q120 75 140 75 Q160 75 160 95" stroke="#E8729A" strokeWidth="1.8" fill="#E8729A" fillOpacity="0.06" opacity="0.45"/>
    <path d="M122 90 L108 100" stroke="#E8729A" strokeWidth="1.8" strokeLinecap="round" opacity="0.4"/>
    <path d="M108 100 L95 92" stroke="#E8729A" strokeWidth="1.8" strokeLinecap="round" opacity="0.4"/>
    <path d="M158 90 L172 100" stroke="#E8729A" strokeWidth="1.8" strokeLinecap="round" opacity="0.4"/>
    <path d="M172 100 L182 95" stroke="#E8729A" strokeWidth="1.8" strokeLinecap="round" opacity="0.4"/>
    <path d="M125 95 L115 130" stroke="#E8729A" strokeWidth="1.8" strokeLinecap="round" opacity="0.4"/>
    <path d="M155 95 L165 130" stroke="#E8729A" strokeWidth="1.8" strokeLinecap="round" opacity="0.4"/>
    <rect x="30" y="100" width="38" height="48" rx="4" stroke="#E8729A" strokeWidth="1.2" fill="#E8729A" fillOpacity="0.05" opacity="0.35" transform="rotate(-12 30 100)"/>
    <line x1="33" y1="112" x2="58" y2="108" stroke="#E8729A" strokeWidth="1" opacity="0.12"/>
    <line x1="34" y1="120" x2="59" y2="116" stroke="#E8729A" strokeWidth="1" opacity="0.1"/>
    <line x1="35" y1="128" x2="55" y2="124" stroke="#E8729A" strokeWidth="1" opacity="0.1"/>
    <rect x="210" y="85" width="38" height="48" rx="4" stroke="#E8729A" strokeWidth="1.2" fill="#E8729A" fillOpacity="0.05" opacity="0.35" transform="rotate(10 210 85)"/>
    <line x1="214" y1="97" x2="240" y2="99" stroke="#E8729A" strokeWidth="1" opacity="0.12"/>
    <line x1="214" y1="106" x2="240" y2="108" stroke="#E8729A" strokeWidth="1" opacity="0.1"/>
    <line x1="215" y1="115" x2="238" y2="117" stroke="#E8729A" strokeWidth="1" opacity="0.1"/>
    <path d="M178 95 Q185 88 182 80" stroke="#E8729A" strokeWidth="1.2" fill="none" opacity="0.2" strokeDasharray="2 2"/>
    <circle cx="182" cy="78" r="2" fill="#E8729A" opacity="0.2"/>
    <text x="188" y="74" fontFamily="Caveat,cursive" fontSize="11" fill="#E8729A" opacity="0.22">idea!</text>
    <text x="42" y="160" fontFamily="Caveat,cursive" fontSize="11" fill="#E8729A" opacity="0.18">✦</text>
    <text x="220" y="155" fontFamily="Caveat,cursive" fontSize="13" fill="#E8729A" opacity="0.16">⟡</text>
  </svg>
)

export default function Home() {
  const navigate = useNavigate()
  return (
    <div style={{ backgroundColor: '#C8BFB0', minHeight: '100vh', padding: '14px', display: 'flex', flexDirection: 'column', gap: '10px' }}>

      <div className='hero-outer' style={{ backgroundColor: '#F5F0E8', borderRadius: '14px', display: 'flex', overflow: 'hidden', minHeight: '460px', position: 'relative' }}>

        {/* bottom watermark — KaavyaIndhu */}
        <div style={{ position: 'absolute', bottom: '-30px', left: '-10px', fontFamily: 'DM Serif Display, serif', fontSize: '200px', color: '#E8729A', opacity: 0.055, lineHeight: 1, userSelect: 'none', pointerEvents: 'none', whiteSpace: 'nowrap' }}>KaavyaIndhu</div>

        {/* center watermark — portfolio */}
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

        </svg>

        {/* LEFT — name only */}
        <div className='hero-left' style={{ width: '360px', flexShrink: 0, padding: '52px 40px', display: 'flex', flexDirection: 'column', justifyContent: 'flex-start', position: 'relative', zIndex: 1 }}>
          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', padding: '6px 16px', borderRadius: '30px', border: '1px solid #E8729A', fontFamily: 'Caveat, cursive', fontSize: '17px', color: '#E8729A', width: 'fit-content', marginBottom: '14px' }}>
            <span style={{ width: '7px', height: '7px', borderRadius: '50%', background: '#E8729A', display: 'inline-block' }}></span>
            available for projects
          </div>
          <div style={{ fontFamily: 'Caveat, cursive', fontSize: '20px', color: '#9a9285', marginBottom: '8px' }}>Hi, since you are new here</div>
          <div className='hero-name' style={{ fontFamily: 'DM Serif Display, serif', fontSize: '110px', color: '#E8729A', lineHeight: '0.88' }}>Kaavya<br />Indhu</div>
        </div>

        {/* CENTER — all details */}
        <div className='hero-center' style={{ flex: 1, padding: '52px 44px 52px 52px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', position: 'relative', zIndex: 1 }}>
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
        <div className='hero-photo-panel' style={{ width: '420px', backgroundColor: '#E0D9CE', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'flex-end', flexShrink: 0, position: 'relative', zIndex: 1 }}>
          
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

          <div className='photo-arch' style={{ width: '360px', height: '430px', borderRadius: '180px 180px 0 0', overflow: 'hidden', flexShrink: 0 }}>
            <img src="/photo.png" alt="Kaavya Indhu" style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center top', display: 'block' }} />
          </div>
        </div>
      </div>

      <div className='nav-grid' style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
        <NavCard num="01" title="My Skills" sub="What I bring to the table" doodle="o" illustration={<SkillsIllustration />} squiggle onClick={() => navigate('/skills')} />
        <NavCard num="02" title="My Projects" sub="Things I have built" doodle="+" illustration={<ProjectsIllustration />} onClick={() => navigate('/projects')} />
      </div>

      <div className='nav-grid' style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
        <NavCard num="03" title="My Blog" sub="Thoughts and writing" doodle="~ life stories ~" illustration={<BlogIllustration />} squiggle onClick={() => navigate('/blog')} />
        <NavCard num="04" title="My Experience" sub="Where I have been" doodle="~ work ~" illustration={<ExperienceIllustration />} onClick={() => navigate('/experience')} />
      </div>

      <div className='connect-section' style={{ backgroundColor: '#F5F0E8', borderRadius: '14px', padding: '52px 48px', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '32px', minHeight: '280px', position: 'relative', overflow: 'hidden' }}>
        <div style={{ position: 'absolute', bottom: '-20px', right: '-10px', fontFamily: 'DM Serif Display, serif', fontSize: '160px', color: '#E8729A', opacity: 0.04, lineHeight: 1, userSelect: 'none', whiteSpace: 'nowrap' }}>connect</div>
        <div style={{ position: 'relative', zIndex: 1, display: 'flex', flexDirection: 'column' }}>
          <div style={{ fontFamily: 'DM Serif Display, serif', fontSize: '52px', color: '#3a3430', lineHeight: 1, marginBottom: '6px' }}>Connect<br />with me</div>
          <div style={{ fontFamily: 'Caveat, cursive', fontSize: '20px', color: '#9a9285', marginBottom: '20px' }}>let us build something together</div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {connectLinks.map((item) => (<ConnectLink key={item.label} item={item} />))}
          </div>
          <div style={{ fontFamily: 'Caveat, cursive', fontSize: '17px', color: '#9a9285', marginTop: '16px' }}>Based in India - Open to remote work</div>
        </div>
        <div style={{ backgroundColor: '#EDE7DC', borderRadius: '14px', padding: '32px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', position: 'relative', overflow: 'hidden', zIndex: 1 }}>
          <div style={{ position: 'absolute', bottom: '-10px', right: '-8px', fontFamily: 'Caveat, cursive', fontSize: '90px', color: '#E8729A', opacity: 0.07, userSelect: 'none' }}>hi!</div>
          <div>
            <div style={{ fontFamily: 'DM Serif Display, serif', fontSize: '30px', color: '#3a3430' }}>Lets work together</div>
            <div style={{ fontSize: '15px', color: '#7a7065', lineHeight: 1.7, marginTop: '8px' }}>Have a project in mind, a question, or just want to say hi? I would love to hear from you.</div>
            <div style={{ fontFamily: 'Caveat, cursive', fontSize: '22px', color: '#E8729A', marginTop: '14px' }}>kaavyaindhu06@gmail.com</div>
            <div style={{ fontFamily: 'Caveat, cursive', fontSize: '17px', color: '#E8729A', opacity: 0.5, marginTop: '2px' }}>shoot me a mail!</div>
          </div>
          <MessageButton />
        </div>
      </div>

    </div>
  )
}
