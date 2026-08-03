# Deploy and Host Docling Serve on Railway

## About Hosting Docling Serve

Docling Serve exposes Docling's document understanding and conversion pipelines through synchronous and asynchronous REST APIs and an optional web UI. This template deploys stable CPU-only version 1.29.0 with generated API-key protection and bounded production defaults.

Authenticate conversion requests with `X-Api-Key: <DOCLING_SERVE_API_KEY>`.

## Common Use Cases

- Convert PDF, DOCX, PPTX, HTML, images, Markdown, and spreadsheets
- Extract structured Markdown, JSON, text, HTML, and DocTags
- Add document conversion to ingestion and retrieval pipelines

## Dependencies for Docling Serve Hosting

### Deployment Dependencies

- One CPU-only Docling Serve service
- Railway managed HTTPS
- Sufficient memory and CPU for selected document pipelines

### Implementation Details

The service is stateless. Readiness waits for model loading and the local orchestrator. Generated API-key auth protects conversion routes. Remote services, external plugins, custom remote model configs, and verbose error details are disabled. Requests are bounded to 20 MiB, 50 pages, and a 300-second synchronous wait.

Health and metrics endpoints remain public by upstream design. Submitted documents and temporary results are not durable.

## Why Deploy Docling Serve on Railway?

Railway provides managed HTTPS, generated API credentials, health-checked model startup, resource metrics, and Git-driven rollouts for document conversion workloads.
