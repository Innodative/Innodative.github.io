# Quick Start Guide - Publishing to innodative.com

## What's Already Configured

Your site is **completely ready** to deploy to innodative.com. All necessary files are configured:

✅ Custom domain set to innodative.com  
✅ CNAME file created  
✅ .nojekyll file for GitHub Pages  
✅ GitHub Actions workflow for automatic deployment  
✅ All content pages updated  

## Deploy in 5 Minutes

### 1. Create GitHub Repository
```bash
# Go to https://github.com/new
# Create a new repository (e.g., "innodative-site")
# Do NOT initialize with README
```

### 2. Push Your Site
```bash
cd pelican-tufte-site
git init
git add .
git commit -m "Initial commit - Innodative website"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git push -u origin main
```

### 3. Enable GitHub Pages
- Go to your repo → Settings → Pages
- Source: Select "GitHub Actions"
- Custom domain: Enter `innodative.com`
- Check "Enforce HTTPS"

### 4. Configure DNS
In your domain registrar (where you manage innodative.com), add these A records:

```
Type: A    Name: @    Value: 185.199.108.153
Type: A    Name: @    Value: 185.199.109.153
Type: A    Name: @    Value: 185.199.110.153
Type: A    Name: @    Value: 185.199.111.153
```

Optional but recommended - add www subdomain:
```
Type: CNAME    Name: www    Value: YOUR-USERNAME.github.io
```

### 5. Wait
- GitHub Actions will build your site (1-2 minutes)
- DNS propagation (minutes to hours)
- SSL certificate provisioning (up to 24 hours)

Visit https://innodative.com - you're live! 🎉

## Making Updates Later

1. Edit files in `content/` directory
2. Commit and push:
   ```bash
   git add .
   git commit -m "Updated content"
   git push
   ```
3. GitHub automatically rebuilds and deploys

## Need Help?

See DEPLOYMENT.md for detailed instructions and troubleshooting.

## Current Site Status

- 3 published blog posts (in Thoughts category)
- 12 pages including: Research, Teaching, Consulting, Media, About, Colophon
- Ready for custom domain: innodative.com
