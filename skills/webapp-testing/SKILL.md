---
name: webapp-testing
description: Toolkit for interacting with and testing local web applications using Playwright. Use when verifying frontend functionality, debugging UI behavior, capturing browser screenshots, or viewing browser logs.
license: Apache-2.0
metadata:
  author: anthropic
  version: "1.0.0"
  source: https://github.com/anthropics/skills
---

# Web Application Testing

To test local web applications, write native Python Playwright scripts.

## Decision Tree: Choosing Your Approach

```
User task → Is it static HTML?
    ├─ Yes → Read HTML file directly to identify selectors
    │         ├─ Success → Write Playwright script using selectors
    │         └─ Fails/Incomplete → Treat as dynamic (below)
    │
    └─ No (dynamic webapp) → Is the server already running?
        ├─ No → Start server first, then write Playwright script
        │
        └─ Yes → Reconnaissance-then-action:
            1. Navigate and wait for networkidle
            2. Take screenshot or inspect DOM
            3. Identify selectors from rendered state
            4. Execute actions with discovered selectors
```

## Example: Basic Playwright Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://localhost:3000')
    page.wait_for_load_state('networkidle')  # CRITICAL: Wait for JS
    
    # Take screenshot for inspection
    page.screenshot(path='/tmp/inspect.png', full_page=True)
    
    # Find and click a button
    page.click('button:has-text("Submit")')
    
    browser.close()
```

## Reconnaissance-Then-Action Pattern

1. **Inspect rendered DOM**:
   ```python
   page.screenshot(path='/tmp/inspect.png', full_page=True)
   content = page.content()
   buttons = page.locator('button').all()
   ```

2. **Identify selectors** from inspection results

3. **Execute actions** using discovered selectors

## Common Pitfall

- **Don't** inspect the DOM before waiting for `networkidle` on dynamic apps
- **Do** wait for `page.wait_for_load_state('networkidle')` before inspection

## Best Practices

- Use `sync_playwright()` for synchronous scripts
- Always close the browser when done
- Use descriptive selectors: `text=`, `role=`, CSS selectors, or IDs
- Add appropriate waits: `page.wait_for_selector()` or `page.wait_for_timeout()`
- Always launch chromium in headless mode for CI/automation

## Selector Examples

```python
# By text content
page.click('text=Sign In')

# By role
page.click('role=button[name="Submit"]')

# By CSS selector
page.click('.submit-button')
page.click('#login-form button[type="submit"]')

# By test ID (recommended)
page.click('[data-testid="submit-btn"]')
```

## Assertions

```python
from playwright.sync_api import expect

# Check element is visible
expect(page.locator('.success-message')).to_be_visible()

# Check text content
expect(page.locator('h1')).to_have_text('Welcome')

# Check URL
expect(page).to_have_url('http://localhost:3000/dashboard')
```
