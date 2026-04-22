import { useNavigate } from 'react-router-dom';
import { useState } from 'react';

const projects = [
  {
    id: '01', category: 'CLI Tool', title: 'Git-Inspired Version Control System (MyGit)',
    bg: '#F5F0E8', numColor: '#c4a0b0', titleColor: '#3a3430', aboutColor: '#5a5248',
    labelColor: '#b0a898', pillBg: '#E0D9CE', pillText: '#3a3430',
    linkBg: '#E8729A', linkText: '#fff', arrowBg: '#E0D9CE', arrowText: '#3a3430',
    dotBg: '#E0D9CE', dotActive: '#E8729A', imgBg: '#EDE7DC', accentColor: '#E8729A',
    about: 'I built MyGit because I wanted to actually understand how Git works under the hood, not just use it. So I recreated it from scratch in Go. It can initialise a repository, track file changes through a staging area, save commit snapshots, and even traverse commit history. I also added branch creation and switching, a visual commit graph so you can see history clearly, and a debug mode that traces every internal operation as it happens. The whole thing runs as a command line tool and uses SHA-1 hashing to store files the same way Git does.',
    tech: ['Go', 'CLI', 'SHA-1 Hashing', 'Filesystem Storage'],
    link: 'https://github.com/KaavyaIndhu/mygit', linkLabel: 'View on GitHub',
    images: ['p','p','p'],
  },
  {
    id: '02', category: 'Full Stack Platform', title: 'Predictive Scaling and Root-Cause Intelligence Platform',
    bg: '#EDE0E8', numColor: '#b888a4', titleColor: '#5a2a42', aboutColor: '#6a3a52',
    labelColor: '#b888a4', pillBg: '#f5d4e0', pillText: '#8a3455',
    linkBg: '#8a3455', linkText: '#fff', arrowBg: '#f5d4e0', arrowText: '#8a3455',
    dotBg: '#f5d4e0', dotActive: '#8a3455', imgBg: '#e8ccd8', accentColor: '#8a3455',
    about: 'ScaleGuard came from a question I kept asking myself, what if you could see exactly where your system is going to break before it actually does. This platform lets engineering teams simulate traffic growth, watch how load spreads across their architecture in an interactive 2D and 3D graph, and get ranked root cause suggestions when something goes wrong. It connects logs, monitors risk scores in real time, and models the whole system like a living thing that breathes and strains under pressure. It was one of the most ambitious things I have built.',
    tech: ['React', 'TypeScript', 'FastAPI', 'Three.js', 'Python', 'NetworkX', 'TailwindCSS'],
    link: 'https://github.com/KaavyaIndhu/Scaleguard', linkLabel: 'View on GitHub',
    images: ['p','p','p'],
  },
  {
    id: '03', category: 'Productivity App', title: 'Full-Stack Productivity Tracking Platform',
    bg: '#D9EDE6', numColor: '#5a9e86', titleColor: '#1a4a38', aboutColor: '#2a5a48',
    labelColor: '#5a9e86', pillBg: '#b8dfd4', pillText: '#1a5040',
    linkBg: '#1a5040', linkText: '#fff', arrowBg: '#b8dfd4', arrowText: '#1a5040',
    dotBg: '#b8dfd4', dotActive: '#1a5040', imgBg: '#c4e8dc', accentColor: '#1a5040',
    about: 'I built this app because I genuinely struggled with staying focused and keeping track of what I was working on. It lets you create, update and delete tasks, run timed focus sessions, and see your productivity trends over time. Everything updates in real time through REST APIs so nothing feels slow or stale. The backend runs on Node.js and Express with MongoDB handling all the data, and the frontend is built in React with Tailwind CSS so it works nicely on any screen size. It is one of those projects that I actually use myself.',
    tech: ['React.js', 'Node.js', 'MongoDB', 'Tailwind CSS', 'REST APIs', 'Express'],
    link: 'https://github.com/KaavyaIndhu/FocusFlow', linkLabel: 'View on GitHub',
    images: ['p','p'],
  },
  {
    id: '04', category: 'Club Website', title: 'CSED Official Site',
    bg: '#F5EDD8', numColor: '#c4956a', titleColor: '#5a3a10', aboutColor: '#6a4a20',
    labelColor: '#c4956a', pillBg: '#f0d8a8', pillText: '#7a4f10',
    linkBg: '#7a4f10', linkText: '#fff', arrowBg: '#f0d8a8', arrowText: '#7a4f10',
    dotBg: '#f0d8a8', dotActive: '#7a4f10', imgBg: '#e8d8b0', accentColor: '#7a4f10',
    about: 'This is the official website for CSED, the Centre for Social Entrepreneurship and Development at VIT Vellore, which is the club I am part of. We built it as a team to give the club a proper home on the internet. It has pages for all our members, a full events section, and a newsletter area so people can stay updated with what we are doing. It was a great experience collaborating with other developers and shipping something that real people in our college actually visit and use.',
    tech: ['React.js', 'Group Project'],
    link: 'https://csedvit.com/', linkLabel: 'Visit Site',
    images: ['p','p'],
  },
  {
    id: '05', category: 'Bidding Platform', title: 'Auction2Action',
    bg: '#E8E0F0', numColor: '#9070c0', titleColor: '#3a1a5a', aboutColor: '#4a2a6a',
    labelColor: '#9070c0', pillBg: '#d4c0ec', pillText: '#4a2070',
    linkBg: '#4a2070', linkText: '#fff', arrowBg: '#d4c0ec', arrowText: '#4a2070',
    dotBg: '#d4c0ec', dotActive: '#4a2070', imgBg: '#d8ccec', accentColor: '#4a2070',
    about: 'Auction2Action was built for a live event our club ran where participants had to bid on items in real time as part of a game. We needed a platform that could handle multiple users placing bids at the same time without things going out of sync, so we built secure APIs and used MongoDB to keep all the transaction data clean and consistent. It was fast, it worked under pressure with real people using it, and honestly it was really fun to see it running during the event itself.',
    tech: ['MongoDB', 'REST APIs', 'Group Project'],
    link: '#', linkLabel: 'View Project',
    images: ['p','p'],
  },
];

function ImageCarousel({ images, imgBg, arrowBg, arrowText, dotBg, dotActive }) {
  const [current, setCurrent] = useState(0);
  const prev = () => setCurrent((c) => (c - 1 + images.length) % images.length);
  const next = () => setCurrent((c) => (c + 1) % images.length);
  return (
    <div style={{ width: 300, flexShrink: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 12 }}>
      <div style={{ width: 280, height: 200, borderRadius: 14, background: imgBg, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <svg width='70' height='70' viewBox='0 0 60 60' fill='none' stroke={arrowText} strokeWidth='1.3' opacity='0.3'>
          <rect x='8' y='8' width='44' height='44' rx='6'/>
          <circle cx='22' cy='22' r='6'/>
          <polyline points='8,44 20,30 30,38 44,20 52,28'/>
        </svg>
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
        <button onClick={prev} style={{ width: 36, height: 36, borderRadius: '50%', border: 'none', background: arrowBg, color: arrowText, cursor: 'pointer', fontSize: 20, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>&lsaquo;</button>
        <div style={{ display: 'flex', gap: 6 }}>
          {images.map((_, i) => (<div key={i} style={{ width: 7, height: 7, borderRadius: '50%', background: i === current ? dotActive : dotBg, transition: 'background 0.2s' }} />))}
        </div>
        <button onClick={next} style={{ width: 36, height: 36, borderRadius: '50%', border: 'none', background: arrowBg, color: arrowText, cursor: 'pointer', fontSize: 20, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>&rsaquo;</button>
      </div>
    </div>
  );
}

function MiddleDoodle({ accentColor }) {
  return (
    <div style={{ width: 60, flexShrink: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 16, opacity: 0.25 }}>
      <svg width='24' height='80' viewBox='0 0 24 80' fill='none' stroke={accentColor} strokeWidth='1.5'>
        <line x1='12' y1='0' x2='12' y2='80' strokeDasharray='4 4'/>
      </svg>
      <svg width='28' height='28' viewBox='0 0 28 28' fill='none' stroke={accentColor} strokeWidth='1.5'>
        <circle cx='14' cy='14' r='4' fill={accentColor}/>
        <circle cx='14' cy='14' r='10'/>
      </svg>
      <svg width='24' height='80' viewBox='0 0 24 80' fill='none' stroke={accentColor} strokeWidth='1.5'>
        <line x1='12' y1='0' x2='12' y2='80' strokeDasharray='4 4'/>
      </svg>
    </div>
  );
}

export default function Projects() {
  const navigate = useNavigate();
  const [hovered, setHovered] = useState(null);
  return (
    <div style={{ background: '#C8BFB0', minHeight: '100vh', padding: '14px', fontFamily: 'Inter, sans-serif' }}>
      <button onClick={() => navigate('/')} style={{ display: 'inline-flex', alignItems: 'center', gap: 8, fontSize: 16, color: '#3a3430', background: '#F5F0E8', border: 'none', borderRadius: 40, padding: '10px 24px', cursor: 'pointer', marginBottom: 14, fontFamily: 'Inter, sans-serif', fontWeight: 500 }}>
        ← Home
      </button>
      <h1 style={{ fontFamily: 'DM Serif Display, serif', fontSize: 'clamp(52px, 9vw, 80px)', color: '#E8729A', lineHeight: 1, margin: 0 }}>My Projects</h1>
      <p style={{ fontFamily: 'Caveat, cursive', fontSize: 28, color: '#9a9285', margin: '6px 0 20px' }}>things I have built</p>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
        {projects.map((p, idx) => (
          <div key={p.id} onMouseEnter={() => setHovered(idx)} onMouseLeave={() => setHovered(null)}
            style={{ background: p.bg, borderRadius: 14, padding: '44px 44px',
              display: 'flex', flexDirection: 'row', gap: 0,
              alignItems: 'center', minHeight: 300, position: 'relative', overflow: 'hidden',
              transition: 'box-shadow 0.22s ease, transform 0.22s ease',
              boxShadow: hovered === idx ? '0 16px 48px rgba(58,52,48,0.2)' : 'none',
              transform: hovered === idx ? 'translateY(-4px)' : 'translateY(0)' }}>
            <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 12, paddingRight: 8 }}>
              <p style={{ fontFamily: 'Caveat, cursive', fontSize: 18, color: p.numColor, letterSpacing: 1, textTransform: 'uppercase', margin: 0 }}>{p.id} / {p.category}</p>
              <h2 style={{ fontFamily: 'DM Serif Display, serif', fontSize: 'clamp(26px, 3.5vw, 40px)', color: p.titleColor, margin: 0, lineHeight: 1.1 }}>{p.title}</h2>
              <p style={{ fontSize: 16, color: p.aboutColor, lineHeight: 1.85, margin: 0, maxWidth: '100%' }}>{p.about}</p>
              <p style={{ fontSize: 13, fontWeight: 500, letterSpacing: 1, textTransform: 'uppercase', color: p.labelColor, margin: '10px 0 0' }}>Tech Stack</p>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
                {p.tech.map((t) => (<span key={t} style={{ background: p.pillBg, color: p.pillText, borderRadius: 40, padding: '7px 18px', fontSize: 14 }}>{t}</span>))}
              </div>
              <div onClick={() => p.link !== '#' && window.open(p.link, '_blank')}
                style={{ display: 'inline-flex', alignItems: 'center', gap: 8, marginTop: 12,
                  fontSize: 15, fontWeight: 500, background: p.linkBg, color: p.linkText,
                  borderRadius: 40, padding: '10px 24px', width: 'fit-content',
                  cursor: p.link !== '#' ? 'pointer' : 'default' }}>
                {p.linkLabel} →
              </div>
            </div>
            <MiddleDoodle accentColor={p.accentColor} />
            <div className='proj-carousel'><ImageCarousel images={p.images} imgBg={p.imgBg} arrowBg={p.arrowBg} arrowText={p.arrowText} dotBg={p.dotBg} dotActive={p.dotActive} /></div>
          </div>
        ))}
      </div>
    </div>
  );
}