"""Molekit — gizlilik politikası + kullanım koşulları sayfası.
src/<dil>.html parçalarını tek sayfada birleştirir: legal/index.html (+ privacy.html, terms.html yönlendirmeleri).
Kullanım: python3 legal/build.py   (metni değiştirdikten sonra çalıştır)
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
LANGS = [  # kod, menüde görünen ad, sayfa başlığı
    ('en', 'English', 'Molekit — Privacy Policy & Terms of Use'),
    ('tr', 'Türkçe', 'Molekit — Gizlilik Politikası ve Kullanım Koşulları'),
    ('de', 'Deutsch', 'Molekit — Datenschutzerklärung & Nutzungsbedingungen'),
    ('es', 'Español', 'Molekit — Política de privacidad y Términos de uso'),
    ('fr', 'Français', 'Molekit — Politique de confidentialité et Conditions d’utilisation'),
    ('pt', 'Português (Brasil)', 'Molekit — Política de Privacidade e Termos de Uso'),
]
HTML_LANG = {'pt': 'pt-BR'}

mascot = open(os.path.join(HERE, 'mascot.svg'), encoding='utf-8').read()
mascot = re.sub(r'<\?xml.*?\?>|<metadata>.*?</metadata>|<!--.*?-->', '', mascot, flags=re.S).strip()
mascot = re.sub(r'<svg\b', '<svg class="mascot" aria-hidden="true" focusable="false"', mascot, count=1)

arts = []
for code, name, title in LANGS:
    body = open(os.path.join(HERE, 'src', f'{code}.html'), encoding='utf-8').read().strip()
    hidden = '' if code == 'en' else ' hidden'
    arts.append(f'<article lang="{HTML_LANG.get(code, code)}" data-lang="{code}" data-title="{title}"{hidden}>\n{body}\n</article>')

opts = ''.join(f'<option value="{c}">{n}</option>' for c, n, _ in LANGS)
codes = [c for c, _, _ in LANGS]

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{LANGS[0][2]}</title>
<meta name="description" content="Privacy Policy, Terms of Use and contact information for the Molekit game.">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='32' cy='36' r='22' fill='%23FF5A4E'/%3E%3Ccircle cx='14' cy='12' r='9' fill='%23fff' stroke='%231D2350' stroke-width='3'/%3E%3Ccircle cx='50' cy='12' r='9' fill='%23fff' stroke='%231D2350' stroke-width='3'/%3E%3C/svg%3E">
<style>
:root{{--bg:#F3F6FD; --paper:#FFFFFF; --ink:#1D2350; --muted:#5A6390; --line:#DCE3F2; --brand:#3D7BFF; --brand-ink:#1F5BE0; --chip:#E8EFFF}}
@media (prefers-color-scheme: dark){{:root{{--bg:#0E1426; --paper:#151C33; --ink:#E8EDFA; --muted:#9AA6C8; --line:#26304D; --brand:#6E9BFF; --brand-ink:#8FB2FF; --chip:#1D2747}}}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth; -webkit-text-size-adjust:100%}}
body{{margin:0; background:var(--bg); color:var(--ink); font:16px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif}}
a{{color:var(--brand-ink); text-underline-offset:2px}}
.top{{position:sticky; top:0; z-index:5; background:color-mix(in srgb, var(--bg) 88%, transparent); backdrop-filter:blur(10px); -webkit-backdrop-filter:blur(10px); border-bottom:1px solid var(--line)}}
.top .in{{max-width:820px; margin:0 auto; padding:10px 16px; display:flex; align-items:center; gap:12px}}
.brand{{display:flex; align-items:center; gap:8px; font-weight:800; font-size:18px; letter-spacing:-.01em; color:var(--ink); text-decoration:none; margin-right:auto}}
.brand .mascot{{width:34px; height:34px}}
.langsel{{display:flex; align-items:center; gap:6px; color:var(--muted); font-size:14px}}
select{{font:inherit; color:var(--ink); background:var(--paper); border:1px solid var(--line); border-radius:10px; padding:6px 10px; max-width:52vw}}
main{{max-width:820px; margin:0 auto; padding:24px 16px 64px}}
article{{background:var(--paper); border:1px solid var(--line); border-radius:20px; padding:28px clamp(18px, 5vw, 48px) 36px}}
.hero h1{{font-size:clamp(26px, 5vw, 36px); line-height:1.15; letter-spacing:-.02em; margin:0 0 6px}}
.meta{{color:var(--muted); margin:0 0 16px}}
.toc{{display:flex; flex-wrap:wrap; gap:8px; margin-bottom:8px}}
.toc a{{background:var(--chip); padding:6px 14px; border-radius:999px; text-decoration:none; font-weight:600; font-size:14px}}
section{{scroll-margin-top:72px; border-top:1px solid var(--line); margin-top:28px; padding-top:8px}}
h2{{font-size:24px; letter-spacing:-.01em; margin:18px 0 8px}}
h3{{font-size:17px; margin:22px 0 4px}}
p, li{{overflow-wrap:anywhere}}
ul{{padding-left:22px}} li{{margin:4px 0}}
.contact .card{{background:var(--chip); border-radius:14px; padding:16px 18px; line-height:1.6}}
footer{{text-align:center; color:var(--muted); font-size:13px; margin-top:24px}}
noscript article{{display:block}}
</style>
</head>
<body>
<div class="top"><div class="in">
  <a class="brand" href="#">{mascot}<span>Molekit</span></a>
  <label class="langsel"><span aria-hidden="true">🌐</span><select id="lang" aria-label="Language">{opts}</select></label>
</div></div>
<main>
{chr(10).join(arts)}
<footer>© 2026 Can Behran Kankul · <a href="mailto:avelio-info@gmail.com">avelio-info@gmail.com</a></footer>
</main>
<script>
(function () {{
  var LANGS = {codes!r};
  var sel = document.getElementById('lang');
  function pick() {{
    var q = new URLSearchParams(location.search).get('lang');
    if (q) q = q.toLowerCase().slice(0, 2);
    if (LANGS.indexOf(q) >= 0) return q;
    try {{ var s = localStorage.getItem('molekit-legal-lang'); if (LANGS.indexOf(s) >= 0) return s; }} catch (e) {{}}
    var nav = navigator.languages || [navigator.language || 'en'];
    for (var i = 0; i < nav.length; i++) {{ var c = String(nav[i]).toLowerCase().slice(0, 2); if (LANGS.indexOf(c) >= 0) return c; }}
    return 'en';
  }}
  function show(code, save) {{
    var arts = document.querySelectorAll('article[data-lang]');
    for (var i = 0; i < arts.length; i++) {{
      var on = arts[i].getAttribute('data-lang') === code;
      arts[i].hidden = !on;
      var secs = arts[i].querySelectorAll('[data-sid]');
      for (var j = 0; j < secs.length; j++) {{ if (on) secs[j].id = secs[j].getAttribute('data-sid'); else secs[j].removeAttribute('id'); }}
      if (on) {{ document.documentElement.lang = arts[i].lang; document.title = arts[i].getAttribute('data-title'); }}
    }}
    sel.value = code;
    if (save) {{
      try {{ localStorage.setItem('molekit-legal-lang', code); }} catch (e) {{}}
      var u = new URL(location.href); u.searchParams.set('lang', code);
      history.replaceState(null, '', u.pathname + u.search + u.hash);
    }}
  }}
  var all = document.querySelectorAll('article [id]');
  for (var k = 0; k < all.length; k++) all[k].setAttribute('data-sid', all[k].id);
  sel.addEventListener('change', function () {{ show(sel.value, true); }});
  show(pick(), false);
  if (location.hash) {{ var t = document.getElementById(location.hash.slice(1)); if (t) t.scrollIntoView(); }}
}})();
</script>
</body>
</html>
"""
open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(page)

# Kısa adresler: privacy.html → index.html#privacy, terms.html → index.html#terms (dil parametresi korunur)
for name, anchor in (('privacy', 'privacy'), ('terms', 'terms'), ('contact', 'contact')):
    open(os.path.join(HERE, f'{name}.html'), 'w', encoding='utf-8').write(f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Molekit</title>
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url=./#{anchor}">
<link rel="canonical" href="./#{anchor}">
<script>location.replace('./' + location.search + '#{anchor}');</script>
</head><body><a href="./#{anchor}">Molekit</a></body></html>
""")
print('ok', os.path.join(HERE, 'index.html'), os.path.getsize(os.path.join(HERE, 'index.html')), 'bytes')
