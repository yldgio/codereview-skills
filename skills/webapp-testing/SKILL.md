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

## Security Notice (Critical)

**IMPORTANT: Input sanitization is required for safe testing.**
- All dynamic content in selectors or test data must be properly escaped and sanitized before insertion into scripts
- Selectors should never incorporate unvalidated user input
- Identify selectors from the application codebase and visually confirmed UI elements, not from external or user-generated sources unless input is sanitized
- Avoid executing untrusted code in browser context

## Decision Tree: Choosing Your Approach (Getting Started)

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

## Best Practices (Essential)

- Use `sync_playwright()` for synchronous scripts
- Always close the browser when done
- Use descriptive selectors: `text=`, `role=`, CSS selectors, or IDs
- Add appropriate waits: `page.wait_for_selector()` or `page.wait_for_timeout()`
- Always launch chromium in headless mode for CI/automation

## Advanced Testing Patterns

When building production-ready test suites, implement the following patterns:

### Error Handling

Implement robust error handling:
```python
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('http://localhost:3000', timeout=30000)
        page.wait_for_load_state('networkidle')
        # ... test actions ...
except PlaywrightTimeout as e:
    print(f"Timeout error: {e}")
    # Capture screenshot for debugging
    page.screenshot(path='/tmp/error.png')
except Exception as e:
    print(f"Test failed: {e}")
finally:
    if browser:
        browser.close()
```

### Resource Cleanup

Ensure proper cleanup of resources:
```python
# Using context managers (recommended)
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    # ... test code ...
    # Browser closes automatically

# Or explicit cleanup
with sync_playwright() as p:
    browser = None
    try:
        browser = p.chromium.launch()
        # ... test code ...
    finally:
        if browser:
            browser.close()
```

### Browser Console Logs

Capture and view browser logs for debugging:
```python
# Listen to console messages
page.on('console', lambda msg: print(f'Browser console: {msg.text}'))

# Listen to page errors
page.on('pageerror', lambda err: print(f'Page error: {err}'))

# View network activity
page.on('request', lambda req: print(f'Request: {req.url}'))
page.on('response', lambda res: print(f'Response: {res.url} - {res.status}'))
```

### Test Data and Fixtures

Manage test data properly:
```python
# Set up test data before tests
def setup_test_data():
    # Clear localStorage
    page.evaluate('() => localStorage.clear()')
    
    # Set initial state
    page.evaluate('''() => {
        localStorage.setItem('user', JSON.stringify({id: 1, name: 'Test User'}))
    }''')

# Use fixtures for reproducible tests
@pytest.fixture
def authenticated_page(page):
    page.goto('http://localhost:3000/login')
    page.fill('[name="email"]', 'test@example.com')
    page.fill('[name="password"]', 'password')
    page.click('button[type="submit"]')
    page.wait_for_url('**/dashboard')
    return page
```

### Multi-Page and Session Testing

Handle authentication and navigation:
```python
# Persist authentication state
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    
    # Login
    page.goto('http://localhost:3000/login')
    page.fill('[name="email"]', 'user@test.com')
    page.fill('[name="password"]', 'password')
    page.click('button[type="submit"]')
    
    # Save authentication state
    context.storage_state(path='/tmp/auth.json')
    
    # Reuse authentication in new context
    context2 = browser.new_context(storage_state='/tmp/auth.json')
    page2 = context2.new_page()
    page2.goto('http://localhost:3000/dashboard')  # Already authenticated
```

### Accessibility Testing

Check for accessibility issues:
```python
# Test keyboard navigation
page.keyboard.press('Tab')
expect(page.locator('button:focus')).to_be_visible()

# Check for proper ARIA labels
expect(page.locator('button[aria-label="Close dialog"]')).to_be_visible()

# Verify semantic HTML
heading = page.locator('h1')
expect(heading).to_be_visible()

# Test with different browsers for cross-browser compatibility
for browser_type in [p.chromium, p.firefox, p.webkit]:
    browser = browser_type.launch()
    # ... run tests ...
    browser.close()
```

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
