# GSF-Factory 🏭

Welcome to the **Secondary Unmanned AI Blog Engine** for Good Samaritan Frontier.
This repository acts completely independently from the main GSF-Blog.

## 🚀 Overview
GSF-Factory is completely automated. Every single day, a cron job spins up an AI python script (`news_bot.py`), which:
1. Scrapes Japanese real estate, finance, and asset market RSS feeds.
2. Formats and translates the scraped output into professional multi-language (en, ko, ja) Markdown files.
3. Automatically pushes the output to `src/data/blog/[lang]/`.
4. Triggering Vercel to auto-deploy the latest news.

**ZERO user interaction is required.**

## ⚙️ Configuration
The automated bot relies on the `OPENAI_API_KEY` stored in the repository's GitHub Actions Secrets.
If the API key is not present, the bot will still run using mockup string outputs.

## 📁 Project Structure
- `.github/workflows/main.yml` : The Cron scheduler (runs daily at 22:00 UTC / 07:00 JST).
- `news_bot.py` : The brain of the Factory. Python parsing logic.
- `src/` : The Astro V5 frontend inherited from GSF-Blog to render the news visually.
