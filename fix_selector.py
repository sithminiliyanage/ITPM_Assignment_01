with open('test_automation/test_automation.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the broken selector first (restore original then fix properly)
content = content.replace(
    '.locator("textarea[placeholder*=\\"Sinhala\\"]").first',
    '.locator("textarea[placeholder*=\'Sinhala\']").first'
)

# Also fix the original selector if still present
content = content.replace(
    '.locator("div.bg-slate-50").first',
    '.locator("textarea[placeholder*=\'Sinhala\']").first'
)

with open('test_automation/test_automation.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Selector fixed successfully.")

# Verify
if "textarea[placeholder*='Sinhala']" in content:
    print("Verified: New selector is in place.")
else:
    print("WARNING: Selector may not have been replaced correctly.")
