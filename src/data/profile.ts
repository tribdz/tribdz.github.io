import profileImage from '../assets/profile.jpg'
import resumePdf from '../assets/documents/resume.pdf'
import type { HeroSection, Profile } from '../types/portfolio'

export const profile = {
  name: 'Tran Tri Binh',
  slug: 'tran-tri-binh',
  role: '7th Grade Student',
  location: 'Hanoi Capital Region, Vietnam',
  email: 'trantribinh2021@gmail.com',
  profileImage,
  resume: {
    label: 'Download Resume',
    href: resumePdf,
    fileName: 'Tran-Tri-Binh-Resume.pdf',
    ariaLabel: 'Download Tran Tri Binh resume PDF',
  },
  summary:
    'My name is Tran Tri Binh and I love gaming.',
  socialLinks: [
    {
      label: 'GitHub',
      href: 'https://github.com/tribdz',
      ariaLabel: 'Open Tran Tri Binh GitHub profile',
    },
    {
      label: 'LinkedIn',
      href: 'https://www.linkedin.com/in/quoc-hung-nham/',
      ariaLabel: 'Open Nham Quoc Hung LinkedIn profile',
    },
    {
      label: 'Email',
      href: 'mailto:nhamhung.gttn@gmail.com',
      ariaLabel: 'Email Nham Quoc Hung',
    },
  ],
} satisfies Profile

export const hero = {
  eyebrow: '<engineer id="nham-quoc-hung" />',
  statusBadges: ['SYSTEM STATUS: BUILDING', 'DATA | SOFTWARE | MENTORSHIP'],
  headline: 'Building reliable data pipelines and scalable data platforms.',
  highlightedPhrase: 'data pipelines',
  intro: profile.summary,
  stats: [
    { value: '4+ Years', label: 'Experience' },
    { value: 'Data + Teaching', label: 'Focus' },
    { value: 'Everything Data-related', label: 'Coverage' },
  ],
  primaryAction: {
    label: 'View Projects',
    sectionId: 'projects',
    ariaLabel: 'Scroll to selected projects',
  },
  secondaryAction: {
    label: 'Contact',
    sectionId: 'contact',
    ariaLabel: 'Scroll to contact section',
  },
  stackHighlights: ['Big Data', 'Data Analytics', 'Data Science', 'Data Engineering', 'Machine Learning', 'Deep Learning'],
} satisfies HeroSection
