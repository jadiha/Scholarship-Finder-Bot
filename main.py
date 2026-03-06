import json
import os
import yaml
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from scrapers.curated import CuratedScraper
from scrapers.engineers_canada import EngineersCanadaScraper
from filters import filter_and_score
from notifier import post_to_discord, generate_dashboard

load_dotenv()

SEEN_PATH = "seen.json"


def load_config() -> dict:
    with open("config.yaml") as f:
        return yaml.safe_load(f)


def load_seen() -> set:
    if not os.path.exists(SEEN_PATH):
        return set()
    with open(SEEN_PATH) as f:
        return set(json.load(f))


def save_seen(seen: set):
    with open(SEEN_PATH, "w") as f:
        json.dump(sorted(seen), f, indent=2)


def main():
    config = load_config()
    seen = load_seen()

    all_raw = []

    # Curated list needs no browser
    curated = CuratedScraper(config).scrape()
    print(f"  [CuratedScraper] found {len(curated)}")
    all_raw.extend(curated)

    # Engineers Canada needs a browser to follow detail page links
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        )
        ec = EngineersCanadaScraper(config).scrape(page)
        print(f"  [EngineersCanadaScraper] found {len(ec)}")
        all_raw.extend(ec)
        browser.close()

    print(f"Total raw: {len(all_raw)}")

    eligible = filter_and_score(all_raw, config)
    print(f"Eligible after filtering: {len(eligible)}")

    new = [s for s in eligible if s.id not in seen]
    print(f"New (not yet notified): {len(new)}")

    if new and config.get("notifications", {}).get("discord"):
        webhook = os.environ.get("DISCORD_WEBHOOK_URL")
        if webhook:
            post_to_discord(new, webhook)
            print(f"[Discord] Posted {len(new)} scholarships")
        else:
            print("[Discord] DISCORD_WEBHOOK_URL not set — skipping")

    if config.get("notifications", {}).get("github_pages"):
        generate_dashboard(eligible)

    for s in new:
        seen.add(s.id)
    save_seen(seen)

    print("Done.")


if __name__ == "__main__":
    main()
