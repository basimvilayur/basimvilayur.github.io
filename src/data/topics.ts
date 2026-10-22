export const TOPIC_IDS = [
  'networking', 'servers', 'security', 'cloud', 'odoo', 'automation', 'database', 'interviews',
] as const;

export type TopicId = (typeof TOPIC_IDS)[number];

export const TOPICS: Record<TopicId, { label: string; short: string; icon: string; color: string; description: string }> = {
  networking: {
    label: 'Networking', short: 'Networking', icon: '🌐', color: 'var(--c-net)',
    description: 'VLANs, routing, firewall policies, DNS, DHCP, switching, access points, LACP and troubleshooting.',
  },
  servers: {
    label: 'Servers & Proxmox', short: 'Servers', icon: '🖥️', color: 'var(--c-srv)',
    description: 'VM design, backup planning, storage checks, Dell iDRAC, Linux server setup and restore procedures.',
  },
  security: {
    label: 'Security', short: 'Security', icon: '🔐', color: 'var(--c-sec)',
    description: 'Firewall rules, endpoint protection, Wazuh SIEM, Suricata IDS, hardening, USB control and data protection.',
  },
  cloud: {
    label: 'Cloud & Microsoft 365', short: 'Cloud', icon: '☁️', color: 'var(--c-cld)',
    description: 'M365 administration, Entra ID, MFA, mail security, Azure basics, domains and account protection.',
  },
  odoo: {
    label: 'Odoo & ERP', short: 'Odoo & ERP', icon: '🧩', color: 'var(--c-erp)',
    description: 'Odoo Online and Community, approvals, record rules, CRM customization, timesheets and API integration.',
  },
  automation: {
    label: 'Automation', short: 'Automation', icon: '⚙️', color: 'var(--c-aut)',
    description: 'n8n workflows, Teams notifications, Odoo API automation, scheduled reminders and reporting.',
  },
  database: {
    label: 'Database & Storage', short: 'Database', icon: '🗄️', color: 'var(--c-db)',
    description: 'SQL, joins, indexes, PostgreSQL, backups, NAS, RAID concepts and capacity planning.',
  },
  interviews: {
    label: 'Technical Interviews', short: 'Interviews', icon: '🎯', color: 'var(--c-int)',
    description: 'System design, networking, Linux, databases, cloud, security questions and troubleshooting scenarios.',
  },
};

export const SITE = {
  name: 'Basim Mohammed',
  title: 'Basim Mohammed | Technical Notes',
  description: 'Practical IT notes on networking, servers, Proxmox, security, Microsoft 365, Odoo and automation by Basim Mohammed.',
  email: 'info@basimvilayur.com',
  linkedin: 'https://www.linkedin.com/in/basimvilayur/',
  x: 'https://x.com/basimvilayur',
  facebook: 'https://www.facebook.com/basimvilayur',
  instagram: 'https://www.instagram.com/basimvilayur/',
};
