# Django Wagtail Website

A modern blog website built with **Django**, **Wagtail CMS**, **Django Templates**, **Tailwind CSS**, **HTMX**, and **Alpine.js**.

The project is designed for editorial websites that publish **articles, books, images, rich content, and media**, with a foundation that can later be extended with e-commerce features such as online ordering, payments, and protected digital downloads.

The current UI is **RTL-ready with an Arabic-oriented base layout**, while the content model and application structure can be adapted to other languages and use cases.

## Features

- Wagtail CMS administration interface
- Article publishing with images and rich structured content
- Book catalog with cover image, price, format, ISBN, and optional PDF document
- Homepage with the latest articles and books
- Site branding configurable from Wagtail settings
- Configurable header navigation from the Wagtail admin
- Site search using Wagtail's database search backend
- Dynamic search results with HTMX
- Responsive mobile navigation with Alpine.js
- Tailwind CSS frontend compiled with Vite
- PostgreSQL database support
- Docker Compose development environment

> **Note:** the project currently provides a book catalog and a basic email-based order action. Payment processing and secure paid-download workflows are not implemented yet.

---

## Technology Stack

| Layer | Technology |
| --- | --- |
| Backend | Python 3.12, Django 5.x |
| CMS | Wagtail 6.x |
| Database | PostgreSQL 16 |
| Templates | Django Templates |
| CSS | Tailwind CSS 4 |
| Frontend build | Vite 8 |
| Server interactions | HTMX 2 |
| Client-side UI | Alpine.js 3 |
| Static files | WhiteNoise |
| Containers | Docker, Docker Compose |

HTMX and Alpine.js are loaded from a CDN in the base template. Tailwind CSS is compiled locally by Vite.

---

## Architecture

The application follows a traditional server-rendered Django/Wagtail architecture.

```text
                         ┌──────────────────────┐
                         │       Browser        │
                         │                      │
                         │ Tailwind / HTMX /    │
                         │ Alpine.js            │
                         └──────────┬───────────┘
                                    │ HTTP
                                    ▼
                         ┌──────────────────────┐
                         │    Django / Wagtail  │
                         │                      │
                         │ Django Templates     │
                         │ Wagtail Pages        │
                         │ Wagtail Admin        │
                         └──────────┬───────────┘
                                    │
                  ┌─────────────────┼─────────────────┐
                  │                 │                 │
                  ▼                 ▼                 ▼
             apps/blog         apps/books        apps/search
             apps/home         apps/core          HTMX views
                  │                 │                 │
                  └─────────────────┼─────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     PostgreSQL       │
                         └──────────────────────┘
```

The frontend build is handled independently by the `frontend` Docker service:

```text
static/src/app.css
        │
        ▼
Tailwind CSS + Vite
        │
        ▼
static/dist/assets/app.css
        │
        ▼
Django templates
```

---

## Project Structure

```text
.
├── apps/
│   ├── blog/              # Article index and article pages
│   ├── books/             # Book catalog and book pages
│   ├── core/              # Shared StreamField blocks and site settings
│   ├── home/              # Homepage and latest-content queries
│   └── search/            # Wagtail search + HTMX partial responses
│
├── config/
│   ├── settings/
│   │   ├── base.py        # Shared settings
│   │   ├── dev.py         # Development settings
│   │   └── prod.py        # Production security settings
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── blocks/            # StreamField block templates
│   ├── blog/
│   ├── books/
│   ├── home/
│   ├── includes/
│   └── search/
│
├── static/
│   ├── images/
│   └── src/app.css        # Tailwind source stylesheet
│
├── scripts/
│   ├── create-admin.sh
│   └── start-dev.sh
│
├── Dockerfile
├── docker-compose.yml
├── package.json
├── requirements.txt
├── vite.config.js
└── manage.py
```

Generated directories such as `staticfiles/`, `static/dist/`, `node_modules/`, media uploads, local databases, and Python caches are excluded from Git through `.gitignore`.

---

## Wagtail Content Model

### Home page

`HomePage` provides:

- optional introduction text
- optional hero image
- reusable rich content through `StreamField`
- the 3 latest published books
- the 6 latest published articles

### Articles

`BlogIndexPage` acts as the article listing page.

Each `BlogPage` supports:

- publication date
- introduction
- main image
- structured rich content
- Wagtail search indexing

### Books

`BooksIndexPage` lists published books.

Each `BookPage` supports:

- introduction
- cover image
- price
- book type: ebook, printed book, or both
- ISBN
- optional Wagtail document/PDF
- structured rich content
- Wagtail search indexing

### Reusable content blocks

The shared blocks in `apps/core/blocks.py` include:

- heading
- rich text paragraph
- image with caption
- quote
- video link

---

## Requirements

### Docker workflow — recommended

You only need:

- Docker
- Docker Compose v2

Python, PostgreSQL, and Node.js are provided by the containers.

### Local workflow

If you run the services directly on your machine, use:

- Python 3.12+
- PostgreSQL
- Node.js `^20.19.0` or `>=22.12.0` for the current Vite version
- npm

---

## Getting Started with Docker

### 1. Clone the repository

```bash
git clone https://github.com/ahmabrk/django-wagtail-website.git
cd django-wagtail-website
```

### 2. Create the environment file

```bash
cp .env.example .env
```

For Docker Compose, make sure the database URL points to the Compose database service (`db`). With the default values from `docker-compose.yml`:

```env
DJANGO_SETTINGS_MODULE=config.settings.dev
DJANGO_SECRET_KEY=change-me-in-production
DJANGO_DEBUG=1
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

POSTGRES_DB=wagtail
POSTGRES_USER=wagtail
POSTGRES_PASSWORD=wagtail
DATABASE_URL=postgresql://wagtail:wagtail@db:5432/wagtail
```

Do not commit your `.env` file.

### 3. Build and start the application

```bash
docker compose up --build
```

The `web` container automatically runs migrations and starts the Django development server. The `frontend` container installs the npm dependencies and continuously rebuilds the Tailwind CSS bundle with Vite.

### 4. Open the application

Public website:

```text
http://localhost:8000/
```

Wagtail administration:

```text
http://localhost:8000/admin/
```

Django administration:

```text
http://localhost:8000/django-admin/
```

Search:

```text
http://localhost:8000/search/
```

---

## Create an Administrator

With the containers running:

```bash
docker compose exec web ./scripts/create-admin.sh
```

or:

```bash
docker compose exec web python manage.py createsuperuser
```

Then sign in at:

```text
http://localhost:8000/admin/
```

---

## Initial Wagtail Setup

After signing in to Wagtail:

1. Open **Pages**.
2. Create or edit the home page.
3. Add a `BlogIndexPage`, typically with the slug `blog`.
4. Add `BlogPage` children below the blog index.
5. Add a `BooksIndexPage`, typically with the slug `livres`.
6. Add `BookPage` children below the books index.
7. Publish the pages.

The default header links point to:

```text
/blog/
/livres/
```

The menu labels and URLs can be changed from the Wagtail settings interface without modifying the template.

---

## Site Branding

Branding is managed through Wagtail settings.

Go to:

```text
Wagtail Admin → Settings → Site branding
```

You can configure:

- site name
- SVG logo
- subtitle

If no custom logo is configured, the application uses:

```text
static/images/default-logo.svg
```

The main menu can also be configured in Wagtail through the `HeaderMenuSettings` site setting.

---

## Frontend Development

The main Tailwind source file is:

```text
static/src/app.css
```

Vite writes the compiled stylesheet to:

```text
static/dist/assets/app.css
```

With Docker Compose, the frontend service runs Vite in watch mode automatically:

```bash
docker compose up frontend
```

To create a one-time production build:

```bash
docker compose run --rm frontend npm run build
```

If you work without Docker:

```bash
npm ci
npm run dev
```

or:

```bash
npm run build
```

---

## HTMX and Alpine.js

### HTMX

HTMX is used for lightweight server-driven interactions without introducing a separate JavaScript application.

The current example is the search page. Typing in the search field sends an HTMX request and Django returns only the results partial:

```text
templates/search/partials/results.html
```

### Alpine.js

Alpine.js handles small client-side UI interactions. The current example is the responsive mobile navigation menu in:

```text
templates/includes/header.html
```

---

## Search

The project uses Wagtail's database search backend:

```python
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}
```

Searchable fields currently include article and book introductions and body content.

The implementation is intentionally simple and can later be replaced with a more advanced search backend when needed.

---

## Useful Development Commands

Start all services:

```bash
docker compose up
```

Start in the background:

```bash
docker compose up -d
```

Rebuild containers:

```bash
docker compose up --build
```

View Django logs:

```bash
docker compose logs -f web
```

Open a shell in the Django container:

```bash
docker compose exec web bash
```

Create migrations:

```bash
docker compose exec web python manage.py makemigrations
```

Apply migrations:

```bash
docker compose exec web python manage.py migrate
```

Run Django checks:

```bash
docker compose exec web python manage.py check
```

Open the Django shell:

```bash
docker compose exec web python manage.py shell
```

Stop the project:

```bash
docker compose down
```

Remove containers and the local PostgreSQL volume:

```bash
docker compose down -v
```

> `docker compose down -v` permanently removes the local database volume.

---

## Running Without Docker

Create and activate a virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Install Python dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Install frontend dependencies:

```bash
npm ci
```

Create your environment file:

```bash
cp .env.example .env
```

Update `DATABASE_URL` so it points to your local PostgreSQL instance, then run:

```bash
python manage.py migrate
python manage.py createsuperuser
npm run build
python manage.py runserver
```

---

## Production Notes

Production-specific security options are defined in:

```text
config/settings/prod.py
```

A production deployment should at minimum:

- set `DJANGO_SETTINGS_MODULE=config.settings.prod`
- use a strong, unique `DJANGO_SECRET_KEY`
- set `DJANGO_DEBUG=0`
- configure the real `DJANGO_ALLOWED_HOSTS`
- use HTTPS
- store secrets outside the repository
- use a production-grade application server and reverse proxy
- configure PostgreSQL backups
- configure persistent media storage
- review static file hosting for the deployment environment
- restrict access to paid digital files before enabling purchases
- configure CSRF/trusted-origin settings where required by the deployment topology

The included production settings enable secure cookies, HTTPS redirection, HSTS, and additional browser security headers.

---

## Roadmap

Possible next steps include:

- article categories and tags
- richer YouTube/Vimeo embeds
- SEO metadata, Open Graph, sitemap, and robots.txt
- shopping cart and order management
- Stripe or PayPal integration
- protected downloads for paid ebooks
- customer accounts
- transactional email
- advanced PostgreSQL full-text search, Elasticsearch, or Meilisearch
- automated tests
- CI/CD with GitHub Actions
- object storage for production media
- multilingual content support

---

## Contributing

Contributions, bug reports, and improvement ideas are welcome.

A typical contribution workflow is:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Run the Django checks and relevant tests.
5. Commit your changes with a clear message.
6. Push the branch to your fork.
7. Open a Pull Request.

For significant changes, consider opening an Issue first to discuss the proposed approach.

---

## License

This repository does not currently include an open-source license.

If the project is intended for open-source reuse and external contributions, add an explicit license such as MIT, Apache-2.0, or another license appropriate for your goals.
