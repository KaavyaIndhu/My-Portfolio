f = open("src/pages/Home.jsx", "w")
f.write("""import React from 'react'
import { useNavigate } from 'react-router-dom'

const connectLinks = [
  { label: 'LinkedIn', url: 'https://linkedin.com' },
  { label: 'GitHub', url: 'https://github.com' },
  { label: 'Resume', url: '#' },
  { label: 'Instagram', url: 'https://instagram.com' },
]

function ConnectLink({ item }) {
  const [hovered, setHovered] = React.useState(false)
  const url = item.url
  const label = item.label
  return (
    <a href={url} target="_blank" rel="noreferrer"
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      style={{ display: 'flex', alignItems: 'center', gap: '10px', padding: '10px 18px', borderRadius: '40px', border: hovered ? '1px solid #E8729A' : '1px solid #cec5b5', fontSize: '12px', fontWeight: 500, color: hovered ? '#fff' : '#3a3430', textDecoration: 'none', background: hovered ? '#E8729A' : 'transparent', transition: 'all 0.15s', width: 'fit-content', minWidth: '150px' }}>
      <span style={{ width: '5px', height: '5px', borderRadius: '50%', backgroundColor: hovered ? '#fff' : '#E8729A', flexShrink: 0 }} />
      {label}
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
      <div style={{ fontFamily: 'DM Serif Display, serif', fontSize: '48px', color: '#E8729A', lineHeight: 0.95, position: 'relative', zIndex: 1 }}>{title}</div>
      <div style={{ fontFamily: 'Caveat, cursive', fontSize: '17px', color: '#c4a0b0', marginTop: '6px', position: 'relative', zIndex: 1 }}>{sub}</div>
    </div>
  )
}

const SkillsIllustration = () => (
  <svg width="280" height="200" viewBox="0 0 260 180" fill="none">
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
  <svg width="280" height="200" viewBox="0 0 260 180" fill="none">
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
  <svg width="280" height="200" viewBox="0 0 260 180" fill="none">
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

const InterestsIllustration = () => (
  <svg width="280" height="200" viewBox="0 0 280 180" fill="none">
    <ellipse cx="38" cy="52" rx="22" ry="28" stroke="#E8729A" strokeWidth="1.8" fill="#E8729A" fillOpacity="0.06" opacity="0.4"/>
    <line x1="38" y1="25" x2="38" y2="79" stroke="#E8729A" strokeWidth="1" opacity="0.12"/>
    <line x1="16" y1="52" x2="60" y2="52" stroke="#E8729A" strokeWidth="1" opacity="0.12"/>
    <line x1="38" y1="79" x2="34" y2="115" stroke="#E8729A" strokeWidth="2.2" strokeLinecap="round" opacity="0.4"/>
    <circle cx="75" cy="20" r="6" fill="#E8729A" fillOpacity="0.1" stroke="#E8729A" strokeWidth="1.5" opacity="0.32"/>
    <path d="M75 14 L68 4 M75 14 L75 3 M75 14 L82 4" stroke="#E8729A" strokeWidth="1" opacity="0.25"/>
    <circle cx="145" cy="36" r="11" stroke="#E8729A" strokeWidth="1.8" fill="#E8729A" fillOpacity="0.07" opacity="0.4"/>
    <path d="M145 47 L145 80" stroke="#E8729A" strokeWidth="1.8" strokeLinecap="round" opacity="0.4"/>
    <path d="M145 60 L129 52" stroke="#E8729A" strokeWidth="1.8" strokeLinecap="round" opacity="0.4"/>
    <path d="M145 60 L161 48" stroke="#E8729A" strokeWidth="1.8" strokeLinecap="round" opacity="0.4"/>
    <path d="M145 80 L133 98" stroke="#E8729A" strokeWidth="1.8" strokeLinecap="round" opacity="0.4"/>
    <path d="M145 80 L157 96" stroke="#E8729A" strokeWidth="1.8" strokeLinecap="round" opacity="0.4"/>
    <text x="162" y="60" fontFamily="sans-serif" fontSize="18" fill="#E8729A" opacity="0.22">&#9835;</text>
    <path d="M196 108 L196 148 Q214 143 232 148 L232 108 Q214 112 196 108Z" fill="#E8729A" fillOpacity="0.07" stroke="#E8729A" strokeWidth="1.5" opacity="0.32"/>
    <path d="M196 108 L196 148 Q178 143 160 148 L160 108 Q178 112 196 108Z" fill="#E8729A" fillOpacity="0.05" stroke="#E8729A" strokeWidth="1.5" opacity="0.28"/>
    <rect x="30" y="133" width="26" height="22" rx="4" fill="#E8729A" fillOpacity="0.09" stroke="#E8729A" strokeWidth="1.5" opacity="0.32"/>
    <path d="M34 133 Q43 118 43 115 Q47 119 52 133" fill="#E8729A" fillOpacity="0.12" stroke="#E8729A" strokeWidth="1.2" opacity="0.32"/>
    <circle cx="43" cy="105" r="2.5" fill="#E8729A" opacity="0.28"/>
    <rect x="95" y="120" width="7" height="40" rx="3.5" transform="rotate(-18 95 120)" fill="#E8729A" fillOpacity="0.1" stroke="#E8729A" strokeWidth="1.2" opacity="0.32"/>
  </svg>
)

export default function Home() {
  const navigate = useNavigate()
  return (
    <div style={{ backgroundColor: '#C8BFB0', minHeight: '100vh', padding: '14px', display: 'flex', flexDirection: 'column', gap: '10px' }}>

      <div style={{ backgroundColor: '#F5F0E8', borderRadius: '14px', display: 'flex', overflow: 'hidden', minHeight: '460px', position: 'relative' }}>
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
            <div style={{ fontFamily: 'Caveat, cursive', fontSize: '20px', color: '#8a8075', marginTop: '4px' }}>Bridging technology, people, and ideas.</div>
          </div>
          <div>
            <div style={{ fontSize: '13px', color: '#7a7065', lineHeight: 1.8, maxWidth: '380px', borderLeft: '2px solid #E8729A', paddingLeft: '16px' }}>I am a full stack developer who loves building things at the intersection of design and technology. I care deeply about creating experiences that feel good to use. Always learning, always building.</div>
            <div style={{ fontFamily: 'Caveat, cursive', fontSize: '14px', color: '#9a9285', marginTop: '10px' }}>Based in India</div>
          </div>
        </div>
        <div style={{ width: '300px', backgroundColor: '#E0D9CE', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'flex-end', flexShrink: 0, position: 'relative', zIndex: 1 }}>
          <span style={{ position: 'absolute', top: '20px', right: '28px', fontFamily: 'Caveat, cursive', fontSize: '28px', color: '#E8729A', opacity: 0.38 }}>*</span>
          <span style={{ position: 'absolute', top: '58px', right: '58px', fontFamily: 'Caveat, cursive', fontSize: '14px', color: '#E8729A', opacity: 0.25 }}>*</span>
          <span style={{ position: 'absolute', top: '100px', right: '24px', fontFamily: 'Caveat, cursive', fontSize: '18px', color: '#E8729A', opacity: 0.2 }}>o</span>
          <span style={{ position: 'absolute', bottom: '80px', left: '16px', fontFamily: 'Caveat, cursive', fontSize: '13px', color: '#E8729A', opacity: 0.22 }}>+</span>
          <div style={{ width: '200px', height: '290px', backgroundColor: '#ccc4b5', borderRadius: '100px 100px 0 0', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <span style={{ fontSize: '52px', opacity: 0.22 }}>:)</span>
          </div>
          <div style={{ position: 'absolute', bottom: '14px', fontSize: '10px', color: '#9a9285', letterSpacing: '0.07em' }}>your photo here</div>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
        <NavCard num="01" title="My Skills" sub="What I bring to the table" doodle="o" illustration={<SkillsIllustration />} squiggle onClick={() => navigate('/skills')} />
        <NavCard num="02" title="My Projects" sub="Things I have built" doodle="+" illustration={<ProjectsIllustration />} onClick={() => navigate('/projects')} />
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
        <NavCard num="03" title="My Blog" sub="Thoughts and writing" doodle="~ life stories ~" illustration={<BlogIllustration />} squiggle onClick={() => navigate('/blog')} />
        <NavCard num="04" title="My Interests" sub="Beyond the screen" doodle="*" illustration={<InterestsIllustration />} onClick={() => navigate('/interests')} />
      </div>

      <div style={{ backgroundColor: '#F5F0E8', borderRadius: '14px', padding: '52px 48px', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '32px', minHeight: '280px', position: 'relative', overflow: 'hidden' }}>
        <div style={{ position: 'absolute', bottom: '-20px', right: '-10px', fontFamily: 'DM Serif Display, serif', fontSize: '160px', color: '#E8729A', opacity: 0.04, lineHeight: 1, userSelect: 'none', whiteSpace: 'nowrap' }}>connect</div>
        <div style={{ position: 'relative', zIndex: 1, display: 'flex', flexDirection: 'column' }}>
          <div style={{ fontFamily: 'DM Serif Display, serif', fontSize: '44px', color: '#3a3430', lineHeight: 1, marginBottom: '6px' }}>Connect<br />with me</div>
          <div style={{ fontFamily: 'Caveat, cursive', fontSize: '17px', color: '#9a9285', marginBottom: '20px' }}>let us build something together</div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {connectLinks.map((item) => (<ConnectLink key={item.label} item={item} />))}
          </div>
          <div style={{ fontFamily: 'Caveat, cursive', fontSize: '13px', color: '#9a9285', marginTop: '16px' }}>Based in India - Open to remote work</div>
        </div>
        <div style={{ backgroundColor: '#EDE7DC', borderRadius: '14px', padding: '32px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', position: 'relative', overflow: 'hidden', zIndex: 1 }}>
          <div style={{ position: 'absolute', bottom: '-10px', right: '-8px', fontFamily: 'Caveat, cursive', fontSize: '90px', color: '#E8729A', opacity: 0.07, userSelect: 'none' }}>hi!</div>
          <div>
            <div style={{ fontFamily: 'DM Serif Display, serif', fontSize: '26px', color: '#3a3430' }}>Lets work together</div>
            <div style={{ fontSize: '12px', color: '#7a7065', lineHeight: 1.7, marginTop: '8px' }}>Have a project in mind, a question, or just want to say hi? I would love to hear from you.</div>
            <div style={{ fontFamily: 'Caveat, cursive', fontSize: '18px', color: '#E8729A', marginTop: '14px' }}>kaavyaindhu06@gmail.com</div>
            <div style={{ fontFamily: 'Caveat, cursive', fontSize: '13px', color: '#E8729A', opacity: 0.5, marginTop: '2px' }}>shoot me a mail!</div>
          </div>
          <MessageButton />
        </div>
      </div>

    </div>
  )
}
""")
f.close()
print("Done!")
PYEOF