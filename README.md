# BenoVet - Veterinary Solutions Website

Modern, responsive website for BenoVet with advanced features including DNA particle formation animation, mobile-first design, and premium dark mode interface.

## Features

- ✨ **DNA Particle Animation** - Custom canvas-based particle system that forms the logo from glowing particles
- 📱 **Mobile-First Responsive** - Optimized for all devices (320px - 1920px+)
- 🎨 **Dark Mode Premium** - Elegant dark theme with cyan and purple accents
- ⚡ **High Performance** - No build step required, pure HTML/CSS/JS
- ♿ **Accessibility** - WCAG AA compliance, prefers-reduced-motion support
- 🧬 **Founder Profiles** - Detailed team section with credentials

## Project Structure

```
├── index.html                 # Main website
├── frontend/
│   └── assets/               # Images and logos
│       ├── symbol-benovet.png
│       ├── logo-benovet.png
│       ├── hero-animals.png
│       ├── pets-section.png
│       ├── products-bg.png
│       └── founder photos
├── midia/                    # Additional media files
└── vercel.json              # Vercel configuration
```

## Deployment

### With Vercel CLI

```bash
npm install -g vercel
vercel
```

### With Git (GitHub/GitLab)

1. Push to your repository
2. Connect at https://vercel.com
3. Select the repository
4. Deploy automatically on each push

## Local Development

Serve locally with Python:

```bash
python -m http.server 8080
```

Visit: http://localhost:8080

## Customization

### Colors
Edit CSS custom properties for brand colors:
- Cyan: `#00C2FF`
- Purple: `#7B00FF`
- Dark Background: `#0B0F17`

### Content
Edit text directly in `index.html` - no build process needed.

### DNA Animation
The particle animation is fully functional and will render on both navbar and about section logos. It respects `prefers-reduced-motion` for accessibility.

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- LCP: < 2.5s
- FID: < 100ms
- CLS: < 0.1
- No JavaScript dependencies required

## License

All rights reserved © BenoVet
