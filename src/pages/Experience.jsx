import { useNavigate } from 'react-router-dom';

export default function Experience() {
  const navigate = useNavigate();

  const SectionLabel = ({ text, color }) => (
    <p style={{ fontSize: 13, fontWeight: 500, letterSpacing: '1.5px', textTransform: 'uppercase', color: color, margin: '18px 0 7px' }}>{text}</p>
  );

  const SectionText = ({ text, color }) => (
    <p style={{ fontSize: 17, lineHeight: 1.9, color: color, margin: 0 }}>{text}</p>
  );

  const PicBox = ({ bg, stroke, doodle }) => (
    <div style={{ width: 140, height: 140, borderRadius: 20, background: bg, flexShrink: 0, display: 'flex', alignItems: 'center', justifyContent: 'center', alignSelf: 'flex-start', marginTop: 4 }}>
      {doodle}
    </div>
  );

  const ArrowConnector = ({ direction, label, color }) => (
    <div style={{ display: 'flex', justifyContent: 'center', padding: '8px 0', margin: '18px 0' }}>
      {direction === 'right-to-left' ? (
        <svg width='360' height='68' viewBox='0 0 360 68' fill='none'>
          <path d='M280 8 Q280 58 80 58' stroke={color} strokeWidth='3.5' strokeLinecap='round'/>
          <polyline points='66,47 80,58 66,69' stroke={color} strokeWidth='3.5' strokeLinecap='round' strokeLinejoin='round'/>
          <text x='180' y='46' textAnchor='middle' fontFamily='Caveat,cursive' fontSize='17' fill={color}>{label}</text>
        </svg>
      ) : (
        <svg width='360' height='68' viewBox='0 0 360 68' fill='none'>
          <path d='M80 8 Q80 58 280 58' stroke={color} strokeWidth='3.5' strokeLinecap='round'/>
          <polyline points='294,47 280,58 294,69' stroke={color} strokeWidth='3.5' strokeLinecap='round' strokeLinejoin='round'/>
          <text x='180' y='46' textAnchor='middle' fontFamily='Caveat,cursive' fontSize='17' fill={color}>{label}</text>
        </svg>
      )}
    </div>
  );

  const doodleHR = (
    <svg width='80' height='80' viewBox='0 0 80 80' fill='none' stroke='#E8729A' strokeWidth='1.6'>
      <circle cx='40' cy='28' r='14'/>
      <path d='M12 76 Q12 54 40 54 Q68 54 68 76' strokeLinecap='round'/>
      <line x1='28' y1='60' x2='28' y2='72'/>
      <line x1='52' y1='60' x2='52' y2='72'/>
    </svg>
  );

  const doodleMarketing = (
    <svg width='80' height='80' viewBox='0 0 80 80' fill='none' stroke='#E8729A' strokeWidth='1.6'>
      <polyline points='10,60 25,38 38,50 55,24 70,34' strokeLinecap='round' strokeLinejoin='round'/>
      <circle cx='25' cy='38' r='3.5' fill='#E8729A'/>
      <circle cx='55' cy='24' r='3.5' fill='#E8729A'/>
      <line x1='10' y1='66' x2='70' y2='66'/>
    </svg>
  );

  const doodleRD = (
    <svg width='80' height='80' viewBox='0 0 80 80' fill='none' stroke='#8a3455' strokeWidth='1.6'>
      <circle cx='40' cy='40' r='20'/>
      <circle cx='40' cy='40' r='8'/>
      <circle cx='40' cy='40' r='3' fill='#8a3455'/>
      <line x1='40' y1='10' x2='40' y2='20'/>
      <line x1='40' y1='60' x2='40' y2='70'/>
      <line x1='10' y1='40' x2='20' y2='40'/>
      <line x1='60' y1='40' x2='70' y2='40'/>
    </svg>
  );

  const doodleTech = (
    <svg width='80' height='80' viewBox='0 0 80 80' fill='none' stroke='#8a3455' strokeWidth='1.6'>
      <rect x='12' y='18' width='56' height='38' rx='6'/>
      <line x1='12' y1='30' x2='68' y2='30'/>
      <circle cx='22' cy='24' r='3' fill='#8a3455'/>
      <circle cx='32' cy='24' r='3' fill='#8a3455'/>
      <polyline points='20,44 30,38 40,46 56,34' strokeLinecap='round' strokeLinejoin='round'/>
      <line x1='28' y1='56' x2='52' y2='56'/>
      <line x1='40' y1='56' x2='40' y2='64'/>
    </svg>
  );

  const doodleVice = (
    <svg width='80' height='80' viewBox='0 0 80 80' fill='none' stroke='#8a3455' strokeWidth='1.6'>
      <circle cx='40' cy='24' r='12'/>
      <path d='M14 72 Q14 52 40 52 Q66 52 66 72' strokeLinecap='round'/>
      <polyline points='32,36 40,46 48,36'/>
      <line x1='40' y1='46' x2='40' y2='56'/>
      <line x1='28' y1='58' x2='52' y2='58'/>
    </svg>
  );

  return (
    <div style={{ background: '#C8BFB0', minHeight: '100vh', padding: '14px', fontFamily: 'Inter, sans-serif' }}>

      <button onClick={() => navigate('/')} style={{ display: 'inline-flex', alignItems: 'center', gap: 8, fontSize: 16, color: '#3a3430', background: '#F5F0E8', border: 'none', borderRadius: 40, padding: '10px 24px', cursor: 'pointer', marginBottom: 14, fontFamily: 'Inter, sans-serif', fontWeight: 500 }}>
        ← Home
      </button>

      <h1 style={{ fontFamily: 'DM Serif Display, serif', fontSize: 'clamp(52px, 9vw, 80px)', color: '#E8729A', lineHeight: 1, margin: 0 }}>My Experience</h1>
      <p style={{ fontFamily: 'Caveat, cursive', fontSize: 28, color: '#9a9285', margin: '6px 0 20px' }}>where I have been</p>

      <div className='exp-company-card' style={{ background: '#F5F0E8', borderRadius: 14, padding: '40px 44px 48px', marginBottom: 10 }}>
        <p style={{ fontFamily: 'Caveat, cursive', fontSize: 18, color: '#c4a0b0', letterSpacing: 1, textTransform: 'uppercase', margin: '0 0 6px' }}>01 / internship · 2 months</p>
        <h2 style={{ fontFamily: 'DM Serif Display, serif', fontSize: 38, color: '#3a3430', margin: '0 0 36px', lineHeight: 1.1 }}>Foodworks Gourmet Private Limited (TOVO)</h2>

        <div className='exp-role-block' style={{ display: 'flex', gap: 36, alignItems: 'flex-start' }}>
          <PicBox bg='#EDE7DC' doodle={doodleHR} />
          <div style={{ flex: 1 }}>
            <h3 style={{ fontFamily: 'DM Serif Display, serif', fontSize: 30, color: '#3a3430', margin: '0 0 4px' }}>Human Resources</h3>
            <SectionLabel text='What I did' color='#b0a898' />
            <SectionText color='#5a5248' text='I conducted employee surveys to understand team and customer-facing dynamics, and built a dynamic system to track retention and turnover across eleven branches. I researched what makes a store run smoothly and supported the hiring of over fifty employees. I also reached out to universities across three cities to create internship opportunities for students.' />
            <SectionLabel text='What I learnt' color='#b0a898' />
            <SectionText color='#5a5248' text='I learned how to analyse employee data and understand its real impact on business performance. This experience improved my communication and my ability to assess people during hiring. I also came to understand how deeply employee satisfaction and structure influence overall store efficiency.' />
          </div>
        </div>

        <ArrowConnector direction='right-to-left' label='also at TOVO' color='#c4a0b0' />

        <div className='exp-role-block-flip' style={{ display: 'flex', flexDirection: 'row-reverse', gap: 36, alignItems: 'flex-start' }}>
          <PicBox bg='#EDE7DC' doodle={doodleMarketing} />
          <div style={{ flex: 1 }}>
            <h3 style={{ fontFamily: 'DM Serif Display, serif', fontSize: 30, color: '#3a3430', margin: '0 0 4px' }}>Marketing</h3>
            <SectionLabel text='What I did' color='#b0a898' />
            <SectionText color='#5a5248' text='I managed the end-to-end execution of a month-long shoot by generating leads, shortlisting candidates, and coordinating with collaborators. I handled negotiations with agencies and creators, and ensured smooth execution across branches. I also managed the full payment process and overall coordination from start to finish.' />
            <SectionLabel text='What I learnt' color='#b0a898' />
            <SectionText color='#5a5248' text='I learned how to identify the right people for brand representation and manage multiple stakeholders at the same time. This sharpened my negotiation, decision making, and problem solving skills. I also gained a clear understanding of how marketing campaigns are executed in real time and what it actually takes to pull them off.' />
          </div>
        </div>
      </div>

      <div className='exp-company-card' style={{ background: '#EDE0E8', borderRadius: 14, padding: '40px 44px 48px' }}>
        <p style={{ fontFamily: 'Caveat, cursive', fontSize: 18, color: '#b888a4', letterSpacing: 1, textTransform: 'uppercase', margin: '0 0 6px' }}>02 / current · club</p>
        <h2 style={{ fontFamily: 'DM Serif Display, serif', fontSize: 38, color: '#5a2a42', margin: '0 0 36px', lineHeight: 1.1 }}>Centre for Social Entrepreneurship and Development (CSED)</h2>

        <div className='exp-role-block' style={{ display: 'flex', gap: 36, alignItems: 'flex-start' }}>
          <PicBox bg='#e8ccd8' doodle={doodleRD} />
          <div style={{ flex: 1 }}>
            <h3 style={{ fontFamily: 'DM Serif Display, serif', fontSize: 30, color: '#5a2a42', margin: '0 0 4px' }}>R&D Member</h3>
            <SectionLabel text='What I did' color='#b888a4' />
            <SectionText color='#6a3a52' text='I worked on researching startups, market trends, and business models to support ideation for various events and initiatives. I contributed to structuring problem statements, refining event concepts, and ensuring alignment with CSED focus on entrepreneurship. I created and maintained structured documentation such as case studies, reports, and MOMs to support clarity and continuity. I collaborated with different teams to ensure ideas were feasible and could be effectively implemented, and also supported content creation and knowledge-sharing initiatives within the club.' />
            <SectionLabel text='What I learnt' color='#b888a4' />
            <SectionText color='#6a3a52' text='I developed strong analytical and critical thinking skills by evaluating ideas based on feasibility, impact, and execution. I learned how to structure unrefined ideas into clear and actionable frameworks. I improved my research and documentation skills, ensuring information was organised and usable. I also understood how research directly influences decision-making and overall event quality, and learned how to align creativity with practicality in a team-driven environment.' />
          </div>
        </div>

        <ArrowConnector direction='right-to-left' label='also at CSED' color='#b888a4' />

        <div className='exp-role-block-flip' style={{ display: 'flex', flexDirection: 'row-reverse', gap: 36, alignItems: 'flex-start' }}>
          <PicBox bg='#e8ccd8' doodle={doodleTech} />
          <div style={{ flex: 1 }}>
            <h3 style={{ fontFamily: 'DM Serif Display, serif', fontSize: 30, color: '#5a2a42', margin: '0 0 4px' }}>Technical Team Member</h3>
            <SectionLabel text='What I did' color='#b888a4' />
            <SectionText color='#6a3a52' text='I worked on developing and improving event websites and digital platforms, focusing on frontend development and UI enhancements. I handled registration systems, dynamic forms, and basic backend integrations, ensuring smooth data flow and user experience. I supported deployment and live technical setups during events, troubleshooting issues in real time. I also collaborated with teams to translate requirements into functional systems, including the CSED website update and event platforms for Gravitas and Yantra.' />
            <SectionLabel text='What I learnt' color='#b888a4' />
            <SectionText color='#6a3a52' text='I gained hands-on experience in web development, including working with frontend technologies, APIs, and basic backend logic. I developed strong debugging and problem-solving skills, especially in real-time scenarios. I learned how to build scalable and user-friendly systems while managing performance and reliability. I also improved my ability to work in collaborative development environments using version control and structured workflows.' />
          </div>
        </div>

        <ArrowConnector direction='left-to-right' label='then promoted to' color='#b888a4' />

        <div className='exp-role-block' style={{ display: 'flex', gap: 36, alignItems: 'flex-start' }}>
          <PicBox bg='#e8ccd8' doodle={doodleVice} />
          <div style={{ flex: 1 }}>
            <h3 style={{ fontFamily: 'DM Serif Display, serif', fontSize: 30, color: '#5a2a42', margin: '0 0 4px' }}>Vice Chairperson</h3>
            <SectionLabel text='What I did' color='#b888a4' />
            <SectionText color='#6a3a52' text='As Vice Chairperson, I took responsibility for coordinating across departments to ensure smooth communication, clear timelines, and proper execution of tasks. I handled key administrative work including documentation, approvals, meeting scheduling, and maintaining structured records for the club. I worked closely with the board to align decisions, resolve issues, and ensure all activities were carried out in an organised manner. I also supported member management, recruitment processes, and external collaborations that contributed to the overall growth of the club.' />
            <SectionLabel text='What I learnt' color='#b888a4' />
            <SectionText color='#6a3a52' text='This role helped me understand leadership beyond titles — taking ownership, supporting teams, and ensuring stability during both planning and execution. I learned how to manage people, handle responsibilities calmly under pressure, and maintain clear communication across different teams. I developed a strong sense of accountability and learned how to make decisions that prioritise the club as a whole. Most importantly, I learned how to create a positive and approachable environment where people feel comfortable, respected, and motivated to contribute.' />
          </div>
        </div>

      </div>
    </div>
  );
}