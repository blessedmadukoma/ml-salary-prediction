import pycodestyle

style_checker = pycodestyle.StyleGuide()

# Run PEP 8 check on multiple files
result = style_checker.check_files(['app.py'])

# Print result of PEP 8 style check
print(result.messages)
