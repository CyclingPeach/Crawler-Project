from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Fill input[name="wd"]
    page.locator("input[name=\"wd\"]").fill("nba")

    # Press Enter
    page.locator("input[name=\"wd\"]").press("Enter")
    page.wait_for_url("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=nba&fenlei=256&rsv_pq=b321d273002fe08b&rsv_t=e75f5z3kxPeIUCaB%2FDN1AYWXKR4nxs%2Bap8NppAl0mSh5MAWeec9R%2FcyiGRQ&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=3&rsv_sug1=3&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=1276&rsv_sug4=1276")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
