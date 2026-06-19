import os, re

patterns = [
    # Double quote variants
    (r' ?<a href="\./operating\.html">Operating</a>', ''),
    (r'<a href="\./operating\.html">Operating</a> ?', ''),
    (r'<a href="\./operating\.html">Operating</a>', ''),
    # Single quote variants
    (r" ?<a href='\./operating\.html'>Operating</a>", ''),
    (r"<a href='\./operating\.html'>Operating</a> ?", ''),
    (r"<a href='\./operating\.html'>Operating</a>", ''),
    # Secondary link variant (double quote)
    (r'<a class="secondary" href="\./operating\.html">[^<]*</a>', ''),
    # Secondary link variant (single quote)
    (r"<a class='secondary' href='\./operating\.html'>[^<]*</a>", ''),
]

count = 0
modified_files = []
for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, 'r') as f:
            content = f.read()
        original = content
        for pat, repl in patterns:
            content = re.sub(pat, repl, content)
        if content != original:
            with open(fpath, 'w') as f:
                f.write(content)
            count += 1
            modified_files.append(fname)

print(f'Modified {count} files')

# Verify remaining (excluding operating.html itself)
remaining = []
for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for fname in files:
        if not fname.endswith('.html') or fname == 'operating.html':
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, 'r') as f:
            if 'operating.html' in f.read():
                remaining.append(fname)

print(f'Remaining refs (excl operating.html itself): {len(remaining)}')
if remaining:
    print('Files:', remaining)
