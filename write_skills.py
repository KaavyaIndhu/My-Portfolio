content = '''import { useNavigate } from "react-router-dom";

const skills = [
  {
    id: "01", label: "backend", title: "Backend & Data",
    pills: ["Python", "Java", "C", "C++", "Node.js", "Go", "MongoDB", "SQL", "DSA"],
    bg: "#F5F0E8", labelColor: "#c4a0b0", titleColor: "#3a3430",
    pillBg: "#E0D9CE", pillText: "#3a3430",
    doodle: (
      <svg width="120" height="110" viewBox="0 0 64 64" fill="none" stroke="#E8729A" strokeWidth="1.4">
        <rect x="8" y="16" width="48" height="36" rx="4"/>
        <line x1="8" y1="26" x2="56" y2="26"/>
        <circle cx="16" cy="21" r="2.5" fill="#E8729A"/>
        <circle cx="24" cy="21" r="2.5" fill="#E8729A"/>
        <circle cx="32" cy="21" r="2.5" fill="#E8729A"/>
        <polyline points="16,38 24,32 34,40 48,30" strokeLinecap="round" strokeLinejoin="round"/>
      </svg>
    ),
  },
  {
    id: "02", label: "frontend", title: "Frontend & UI",
    pills: ["React.js", "Next.js", "TypeScript", "JavaScript", "Tailwind CSS", "HTML", "CSS"],
    bg: "#EDE0E8", labelColor: "#b888a4", titleColor: "#5a2a42",
    pillBg: "#f5d4e0", pillText: "#8a3455",
    doodle: (
      <svg width="120" height="110" viewBox="0 0 64 64" fill="none" stroke="#E8729A" strokeWidth="1.4">
        <rect x="6" y="12" width="52" height="36" rx="5"/>
        <rect x="20" y="48" width="24" height="5" rx="2"/>
        <line x1="14" y1="53" x2="50" y2="53"/>
        <rect x="13" y="19" width="14" height="10" rx="2"/>
        <rect x="13" y="33" width="38" height="3" rx="1.5"/>
        <rect x="31" y="19" width="20" height="10" rx="2"/>
        <line x1="35" y1="22" x2="47" y2="22"/>
        <line x1="35" y1="25" x2="44" y2="25"/>
      </svg>
    ),
  },
  {
    id: "03", label: "tooling", title: "Tools & APIs",
    pills: ["Git", "GitHub", "REST APIs", "FastAPI"],
    bg: "#D9EDE6", labelColor: "#5a9e86", titleColor: "#1a4a38",
    pillBg: "#b8dfd4", pillText: "#1a5040",
    doodle: (
      <svg width="120" height="110" viewBox="0 0 64 64" fill="none" stroke="#E8729A" strokeWidth="1.4">
        <circle cx="32" cy="32" r="11"/>
        <circle cx="32" cy="32" r="3.5" fill="#E8729A"/>
        <line x1="32" y1="8" x2="32" y2="18"/>
        <line x1="32" y1="46" x2="32" y2="56"/>
        <line x1="8" y1="32" x2="18" y2="32"/>
        <line x1="46" y1="32" x2="56" y2="32"/>
        <line x1="15" y1="15" x2="22" y2="22"/>
        <line x1="42" y1="42" x2="49" y2="49"/>
        <line x1="49" y1="15" x2="42" y2="22"/>
        <line x1="22" y1="42" x2="15" y2="49"/>
      </svg>
    ),
  },
  {
    id: "04", label: "soft skills", title: "Soft Skills",
    pills: ["Human Resources", "Marketing", "R&D", "Leadership", "Teamwork", "Communication", "Adaptability", "Curiosity"],
    bg: "#F5EDD8", labelColor: "#c4956a", titleColor: "#5a3a10",
    pillBg: "#f0d8a8", pillText: "#7a4f10",
    doodle: (
      <svg width="120" height="110" viewBox="0 0 64 64" fill="none" stroke="#E8729A" strokeWidth="1.4">
        <circle cx="32" cy="20" r="9"/>
        <path d="M14 52 Q14 38 32 38 Q50 38 50 52" strokeLinecap="round"/>
        <circle cx="16" cy="27" r="6"/>
        <path d="M4 50 Q4 40 16 40" strokeLinecap="round"/>
        <circle cx="48" cy="27" r="6"/>
        <path d="M60 50 Q60 40 48 40" strokeLinecap="round"/>
      </svg>
    ),
  },
];

export default function Skills() {
  const navigate = useNavigate();

  return (
    <div style={{ background: "#C8BFB0", minHeight: "100vh", padding: "14px", fontFamily: "Inter, sans-serif" }}>

      <button
        onClick={() => navigate("/")}
        style={{
          display: "inline-flex", alignItems: "center", gap: "8px",
          fontSize: "15px", color: "#3a3430", background: "#F5F0E8",
          border: "none", borderRadius: "40px", padding: "10px 22px",
          cursor: "pointer", marginBottom: "14px", fontFamily: "Inter, sans-serif", fontWeight: 500,
        }}
      >
        ← Home
      </button>

      <h1 style={{ fontFamily: "DM Serif Display, serif", fontSize: "clamp(48px, 8vw, 72px)", color: "#E8729A", lineHeight: 1, margin: 0 }}>
        My Skills
      </h1>
      <p style={{ fontFamily: "Caveat, cursive", fontSize: "22px", color: "#9a9285", margin: "4px 0 18px" }}>
        things I know, love & am learning
      </p>

      <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
        {skills.map((s) => (
          <div
            key={s.id}
            style={{
              background: s.bg, borderRadius: "14px",
              padding: "40px 44px 36px", position: "relative",
              overflow: "hidden", minHeight: "220px",
            }}
          >
            <p style={{ fontFamily: "Caveat, cursive", fontSize: "15px", color: s.labelColor, letterSpacing: "1px", textTransform: "uppercase", margin: "0 0 6px" }}>
              {s.id} / {s.label}
            </p>
            <h2 style={{ fontFamily: "DM Serif Display, serif", fontSize: "48px", color: s.titleColor, margin: "0 0 22px", lineHeight: 1.05 }}>
              {s.title}
            </h2>
            <div style={{ display: "flex", flexWrap: "wrap", gap: "10px", paddingRight: "140px" }}>
              {s.pills.map((pill) => (
                <span key={pill} style={{ background: s.pillBg, color: s.pillText, borderRadius: "40px", padding: "10px 22px", fontSize: "15px", fontFamily: "Inter, sans-serif", fontWeight: 500 }}>
                  {pill}
                </span>
              ))}
            </div>
            <div style={{ position: "absolute", bottom: "24px", right: "36px", opacity: 0.22 }}>
              {s.doodle}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
'''

with open("src/pages/Skills.jsx", "w") as f:
    f.write(content)

print("Skills.jsx written!")
