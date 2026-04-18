content = """import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { client } from '../lib/sanity';

export default function Blog() {
  const navigate = useNavigate();
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    client
      .fetch(`*[_type == "post"] | order(publishedAt desc) {
        _id,
        title,
        slug,
        publishedAt,
        excerpt,
        body
      }`)
      .then((data) => {
        setPosts(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  return (
    <div style={{ background: '#C8BFB0', minHeight: '100vh', padding: '14px', fontFamily: 'Inter, sans-serif' }}>
      <button onClick={() => navigate('/')} style={{ display: 'inline-flex', alignItems: 'center', gap: 8, fontSize: 16, color: '#3a3430', background: '#F5F0E8', border: 'none', borderRadius: 40, padding: '10px 24px', cursor: 'pointer', marginBottom: 14, fontFamily: 'Inter, sans-serif', fontWeight: 500, width: 'fit-content' }}>
        \\u2190 Home
      </button>

      <h1 style={{ fontFamily: 'DM Serif Display, serif', fontSize: 'clamp(52px, 9vw, 80px)', color: '#E8729A', lineHeight: 1, margin: 0 }}>My Blog</h1>
      <p style={{ fontFamily: 'Caveat, cursive', fontSize: 28, color: '#9a9285', margin: '6px 0 28px' }}>thoughts and writing</p>

      {loading && (
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: 300 }}>
          <p style={{ fontFamily: 'Caveat, cursive', fontSize: 24, color: '#9a9285' }}>loading posts...</p>
        </div>
      )}

      {!loading && posts.length === 0 && (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: 300, textAlign: 'center' }}>
          <svg width='180' height='160' viewBox='0 0 180 160' fill='none'>
            <path d='M90 130 C90 130 20 90 20 50 C20 28 36 14 54 14 C65 14 75 20 81 30 C87 20 97 14 108 14 C126 14 142 28 142 50 C142 90 90 130 90 130 Z' fill='#f5d4e0' stroke='#E8729A' strokeWidth='2'/>
          </svg>
          <p style={{ fontFamily: 'DM Serif Display, serif', fontSize: 36, color: '#E8729A', margin: '20px 0 0' }}>coming soon</p>
          <p style={{ fontFamily: 'Caveat, cursive', fontSize: 26, color: '#9a9285', margin: '8px 0 0' }}>I'm writing \\u2665</p>
          <p style={{ fontSize: 16, color: '#7a6e68', lineHeight: 1.8, maxWidth: 400, margin: '20px auto 0' }}>This space will be home to my thoughts, life lessons, and personal stories. Check back soon.</p>
        </div>
      )}

      {!loading && posts.length > 0 && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
          {posts.map((post, idx) => {
            const colors = [
              { bg: '#F5F0E8', title: '#3a3430', date: '#b0a898', text: '#5a5248', accent: '#E8729A' },
              { bg: '#EDE0E8', title: '#5a2a42', date: '#b888a4', text: '#6a3a52', accent: '#8a3455' },
              { bg: '#D9EDE6', title: '#1a4a38', date: '#5a9e86', text: '#2a5a48', accent: '#1a5040' },
              { bg: '#F5EDD8', title: '#5a3a10', date: '#c4956a', text: '#6a4a20', accent: '#7a4f10' },
              { bg: '#E8E0F0', title: '#3a1a5a', date: '#9070c0', text: '#4a2a6a', accent: '#4a2070' },
            ];
            const c = colors[idx % colors.length];
            const date = post.publishedAt ? new Date(post.publishedAt).toLocaleDateString('en-IN', { year: 'numeric', month: 'long', day: 'numeric' }) : '';
            return (
              <div key={post._id} style={{ background: c.bg, borderRadius: 14, padding: '36px 44px', position: 'relative', overflow: 'hidden' }}>
                <p style={{ fontFamily: 'Caveat, cursive', fontSize: 15, color: c.date, letterSpacing: 1, textTransform: 'uppercase', margin: '0 0 8px' }}>{date}</p>
                <h2 style={{ fontFamily: 'DM Serif Display, serif', fontSize: 38, color: c.title, margin: '0 0 16px', lineHeight: 1.1 }}>{post.title}</h2>
                {post.excerpt && (
                  <p style={{ fontSize: 17, color: c.text, lineHeight: 1.85, maxWidth: 680, margin: '0 0 20px' }}>{post.excerpt}</p>
                )}
                <div style={{ display: 'inline-flex', alignItems: 'center', gap: 8, fontSize: 14, fontWeight: 500, background: c.accent, color: '#fff', borderRadius: 40, padding: '8px 20px', cursor: 'default' }}>
                  read more \\u2192
                </div>
                <svg style={{ position: 'absolute', bottom: 16, right: 24, opacity: 0.12 }} width='80' height='60' viewBox='0 0 80 60' fill='none' stroke={c.accent} strokeWidth='1.4'>
                  <path d='M10 50 Q20 30 35 40 Q50 18 65 28 Q75 20 78 14' strokeLinecap='round' strokeLinejoin='round'/>
                  <circle cx='35' cy='40' r='3' fill={c.accent}/>
                  <circle cx='65' cy='28' r='3' fill={c.accent}/>
                </svg>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
"""
with open("src/pages/Blog.jsx", "w") as f:
    f.write(content)
print("Blog.jsx updated!")
