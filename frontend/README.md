# Handoff: BenoVet Institutional Page

## Overview
A single-page institutional site for BenoVet, a veterinary health brand (suínos/bovinos/equinos + pet line). Purpose: present the brand, founders, mission/values, and a product sampler, then drive traffic to the brand's NuvemShop e-commerce store (external link, not part of this page).

## About the Design Files
The file in this bundle (`design-reference.html`) is a **design reference prototype** built in plain HTML/CSS/JS (via a small internal component runtime — ignore the `<x-dc>`/`support.js` scaffolding, it's tooling-specific and not meant to ship). Treat it strictly as a **visual and behavioral reference**. The task is to recreate this design in the target codebase's actual stack (React, Vue, plain static site, etc. — whichever the project uses, or your best choice if none exists yet), using that stack's conventions, component structure, and asset pipeline.

## Fidelity
**High-fidelity.** Colors, typography, spacing, and copy are final as shown. Recreate pixel-close using the values below.

## Screens / Views
Single scrolling page, one view: **Institutional Home**.

### 1. Nav bar
- Full-width row, dark background `#0B0F17`, bottom border `1px solid rgba(255,255,255,.08)`.
- Padding: 24px 40px, flex row, space-between, wraps on narrow widths.
- Left: animated DNA symbol icon (134×202px box, see Interactions below).
- Center: nav links "Quem Somos" (#sobre), "Produtos" (#produtos), "Contato" (#contato) — Public Sans 500 20px, color `rgba(255,255,255,.72)`.
- Right: CTA button "Comprar na loja" — background `#00C2FF`, text `#0B0F17`, Public Sans 600 20px, padding 16px 28px, border-radius 8px.

### 2. Hero
- Full-bleed background image (`assets/hero-animals.png` — pigs/cattle/horse composite), `object-fit: cover`, min-height 520px.
- Left-to-right dark gradient overlay: `linear-gradient(90deg, rgba(11,15,23,.35) 0%, rgba(11,15,23,.15) 100%)`.
- Copy block (left-aligned, max-width 640px, padding 72px 64px):
  - Eyebrow pill: "CIÊNCIA · SAÚDE · RESULTADOS" — border `1px solid rgba(0,194,255,.35)`, color `#00C2FF`, Space Grotesk 600 12px, pill radius 20px.
  - H1: "Saúde animal com padrão científico" — Space Grotesk 700 46px, white.
  - Body: "Tecnologia genética e nutricional aplicada à produtividade e ao bem-estar de suínos, bovinos e equinos. Conheça a linha e finalize sua compra em nossa loja oficial." — Public Sans 400 17px, `rgba(255,255,255,.68)`.
  - Two buttons: "Ver loja completa →" (filled cyan) and "Conhecer produtos" (outline, links to #produtos).

### 3. Quem Somos (About)
Padding 80px 64px. Two-column flex row (gap 48px, align-items center):
- **Left** (max-width 640px): heading "Ciência e gestão a serviço do cuidado animal" (Space Grotesk 700 34px) + two body paragraphs (Public Sans 400 16px, `rgba(255,255,255,.68)`, line-height 1.75):
  1. "A BenoVet nasceu da união de dois profissionais com experiências complementares e um propósito em comum: contribuir para uma relação mais saudável, responsável e consciente entre as pessoas e seus animais."
  2. "Essa combinação nos permite enxergar o cuidado animal de forma ampla, unindo conhecimento técnico, qualidade, responsabilidade e inovação."
- **Right**: animated DNA symbol (192×288px) + "BenoVet" wordmark beside it at 88px Space Grotesk 700 ("Beno" white, "Vet" `#00C2FF`).

**Founders grid** (below, gap 28px, 2 columns, each card: dark card `#111826`, border `1px solid rgba(255,255,255,.1)`, radius 12px, padding 28px, flex row with 96×96px photo + text):
- **Tainã Vinicius Benovit** — MÉDICO-VETERINÁRIO. Bio: "Responsável pelo conhecimento técnico e pela visão voltada à saúde animal." Email: taina@benovet.com.br. Phone: (44) 99756-8684. Photo: `assets/taina-vinicius-benovit.png`.
- **Alan Deluan Gust** — ENG. AGRÍCOLA E ENG. CIVIL. Bio: "Traz experiência em gestão, planejamento, inovação e desenvolvimento de negócios." Email: alan@benovet.com.br. Phone: (45) 99834-6513. Photo: `assets/alan-deluan-gust.png`.

**Mission/Vision** (2-col grid, gap 28px, cards bordered `rgba(255,255,255,.1)`, radius 12px, padding 28px):
- Missão: "Oferecer produtos e soluções de qualidade para a saúde e o bem-estar animal, proporcionando aos nossos clientes confiança, informação e segurança em suas escolhas."
- Visão: "Ser uma empresa reconhecida pela qualidade, credibilidade e inovação no mercado de saúde animal, construindo relacionamentos duradouros com clientes, profissionais e parceiros."

**Values** (heading "Nossos Valores", 5-column grid, gap 20px, cards `#111826` bg, border `rgba(255,255,255,.08)`, radius 10px, padding 20px, title in `#00C2FF` Space Grotesk 700 14px):
1. Responsabilidade — "Tratamos a saúde animal com seriedade e respeito."
2. Qualidade — "Buscamos produtos que atendam aos mais altos padrões."
3. Conhecimento — "Boas decisões começam com informação adequada."
4. Confiança — "Relações transparentes e duradouras com clientes e parceiros."
5. Inovação — "Novas formas de melhorar o cuidado de quem cuida e de quem é cuidado."

### 4. Pet line section
Full-bleed background `assets/pets-section.png` (dogs/cats/rabbit composite), min-height 520px, same dark gradient overlay as hero. Left-aligned copy (max-width 560px):
- Eyebrow: "LINHA PET" — `#00C2FF`, Space Grotesk 600 12px.
- H2: "Cuidado veterinário também para quem divide a casa com você" — Space Grotesk 700 38px.
- Body: "Além da linha de produção animal, oferecemos produtos de saúde e bem-estar para cães, gatos e outros pets, com o mesmo padrão técnico e científico da BenoVet."
- Button: "Ver linha pet na loja →" (filled cyan).

### 5. Products ("Linha de produtos")
Padding 72px 64px. Centered heading + subcopy, then a 4-column grid (gap 24px) of product cards (`#111826` bg, border `rgba(255,255,255,.1)`, radius 12px, 170px placeholder image area on top, 18px padding content):
1. Vermífugo Suíno — "Amplo espectro, uso oral" — R$ 42,90
2. Suplemento Mineral Bovino — "Balde 30kg, uso a campo" — R$ 189,00
3. Complexo Vitamínico Equino — "Injetável, 50ml" — R$ 96,50
4. Kit Manejo Sanitário — "Uso veterinário essencial" — R$ 124,00

Cards have a subtle hover lift (translateY(-6px), border brightens to cyan). "Ver na loja →" link per card, in `#00C2FF`.

### 6. Closing CTA (NuvemShop)
Rounded card (radius 16px), background image `assets/products-bg.png` (dogs/cats composite) at full opacity with a light left-to-right dark tint overlay for text contrast. Row layout:
- Heading: "Catálogo completo e compra segura na nossa loja online" — Space Grotesk 700 28px.
- Body: "Todos os produtos, formas de pagamento e frete calculado estão disponíveis na nossa loja oficial."
- Button: "Acessar loja completa →" (filled cyan, Space Grotesk 700 15px) — **this should link out to the BenoVet NuvemShop store URL** (not yet specified — get the real URL from the client before shipping).

### 7. Footer
Grid: 1.4fr / 1fr / 1fr, padding 48px 64px, top border `rgba(255,255,255,.08)`.
- Col 1: large wordmark logo (`assets/logo-benovet.png`, ~342px tall, cropped/aligned to its visible mark — see note below).
- Col 2 "ENDEREÇO": Rua Paulo Wagner, 449 — Bairro Centro / Maripá — PR, Brasil / CEP 85955-312.
- Col 3 "CONTATO": alan@benovet.com.br / WhatsApp: (45) 99834-6513 / link back to "Quem Somos".

## Interactions & Behavior

### DNA particle-formation animation (nav + Quem Somos section)
A canvas-based decorative animation used in two places (nav, 134×202px; Quem Somos, 192×288px). Behavior:
1. Samples the alpha channel of `assets/symbol-benovet.png` (the DNA icon) at low resolution to get a point cloud of the glyph's visible pixels.
2. On scroll into view, particles animate from a random scatter (starting below/around the frame) converging onto their sampled target points over ~1.65s (ease-out cubic), colored cyan (`0,194,255` / `0,240,255`) on the left half and violet (`123,0,255` / `193,59,255`) on the right half.
3. Once formed, the real PNG fades in behind the particles (opacity 0→1, 1.2s).
4. The whole sequence loops every 3s: particles fade out near the end of the cycle and re-scatter for the next loop. The two instances run on independent, randomized timing offsets so they're not synchronized.
5. Mouse-proximity repel: particles within ~30px of the cursor are gently pushed away.
6. Respects `prefers-reduced-motion` — skips the animation and shows the static PNG.
7. The source PNG has large transparent padding around the glyph; both display boxes crop into it (roughly the middle 58% × 58% of the image) so the glyph fills its frame without dead space — replicate this crop when displaying the symbol at small sizes, or use a pre-cropped asset if producing one for production.

This is a "nice to have" brand moment — if it's not worth the engineering cost in the target stack, a static version of the DNA symbol (no animation) is an acceptable simplification; confirm with the client.

### Scroll reveals
Most content blocks fade up (`opacity 0→1`, `translateY(24px→0)`, 0.7s ease) via IntersectionObserver, triggered once when ~15% visible.

### Hover states
- Buttons (`bv-cta`): translateY(-2px) + background lightens to `#33D0FF` on hover.
- Product cards: translateY(-6px) + border brightens to `rgba(0,194,255,.5)` on hover.
- Links: `#00C2FF` default → `#5CD9FF` hover.

## State Management
Static content page — no dynamic state beyond the animation's internal particle simulation. No forms, no data fetching.

## Design Tokens

**Colors**
- Background: `#0B0F17`
- Card background: `#111826`
- Borders: `rgba(255,255,255,.08)` (subtle) / `rgba(255,255,255,.1)` (cards)
- Primary accent (cyan): `#00C2FF` (hover `#33D0FF` / `#5CD9FF`)
- Secondary accent (violet, used only in particle animation): `#7B00FF`
- Body text: `rgba(255,255,255,.55–.72)` depending on emphasis
- Headings: `#ffffff`

**Typography**
- Display/headings: Space Grotesk, weights 500/600/700
- Body/UI: Public Sans, weights 400/500/600/700
- Scale used: 12px (eyebrows) / 13–16px (body) / 20px (nav) / 28–46px (headings) / 88px (wordmark accent)

**Spacing / radius**
- Section padding: 72–80px vertical, 64px horizontal (40px on nav)
- Card radius: 10–16px depending on component
- Grid gaps: 20–28px

## Assets
All in `assets/`:
- `hero-animals.png` — hero background (pigs/cattle/horse)
- `pets-section.png` — pet-line background (dog/cat/rabbit)
- `products-bg.png` — closing-CTA background (dog/cat)
- `logo-benovet.png` — full wordmark + symbol lockup (footer)
- `symbol-benovet.png` — DNA symbol only, transparent PNG (source for the particle animation)
- `taina-vinicius-benovit.png`, `alan-deluan-gust.png` — founder headshots
- `brand-sheet.png` — unused reference sheet, not part of the live page

## Files
- `design-reference.html` — the full page prototype (single file, inline styles). This is the source of truth for layout/copy/colors; do not ship it as-is.
