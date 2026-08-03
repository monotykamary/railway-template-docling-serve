# Docling Serve on Railway

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/docling-serve?referralCode=ZqgrJ0)

Deploy the official CPU-only Docling Serve 1.29.0 image as an API-key-protected document conversion service.

The Deploy on Railway button is added after the published route is verified.

## Authentication

Send the generated `DOCLING_SERVE_API_KEY` in the `X-Api-Key` header. Health, readiness, version, and metrics endpoints remain public by upstream design; conversion endpoints require the key.

## Safety defaults

- CPU image pinned to the stable Linux/AMD64 digest
- Remote services, external plugins, custom VLM configs, and custom picture-description configs disabled
- Maximum 20 MiB per file, 50 pages per document, and 300 seconds for synchronous requests
- One Uvicorn worker and one local conversion worker sharing models
- Structured JSON logs and sanitized error details

This service is compute and memory intensive. Start with at least 8 GB RAM for common PDF workloads and monitor usage. It is stateless; submitted documents and results are temporary and single-use.

## Updating

Update the pinned image digest deliberately and repeat API-key rejection, markdown and PDF conversion, malformed-document rejection, readiness, model startup, and soak tests.

## Upstream

- Source: https://github.com/docling-project/docling-serve/tree/v1.29.0
- Release: https://github.com/docling-project/docling-serve/releases/tag/v1.29.0
- License: MIT

This repository contains Railway configuration and documentation. Docling Serve remains copyright its upstream contributors and is not affiliated with Railway.
