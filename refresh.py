from playwright.sync_api import sync_playwright
from pathlib import Path

def main(url: str, output_dir: str = ".", body_attr_name: str = "data-bs-theme", body_attr_value: str = "dark"):
    output_path = Path(output_dir)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={"width": 1240, "height": 700},
            device_scale_factor=2,
        )
        page = context.new_page()
        
        print(f"Opening {url}...")
        page.goto(url, wait_until="networkidle")
        
        original_path = output_path / "light.png"
        print("Taking original screenshot...")
        page.screenshot(
            path=str(original_path),
            full_page=True,
            scale="device"
        )
        print(f"Original saved: {original_path}")
        
        print(f"Adding attribute {body_attr_name}='{body_attr_value}' to <body>...")
        page.evaluate(f"""
            document.body.setAttribute("{body_attr_name}", "{body_attr_value}");
        """)
        
        page.wait_for_timeout(500)
        
        modified_path = output_path / "dark.png"
        print("Taking modified screenshot...")
        page.screenshot(
            path=str(modified_path),
            full_page=True,
            scale="device"
        )
        print(f"Modified saved: {modified_path}")
        
        browser.close()
    
    print("Done!")

main("https://mumarshahbaz.com/readme.html")