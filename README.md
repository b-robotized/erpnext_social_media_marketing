# Social Media Marketing

CRM-integrated Social Media tracking for ERPNext.

## Installation

```bash
bench get-app erpnext_social_media_marketing https://github.com/b-robotized/erpnext_social_media_marketing
bench install-app erpnext_social_media_marketing
```

## Testing

### 1. Unit Tests (Logic Verification)
These tests check the Python code logic in isolation. They are fast and run locally or in CI without a full Frappe environment.

**Run locally:**
```bash
docker run --rm -v $(pwd):/app -w /app python:3.14-slim \
    bash -c "pip install -e . pytest && pytest erpnext_social_media_marketing/erpnext_social_media_marketing/erpnext_social_media_marketing/tests"
```

### 2. Integration Tests (Installation Verification)
These tests verify that the app can be successfully installed into a real ERPNext site using Docker Compose.

**Automated Management Script:**
I have provided a helper script to manage the lifecycle of your test environment.

1.  **Start Clean & Run**:
    This will clean up previous runs, build the image, start the containers, and show the installation logs.
    ```bash
    ./manage.sh
    ```

2.  **Clean Up Only**:
    This will stop containers and remove all volumes and images created by this test, freeing up space.
    ```bash
    ./manage.sh --clean-only
    ```

**Manual Commands:**
If you prefer running commands manually:
```bash
cd docker
docker compose up -d --build
docker compose logs -f configurator
```

## License

MIT
