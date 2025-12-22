# OpenSense Website

A professional, distinctive website for open-source environmental monitoring sensors and hydrology consultancy.

## Features

- **Responsive Design**: Works beautifully on desktop, tablet, and mobile
- **Water-Inspired Aesthetic**: Unique color palette and flowing design elements
- **Professional Typography**: Literata serif paired with Space Mono monospace
- **Smooth Animations**: Subtle transitions and effects throughout
- **Five Complete Pages**:
  - Home - Mission, sensor overview, deployments
  - Sensors - Detailed specs for LiDAR, ultrasonic, water quality, and moisture sensors
  - Science - Research methodology and publications
  - Consultancy - Services and case studies
  - About - Team and organizational information

## Quick Start

### Option 1: Deploy to Netlify (Recommended)

1. Push these files to a GitHub repository
2. Go to [Netlify](https://netlify.com) and sign up/login
3. Click "Add new site" → "Import an existing project"
4. Connect your GitHub account and select your repository
5. Build settings:
   - Build command: (leave empty)
   - Publish directory: (leave empty or use `.`)
6. Click "Deploy site"

Your site will be live in seconds at a `*.netlify.app` URL. You can customize the domain in settings.

### Option 2: GitHub Pages

1. Push these files to a GitHub repository
2. Go to repository Settings → Pages
3. Source: Deploy from a branch
4. Branch: `main` (or `master`), folder: `/ (root)`
5. Click Save

Your site will be live at `https://yourusername.github.io/repository-name/`

### Option 3: Vercel

1. Push these files to a GitHub repository
2. Go to [Vercel](https://vercel.com) and sign up/login
3. Click "Add New" → "Project"
4. Import your GitHub repository
5. Click "Deploy"

## File Structure

```
├── index.html          # Homepage
├── sensors.html        # Sensor catalog with specs
├── science.html        # Research methodology
├── consultancy.html    # Services and case studies
├── about.html          # Team and organization
├── styles.css          # Complete stylesheet
└── README.md          # This file
```

## Customization

### Update Content

Simply edit the HTML files to change:
- Team member names and roles (in `about.html`)
- Deployment locations (in `index.html`)
- Case studies (in `consultancy.html`)
- Publications (in `science.html`)
- Sensor specifications (in `sensors.html`)

### Customize Design

The design system is defined in CSS variables at the top of `styles.css`:

```css
:root {
    --primary-deep: #0A3D62;      /* Main brand color */
    --accent-teal: #4ECDC4;       /* Accent color */
    --accent-coral: #FF6B6B;      /* Secondary accent */
    /* ... more colors */
}
```

Change these values to match your brand colors.

### Add Your Logo

Replace the text logo in the navbar with an image:

```html
<!-- Replace this in all HTML files: -->
<a href="index.html" class="logo">OpenSense</a>

<!-- With: -->
<a href="index.html" class="logo">
    <img src="your-logo.png" alt="OpenSense" style="height: 40px;">
</a>
```

### Connect GitHub Repository

Update all GitHub links throughout the site (search for `https://github.com` and replace with your actual repo URL).

### Add E-commerce Later

When ready to add a shop, you can integrate:
- **Shopify Buy Button** - Add products without full Shopify site
- **Gumroad** - Embed products directly
- **Stripe Payment Links** - Simple checkout links
- **Snipcart** - Full shopping cart for static sites

## Browser Support

- Chrome, Firefox, Safari, Edge (latest 2 versions)
- Mobile browsers (iOS Safari, Chrome Android)
- Progressive enhancement for older browsers

## License

Feel free to use this template for your project. Consider it MIT licensed.

## Need Help?

- **Deployment Issues**: Check the hosting provider's documentation
- **Customization Questions**: The code is well-commented, look through the CSS
- **Design Updates**: All visual elements are in `styles.css`

## Next Steps

1. ✅ Deploy to Netlify/GitHub Pages/Vercel
2. 📝 Customize content with your actual team info and data
3. 🎨 Add your logo and brand colors
4. 📸 Replace placeholder team photos with real ones
5. 🔗 Update all external links (GitHub, social media, etc.)
6. 📧 Add contact forms if needed
7. 🛒 Integrate e-commerce when ready

---

Built with modern HTML5, CSS3, and clean semantic markup. No JavaScript frameworks required - just fast, accessible, beautiful web standards.
