import React, { useState, useMemo, useEffect } from 'react';
import data from './data.json';
import { Search, MapPin, Building, DollarSign, MessageCircle, ArrowUpRight, GraduationCap, FileText, CheckCircle2, Zap, Filter, LayoutGrid, Sparkles } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const JobRow = ({ job, index }) => {
  const [coords, setCoords] = useState({ x: 50, y: 50 });

  const handleMouseMove = (e) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * 100;
    const y = ((e.clientY - rect.top) / rect.height) * 100;
    setCoords({ x, y });
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 30 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.05, duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
      className="job-row"
      onMouseMove={handleMouseMove}
      style={{
        '--mouse-x': `${coords.x}%`,
        '--mouse-y': `${coords.y}%`
      }}
    >
      <div className="job-info">
        <div className="job-company font-display">{job.Company}</div>
        <h2 className="job-title font-display">{job.Title}</h2>

        <div className="job-meta">
          <div className="meta-item">
            <MapPin size={16} className="text-accent-neon" />
            {job.Location}
          </div>
          <div className="meta-item">
            <Building size={16} className="text-accent-neon" />
            {job.Source}
          </div>
        </div>

        <div className="job-tags">
          {job.Requirements?.slice(0, 4).map((req, i) => (
            <span key={i} className="tag">{req}</span>
          ))}
          {job.Requirements?.length > 4 && <span className="tag">+{job.Requirements.length - 4} more</span>}
        </div>

        {job.Gossips && job.Gossips !== 'No community data yet.' && (
          <div className="gossip-box">
            <MessageCircle size={18} className="mt-0.5 shrink-0 text-accent-pink" />
            <p><strong>Insider Intel:</strong> {job.Gossips}</p>
          </div>
        )}
      </div>

      <div className="job-actions">
        <div className="salary-pill font-display">
          <DollarSign size={18} />
          {job.SalaryRange}
        </div>
        <a href={job.Link} target="_blank" rel="noopener noreferrer" className="btn-apply font-display">
          Apply Now <ArrowUpRight size={20} />
        </a>
      </div>
    </motion.div>
  );
};

const App = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCompanies, setSelectedCompanies] = useState([]);
  const [roleFilter, setRoleFilter] = useState('All');
  const [showSalaryOnly, setShowSalaryOnly] = useState(false);

  const roles = ['All', 'Engineering', 'Data', 'Design', 'Marketing', 'Executive', 'Operations'];

  const companies = useMemo(() => {
    const coords = new Set(data.map(j => j.Company));
    return Array.from(coords).sort();
  }, []);

  const handleCompanyToggle = (company) => {
    setSelectedCompanies(prev =>
      prev.includes(company)
        ? prev.filter(c => c !== company)
        : [...prev, company]
    );
  };

  const filteredJobs = useMemo(() => {
    return data.filter(job => {
      const matchesSearch =
        job.Title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        job.Company.toLowerCase().includes(searchTerm.toLowerCase()) ||
        job.Location.toLowerCase().includes(searchTerm.toLowerCase());

      const matchesCompany = selectedCompanies.length === 0 || selectedCompanies.includes(job.Company);

      const matchesRole = roleFilter === 'All' || (() => {
        const title = job.Title.toLowerCase();
        if (roleFilter === 'Engineering') return title.includes('engineer') || title.includes('developer') || title.includes('tech');
        if (roleFilter === 'Data') return title.includes('data') || title.includes('analyst') || title.includes('science');
        if (roleFilter === 'Design') return title.includes('design') || title.includes('ui') || title.includes('ux');
        if (roleFilter === 'Marketing') return title.includes('marketing') || title.includes('sales') || title.includes('growth');
        if (roleFilter === 'Executive') return title.includes('head') || title.includes('manager') || title.includes('lead') || title.includes('officer');
        if (roleFilter === 'Operations') return title.includes('ops') || title.includes('support') || title.includes('admin');
        return true;
      })();

      const matchesSalary = !showSalaryOnly || (job.SalaryRange && !job.SalaryRange.includes('Contact'));

      return matchesSearch && matchesCompany && matchesRole && matchesSalary;
    });
  }, [searchTerm, selectedCompanies, roleFilter, showSalaryOnly]);

  return (
    <div className="layout-wrapper">
      <div className="grain-overlay" />

      {/* Top Navigation */}
      <nav className="top-nav">
        <div className="brand-text font-display">Kaam ko <span className="brand-burst">Sandesh.</span></div>
        <div className="flex gap-8">
          <a href="#jobs" className="text-text-muted hover:text-white transition font-medium flex items-center gap-2">
            <LayoutGrid size={18} /> Market
          </a>
          <a href="#resources" className="text-text-muted hover:text-white transition font-medium flex items-center gap-2">
            <Sparkles size={18} /> Arsenal
          </a>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="hero-section">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="hero-badge font-display"
        >
          <Zap size={14} className="text-accent-neon" /> Nepal's Premium Career Intelligence
        </motion.div>
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="hero-title font-display"
        >
          Elevate Your <br />
          <span className="text-gradient">Professional Path</span>
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="hero-subtitle"
        >
          Unfair advantage for the ambitious. Real-time vacancy tracking with hidden salary benchmarks and verified insider community intel.
        </motion.p>
      </section>

      {/* Main Content */}
      <section id="jobs" className="main-content">
        {/* Sidebar Filters */}
        <aside className="filters-panel">
          <div className="filter-group">
            <h3 className="font-display">Search Intel</h3>
            <div className="relative">
              <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-text-muted" size={18} />
              <input
                type="text"
                placeholder="Job title, company, or location..."
                className="search-input pl-12"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
          </div>

          <div className="filter-group">
            <h3 className="font-display">Specialization</h3>
            <div className="flex flex-wrap gap-2">
              {roles.map(role => (
                <button
                  key={role}
                  onClick={() => setRoleFilter(role)}
                  className={`tag cursor-pointer transition-all ${roleFilter === role ? 'bg-white text-black border-white' : 'hover:border-white/20'}`}
                >
                  {role}
                </button>
              ))}
            </div>
          </div>

          <div className="filter-group">
            <h3 className="font-display">Intelligence Filter</h3>
            <label className="check-item">
              <input
                type="checkbox"
                className="absolute opacity-0 cursor-pointer h-0 w-0"
                checked={showSalaryOnly}
                onChange={() => setShowSalaryOnly(!showSalaryOnly)}
              />
              <div className="check-box">
                {showSalaryOnly && <CheckCircle2 size={16} />}
              </div>
              Disclosed Salary Only
            </label>
          </div>

          <div className="filter-group">
            <h3 className="font-display">Top Entities</h3>
            <div className="flex flex-col gap-1 mt-3 max-h-[300px] overflow-y-auto pr-2 custom-scrollbar">
              {companies.map(company => (
                <label key={company} className="check-item relative">
                  <input
                    type="checkbox"
                    className="absolute opacity-0 cursor-pointer h-0 w-0"
                    checked={selectedCompanies.includes(company)}
                    onChange={() => handleCompanyToggle(company)}
                  />
                  <div className="check-box">
                    {selectedCompanies.includes(company) && <CheckCircle2 size={16} />}
                  </div>
                  {company}
                </label>
              ))}
            </div>
          </div>

          <div className="mt-8 p-6 rounded-2xl bg-white/5 border border-white/5">
            <div className="text-xs text-text-muted uppercase tracking-widest mb-2 font-bold">Real-time Pulse</div>
            <div className="text-2xl font-display font-medium">{filteredJobs.length}</div>
            <div className="text-sm text-text-muted">Opportunities synced</div>
          </div>
        </aside>

        {/* Jobs Feed */}
        <div className="jobs-feed">
          <AnimatePresence mode="popLayout">
            {filteredJobs.length > 0 ? (
              filteredJobs.slice(0, 50).map((job, index) => (
                <JobRow key={`${job.Company}-${job.Title}-${index}`} job={job} index={index} />
              ))
            ) : (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="text-center py-40 bg-white/5 rounded-[40px] border border-dashed border-white/10"
              >
                <div className="text-text-muted mb-4">No intelligence matches your criteria.</div>
                <button onClick={() => { setSearchTerm(''); setSelectedCompanies([]); setRoleFilter('All'); setShowSalaryOnly(false); }} className="text-accent-neon hover:underline">Reset all filters</button>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </section>

      {/* Extra Resources Section */}
      <section id="resources" className="resources-section">
        <div className="text-center mb-20">
          <h2 className="text-5xl font-display font-bold mb-6">Career Arsenal</h2>
          <p className="text-xl text-text-muted max-width-[600px] mx-auto">Tactical resources to navigate the Nepalese tech ecosystem and land your next major role.</p>
        </div>

        <div className="resources-grid">
          <a href="#" className="resource-card group">
            <div className="resource-icon">
              <FileText size={32} />
            </div>
            <h3 className="text-2xl font-display font-bold mb-4">Resume Engineering</h3>
            <p className="text-text-muted leading-relaxed mb-6">
              ATS-optimized templates specifically built for high-growth tech firms. Pass the filters, win the interview.
            </p>
            <div className="mt-auto flex items-center gap-2 text-accent-neon opacity-0 group-hover:opacity-100 transition-opacity">
              Access Templates <ArrowUpRight size={18} />
            </div>
          </a>

          <a href="#" className="resource-card group">
            <div className="resource-icon">
              <MessageCircle size={32} />
            </div>
            <h3 className="text-2xl font-display font-bold mb-4">Interview Playbooks</h3>
            <p className="text-text-muted leading-relaxed mb-6">
              Real interview questions sourced from candidates at Leapfrog, Fusemachines, and eSewa. Know the game.
            </p>
            <div className="mt-auto flex items-center gap-2 text-accent-neon opacity-0 group-hover:opacity-100 transition-opacity">
              View Playbooks <ArrowUpRight size={18} />
            </div>
          </a>

          <a href="#" className="resource-card group">
            <div className="resource-icon">
              <GraduationCap size={32} />
            </div>
            <h3 className="text-2xl font-display font-bold mb-4">Skill Benchmarks</h3>
            <p className="text-text-muted leading-relaxed mb-6">
              What does "Senior" actually mean in Nepal? Verified skill trees and certification paths that recruiters value.
            </p>
            <div className="mt-auto flex items-center gap-2 text-accent-neon opacity-0 group-hover:opacity-100 transition-opacity">
              Explore Benchmarks <ArrowUpRight size={18} />
            </div>
          </a>
        </div>
      </section>

      {/* Footer */}
      <footer>
        <div className="footer-brand font-display">Kaam ko <span className="text-accent-neon">Sandesh.</span></div>
        <div className="text-sm">Precision engineered for the Nepal Tech Community.</div>
        <div className="flex gap-4 mt-6">
          <span className="text-xs py-1 px-3 rounded-full bg-white/5 border border-white/10 uppercase tracking-tighter">Handcrafted in Nepal</span>
          <span className="text-xs py-1 px-3 rounded-full bg-white/5 border border-white/10 uppercase tracking-tighter">Data Radar Engine v2.0</span>
        </div>
      </footer>
    </div>
  );
};

export default App;

