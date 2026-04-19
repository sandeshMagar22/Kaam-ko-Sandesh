# Kaam ko Sandesh

Kaam ko Sandesh is a high-end career intelligence dashboard designed for the Nepal tech community. It provides real-time job market transparency by consolidating data from multiple sources and enriching it with salary benchmarks and insider community intel.

This project was built upon an open-source data extraction engine, which was then extended with a premium UI/UX, advanced filtering capabilities, and a dedicated career resources arsenal.

## Features

- **Consolidated Market Intel**: Real-time job listings from major tech players like eSewa, Fusemachines, Leapfrog, and more.
- **Hidden Salary Benchmarks**: Integrated community-sourced salary ranges for better negotiation power.
- **Insider Insights**: Verified "gossips" and community feedback about company culture and pressure levels.
- **Advanced Taxonomy**: Filter by specialization (Engineering, Data, Design, etc.) and specific intelligence criteria.
- **Career Arsenal**: tactical resources for resume engineering and interview playbooks tailored to the local market.

## How It Works

1. **Extraction**: A multi-threaded scraping layer targets company career portals and industry boards.
2. **Standardization**: Raw data is processed into a unified JSON schema, normalizing roles and locations.
3. **Enrichment**: A separate intelligence layer cross-references listings with public discourse and community platforms to attach salary and culture context.
4. **Visualization**: A React-based, glassmorphic dashboard presents the intelligence with fluid animations and responsive design.

## Technical Stack

- **Dashboard**: React, Vite, Framer Motion, Lucide Icons, Vanilla CSS
- **Data Engine**: Python, Selenium, Pandas
- **Styling**: Premium Glassmorphism, Mesh Gradients, Grain texture systems

## Deployment

The application is architected for high performance and is hosted on Vercel for the global community. Visit the live site at [kamkosandesh.vercel.app](https://kamkosandesh.vercel.app).

---

*This project was inspired by open-source data engineering patterns and significantly enhanced to provide a premium user experience.*
