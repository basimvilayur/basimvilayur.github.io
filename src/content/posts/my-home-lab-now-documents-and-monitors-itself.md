---
title: "My home lab now documents and monitors itself"
summary: "How I turned a half-finished network diagram into a self-maintaining source of truth with Rackpad: auto-discovery from Proxmox, the switch and the firewall, 46 health checks with Telegram alerts, and a VLAN plan with a rollback path."
date: 2026-10-26
category: networking
tags: ["HomeLab", "Rackpad", "Proxmox", "OPNsense", "SNMP", "Automation", "Monitoring"]
---

Over the past few days I turned a "mental map + half-finished diagram" home lab into a self-maintaining source of truth, using [Rackpad](https://github.com/Kobii-git/rackpad), an open-source, self-hosted inventory for racks, ports, cables, IPs and devices.

## Why it matters

In a lab or a small office, the real risk is rarely the hardware. It's not knowing what is connected where when something breaks, or when you need to change it. An inventory that is updated by hand is out of date within a week. So the goal was simple: **the inventory has to keep itself current.**

## What's in place now

### Full inventory
- Rack layout with the physical servers, firewall and PoE switch
- 30+ devices and 15 Proxmox VMs and containers, each linked to its host
- 6 networks, including the Tailscale tailnet and ZeroTier
- Wi-Fi access points, radios and SSIDs (home, guest with captive portal, extended)
- IP assignments, DHCP scopes and service links (web UIs, DNS, VPN)

### Auto-discovery every 15 minutes
A small Python sync runs on the Proxmox host and reads the real sources of truth:

- **Proxmox:** new VMs and containers appear automatically with CPU, RAM, disk, MAC address, bridge and IP. Deleted ones are flagged, never silently removed.
- **Switch (SNMP BRIDGE-MIB + LLDP):** the MAC address table becomes real cable records with labels like `SW1-P02 ↔ PVE-ENO1`. Move a cable and the record follows.
- **Firewall (SNMP IF-MIB + ARP):** port up/down, uplink cables, device presence on every network, and MAC + vendor for unknown devices.
- **Network scans:** new hosts on the server LAN are imported automatically; Wi-Fi devices wait in a review queue, already labelled with their manufacturer.

### Monitoring
46 health checks (ping, TCP and HTTP) cover the hypervisor, firewall, DNS, ERP, media services, internet and VPN, with **Telegram alerts** when something goes down and again when it recovers.

### Planning
A VLAN segmentation plan (servers, trusted, IoT, guest, voice, lab, management) is documented as *planned* networks, together with a switch port map, a firewall matrix, a risk register and a pre-migration checklist. The plan lives next to the live inventory, so nothing gets out of sync.

### Safety first
- Key-only access for automation, no shared passwords
- An out-of-band rescue port on the firewall
- Tailscale as a lockout-proof management path
- Automatic rollback for every risky network change

## The stack

| Area | Tools |
|---|---|
| Virtualisation | Proxmox VE 9 on a Lenovo System x3500 M5 |
| Firewall | OPNsense 26.7 |
| Switching | HPE Aruba 2530-24G-PoE+ |
| Wi-Fi | TP-Link Omada access point, Linksys on OpenWrt |
| Inventory | Rackpad (self-hosted, Docker) |
| Automation | Python, SNMP v2c, LLDP, Proxmox `pvesh`, cron |
| Remote access | Tailscale, ZeroTier |
| Alerts | Telegram |

## Three lessons

1. **Discover from the sources of truth** (hypervisor, switch, firewall), not from memory.
2. **Let automation create and update, but never delete.** Flag instead, and let a human decide.
3. **Plan network changes with a rollback path** before touching anything live.

## Next step

Executing the VLAN migration with zero lock-out risk, and updating the inventory as each step lands.
