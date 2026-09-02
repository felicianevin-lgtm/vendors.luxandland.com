import json, re, html

src = open(r'C:\Users\felic\Desktop\vendors-luxandland\index.html', encoding='utf-8').read()
m = re.search(r'const DATA = (\[.*?\]);\n', src, re.S)
DATA = json.loads(m.group(1))
total = sum(len(v) for _, v in DATA)

def esc(s): return html.escape(s)

cats = []
for cat, vendors in DATA:
    rows = ''
    for v in vendors:
        contact = esc(v[2] if len(v) == 3 else (v[1] if len(v) > 1 else ''))
        rows += f'<div class="v"><span class="n">{esc(v[0])}</span><span class="dots"></span><span class="p">{contact}</span></div>'
    cats.append(f'<section class="cat"><h2>{esc(cat)}</h2>{rows}</section>')

body = '\n'.join(cats)

page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<title>Trusted Vendors</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500&family=Jost:wght@300;400;500&display=swap">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  @page {{ size: letter; margin: 0.5in 0.6in 0.55in; }}
  body {{ background:#fff; color:#1E1B17; font-family:'Jost',sans-serif; font-weight:300;
         -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
  header {{ text-align:center; margin-bottom: 11pt; }}
  .eyebrow {{ font-family:'Montserrat',sans-serif; font-weight:500; font-size:8pt; letter-spacing:.38em; text-indent:.38em; color:#1E1B17; }}
  h1 {{ font-family:'Cormorant Garamond',Georgia,serif; font-weight:500; font-size:30pt; letter-spacing:.03em; margin-top:5pt; }}
  .credo {{ font-family:'Cormorant Garamond',serif; font-style:italic; font-size:10.5pt; color:#6E675C; margin-top:5pt; }}
  .credo b {{ color:#A08C63; font-weight:500; }}
  .rule {{ width:1.5in; height:.75pt; background:#C9BB9C; margin:9pt auto 0; }}

  .cols {{ columns:2; column-gap:.42in; }}
  .cat {{ break-inside:avoid; margin-bottom:5.5pt; }}
  .cat h2 {{ display:flex; align-items:center; gap:7pt; font-family:'Montserrat',sans-serif; font-weight:500;
             font-size:7pt; letter-spacing:.22em; text-transform:uppercase; color:#A08C63; margin-bottom:2pt; }}
  .cat h2::after {{ content:''; flex:1; height:.6pt; background:#E5DFD2; }}
  .v {{ display:flex; align-items:baseline; gap:5pt; padding:.7pt 0; font-size:8.2pt; }}
  .v .n {{ color:#1E1B17; }}
  .v .dots {{ flex:1; border-bottom:.6pt dotted #D9D2C2; transform:translateY(-2pt); }}
  .v .p {{ color:#6E675C; white-space:nowrap; font-variant-numeric:tabular-nums; }}

  footer {{ margin-top:12pt; border-top:.6pt solid #E5DFD2; padding-top:8pt; text-align:center; break-inside:avoid; }}
  .agent {{ font-family:'Montserrat',sans-serif; font-weight:500; font-size:8.5pt; letter-spacing:.3em; text-indent:.3em; text-transform:uppercase; }}
  .title {{ font-family:'Montserrat',sans-serif; font-size:6pt; letter-spacing:.3em; text-indent:.3em; text-transform:uppercase; color:#A08C63; margin-top:3pt; }}
  .contact {{ font-size:8pt; color:#6E675C; margin-top:4pt; }}
  .disclaimer {{ font-size:6.6pt; line-height:1.5; color:#9A9182; max-width:6in; margin:6pt auto 0; }}
</style></head><body>
<header>
  <div class="eyebrow">CINDY LITZINGER &middot; LUXURY AND LAND &middot; EXP REALTY</div>
  <h1>Trusted Vendors</h1>
  <p class="credo">How did these vendors get on the list? <b>Reliable communication and ethical performance.</b></p>
  <div class="rule"></div>
</header>
<div class="cols">
{body}
</div>
<footer>
  <div class="agent">Cindy Litzinger</div>
  <div class="title">REALTOR&reg; &middot; Luxury Real Estate &middot; eXp Realty</div>
  <div class="contact">805.478.1412 &middot; cindy@luxandland.com &middot; vendors.luxandland.com</div>
  <p class="disclaimer">Buyers &amp; Sellers: make your selections independently. These professionals do not and cannot compensate me &mdash; directly or indirectly &mdash; in exchange for my endorsement.</p>
</footer>
</body></html>"""

open('vendor_print.html', 'w', encoding='utf-8').write(page)
print('categories:', len(DATA), '| vendors:', total)
