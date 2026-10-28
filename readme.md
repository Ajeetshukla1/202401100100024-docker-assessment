## Stage 3: Docker Image Security

### Before and After Comparison

| Metric | Before (`fest-backend:0.1`) | After (`fest-backend:0.2`) |
|---|---:|---:|
| OS vulnerabilities | 13,357 | 270 |
| OS HIGH vulnerabilities | 2,243 | 59 |
| OS CRITICAL vulnerabilities | 234 | 2 |
| Python package vulnerabilities | 24 | 20 |
| Python HIGH vulnerabilities | 6 | 8 |
| Python CRITICAL vulnerabilities | 0 | 0 |
| Image disk usage | 1.61 GB | 289 MB |

### Security Improvements

- Replaced the original Python 3.9 base image with `python:3.12.12-slim-bookworm`.
- Upgraded the operating-system packages during the build.
- Upgraded pip and the installed Python dependencies.
- Created a dedicated `appuser` account and configured the container to run as that non-root user.
- Reduced image disk usage by approximately 82%.

### Critical Vulnerability Check

Command:

```bash
trivy image --severity CRITICAL --ignore-unfixed --exit-code 1 fest-backend:0.2
```

Result: Passed with exit code `0`. No reportable CRITICAL vulnerabilities were found under the specified filters. The unfiltered scan still reported two OS-level CRITICAL vulnerabilities, so the image is not completely free of critical findings.

### Scan Reports

- Baseline report: `reports/trivy-before.txt`
- Hardened image report: `reports/trivy-after.txt`