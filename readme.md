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
## Stage 4: Docker Hub Release

**Docker Hub repository:** `ajeetshukla12/fest-backend`

Published tags:
- `ajeetshukla12/fest-backend:1.0.0`
- `ajeetshukla12/fest-backend:1.0`

**Image digest:**

`sha256:564ad147134f76d05affedeba993fe78ce43b3c45225fc2789429c7c86a09d5e`

Both tags were pushed successfully and point to the same image digest.
## Stage 5: Image Signing and Verification with Cosign

### Signed Image: Version 1.0.0

**Image:** `ajeetshukla12/fest-backend:1.0.0`

**Digest:**

`sha256:564ad147134f76d05affedeba993fe78ce43b3c45225fc2789429c7c86a09d5e`

The image was signed using Cosign and the private key `cosign.key`.

Verification was successful using `cosign.pub`. Cosign validated the image claims, verified the signature against the public key, and confirmed the transparency-log entry.

### Unsigned Image: Version 1.0.1

**Image:** `ajeetshukla12/fest-backend:1.0.1`

**Digest:**

`sha256:9dfa523860300f43f77021367c247b25c42fdadaef04a1bb12ddf7b79e0a38a5`

The image was pushed to Docker Hub without signing it.

The verification command:

```bash
cosign verify --key cosign.pub ajeetshukla12/fest-backend:1.0.1
```

returned:

```text
Error: no signatures found
```

This confirms that Cosign rejected the unsigned image.

### Key Management

- `cosign.key` is the private signing key and must remain secret.
- `cosign.pub` is the public verification key and can be committed to the repository.
- Private keys and passwords must never be committed to Git.