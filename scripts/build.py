import os

def build():
    if not os.path.exists('dist'): os.makedirs('dist')

    with open('css/luxury_style.css', 'r') as f: css = f.read()
    with open('components/header.html', 'r') as f: header = f.read()
    with open('components/footer.html', 'r') as f: footer = f.read()
    with open('template.xml', 'r') as f: template = f.read()

    final = template.replace('/* CSS_HOLDER */', css)
    final = final.replace('<!-- HEADER_HOLDER -->', header)
    final = final.replace('<!-- FOOTER_HOLDER -->', footer)

    with open('dist/final_theme.xml', 'w') as f: f.write(final)
    print("✅ Build Complete: dist/final_theme.xml")

if __name__ == "__main__": build()