SPEEDTEST PROJECT – TODO & ROADMAP

================================
PHASE 0: FOUNDATION (DONE)
================================
[✔] Define overall architecture (API-first)
[✔] Create clean repo structure
[✔] Setup Python virtual environment (venv)
[✔] Implement get_ip.py
    - Hostname
    - Local IP
    - Public IP
[✔] Establish client ↔ server communication
[✔] Verify real data transfer (localhost testing)

================================
PHASE 1: CORE CLI (FOUNDATION)
================================
[✔] Implement download_test.py
    - Streaming download
    - Measure time
    - Calculate Mbps
[ ] Implement upload_test.py
    - Streaming upload
    - Measure time
    - Calculate Mbps
[ ] Implement latency.py
    - HTTP-based ping
    - Multiple samples
    - Average latency (ms)
[ ] Create cli/main.py
    - Combine IP, latency, download, upload
    - Human-readable terminal output
    - Optional JSON output

================================
PHASE 2: SPEEDTEST SERVER (BACKEND)
================================
[✔] Create API server (Flask)
[✔] Implement /api/ping
[✔] Implement /api/download
[✔] Implement /api/upload
[✔] Implement /api/info (server-side IP)
[✔] Refactor APIs into versioned structure (/api/v1)
[ ] Move speed logic into services/speedtest.py
[ ] Add basic input validation
[ ] Add minimal server-side logging
[ ] Expand /api/info
    - ISP / ASN lookup (optional)

================================
PHASE 3: DOCKERIZATION & LOCAL DEV
================================
[ ] Create requirements.txt / pyproject.toml lock
[ ] Write Dockerfile for server
[ ] Create docker-compose.yml
[ ] Run server in container
[ ] Test CLI against Dockerized server
[ ] Add .env support

================================
PHASE 4: WEB INTERFACE (MVP)
================================
[ ] Create basic web layout
[ ] Implement API client (fetch layer)
[ ] Implement latency test in browser
[ ] Implement download test in browser
[ ] Implement upload test in browser
[ ] Display IP & ISP info
[ ] Show progress indicators
[ ] Display final results clearly

================================
PHASE 5: WEB POLISH & UX
================================
[ ] Real-time progress bars
[ ] Graphs (latency / throughput)
[ ] Error states & retries
[ ] Mobile-friendly layout (responsive)

================================
PHASE 6: MOBILE APP (FUTURE)
================================
[ ] Decide framework (React Native / Flutter)
[ ] Reuse existing backend APIs
[ ] Implement speedtest flow
[ ] Handle mobile-specific network behavior
[ ] Package Android / iOS builds

================================
PHASE 7: OBSERVABILITY & SCALE (OPTIONAL)
================================
[ ] Add Prometheus metrics
[ ] Add structured logging
[ ] Add request rate limiting
[ ] Add basic abuse protection

================================
PHASE 8: INFRA & DEPLOYMENT (OPTIONAL)
================================
[ ] Kubernetes manifests (dev/prod)
[ ] Ingress + TLS
[ ] Terraform cloud provisioning
[ ] CI/CD pipeline hardening

================================
PHASE 9: DOCUMENTATION & FINALIZATION
================================
[ ] Update main README.md
[ ] Add FILE_STRUCTURE.md
[ ] Add ARCHITECTURE.md
[ ] Add API documentation
[ ] Final Git cleanup
[ ] Tag v1.0 release
[ ] Optional: Publish Docker image
