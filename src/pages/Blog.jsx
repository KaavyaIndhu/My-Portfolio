import { useNavigate } from 'react-router-dom';

export default function Blog() {
  const navigate = useNavigate();
  return (
    <div style={{ background: '#C8BFB0', minHeight: '100vh', padding: '14px', fontFamily: 'Inter, sans-serif', display: 'flex', flexDirection: 'column' }}>
      <button onClick={() => navigate('/')} style={{ display: 'inline-flex', alignItems: 'center', gap: 8, fontSize: 16, color: '#3a3430', background: '#F5F0E8', border: 'none', borderRadius: 40, padding: '10px 24px', cursor: 'pointer', marginBottom: 14, fontFamily: 'Inter, sans-serif', fontWeight: 500, width: 'fit-content' }}>
        ← Home
      </button>
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', textAlign: 'center', paddingBottom: 60 }}>
        <svg width='180' height='180' viewBox='0 0 180 180' fill='none'>
          <path d='M90 150 C90 150 20 110 20 65 C20 40 38 22 60 22 C72 22 83 28 90 38 C97 28 108 22 120 22 C142 22 160 40 160 65 C160 110 90 150 90 150 Z' fill='#f5d4e0' stroke='#E8729A' strokeWidth='2'/>
          <path d='M90 138 C90 138 32 102 32 65 C32 46 46 34 60 34 C71 34 80 40 86 50' stroke='#E8729A' strokeWidth='1.4' fill='none' strokeLinecap='round' opacity='0.4'/>
        </svg>
        <h1 style={{ fontFamily: 'DM Serif Display, serif', fontSize: 'clamp(52px, 9vw, 80px)', color: '#E8729A', lineHeight: 1, margin: '24px 0 0' }}>My Blog</h1>
        <p style={{ fontFamily: 'Caveat, cursive', fontSize: 32, color: '#9a9285', margin: '10px 0 0' }}>coming soon...</p>
        <p style={{ fontFamily: 'Caveat, cursive', fontSize: 26, color: '#b0a898', margin: '8px 0 0' }}>I’m coding it ♥</p>
        <p style={{ fontSize: 17, color: '#7a6e68', lineHeight: 1.8, maxWidth: 480, margin: '28px auto 0' }}>This space will be home to my thoughts, life lessons, and personal stories. Check back soon.</p>
      </div>
    </div>
  );
}