from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.pixelssuite.com/chat-translator")
    time.sleep(3)
    
    # Type test input
    input_box = page.locator('textarea').first
    input_box.fill("mama yanawa")
    time.sleep(1)
    
    # Click transliterate button
    page.get_by_role("button", name="Transliterate").click()
    time.sleep(5)
    
    # Try different selectors
    selectors = [
        "textarea[placeholder*='Sinhala']",
        "div.bg-slate-50",
        ".output",
        "textarea >> nth=1",
        "div[class*='output']",
        "div[class*='card'] textarea",
    ]
    
    for sel in selectors:
        try:
            el = page.locator(sel).first
            if el.count() > 0:
                val = el.inner_text() or el.input_value() or el.text_content()
                print(f"FOUND: {sel} => '{val[:50]}'")
            else:
                print(f"NOT FOUND: {sel}")
        except Exception as e:
            print(f"ERROR {sel}: {e}")
    
    # Get all textareas
    print("\n--- ALL TEXTAREAS ---")
    tas = page.locator("textarea").all()
    for i, ta in enumerate(tas):
        try:
            print(f"Textarea {i}: placeholder='{ta.get_attribute('placeholder')}' value='{ta.input_value()[:30]}'")
        except:
            pass
    
    input("Press Enter to close...")
    browser.close()
