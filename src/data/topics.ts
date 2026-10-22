export const TOPIC_IDS = [
  'networking', 'servers', 'security', 'cloud', 'odoo', 'automation', 'database', 'interviews',
] as const;

export type TopicId = (typeof TOPIC_IDS)[number];

export const TOPICS: Record<TopicId, { label: string; short: string; description: string }> = {
  networking: {
    label: 'Networking', short: 'Networking',
    description: 'VLANs, routing, firewall policies, DNS, DHCP, switching, access points, LACP and troubleshooting.',
  },
  servers: {
    label: 'Servers & Proxmox', short: 'Servers',
    description: 'VM design, backup planning, storage checks, Dell iDRAC, Linux server setup and restore procedures.',
  },
  security: {
    label: 'Security', short: 'Security',
    description: 'Firewall rules, endpoint protection, Wazuh SIEM, Suricata IDS, hardening, USB control and data protection.',
  },
  cloud: {
    label: 'Cloud & Microsoft 365', short: 'Cloud',
    description: 'M365 administration, Entra ID, MFA, mail security, Azure basics, domains and account protection.',
  },
  odoo: {
    label: 'Odoo & ERP', short: 'Odoo & ERP',
    description: 'Odoo Online and Community, approvals, record rules, CRM customization, timesheets and API integration.',
  },
  automation: {
    label: 'Automation', short: 'Automation',
    description: 'n8n workflows, Teams notifications, Odoo API automation, scheduled reminders and reporting.',
  },
  database: {
    label: 'Database & Storage', short: 'Database',
    description: 'SQL, joins, indexes, PostgreSQL, backups, NAS, RAID concepts and capacity planning.',
  },
  interviews: {
    label: 'Technical Interviews', short: 'Interviews',
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
