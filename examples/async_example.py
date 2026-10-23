"""Run separately: python -m examples.async_example (start demo app first).

Do not call sync Playwright inside an asyncio loop. This standalone async
example is deliberately separate from the synchronous pytest suite.
"""

import argparse
import asyncio

from playwright.async_api import async_playwright, expect


async def main(browser_name="chromium", base_url="http://127.0.0.1:8765"):
    async with async_playwright() as playwright:
        browser = await getattr(playwright, browser_name).launch()
        try:
            context = await browser.new_context()
            page = await context.new_page()
            await page.goto(base_url + "/lab")
            await page.get_by_label("Full name", exact=True).fill("Archana")
            await expect(page.get_by_label("Full name", exact=True)).to_have_value("Archana")
            response = await context.request.get(base_url + "/health")
            assert response.status == 200
            await context.close()
        finally:
            await browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Standalone async Playwright example")
    parser.add_argument("--browser", choices=["chromium", "firefox", "webkit"], default="chromium")
    parser.add_argument("--base-url", default="http://127.0.0.1:8765")
    args = parser.parse_args()
    asyncio.run(main(args.browser, args.base_url))
