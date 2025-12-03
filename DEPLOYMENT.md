# Deploying to innodative.com via GitHub Pages

## Prerequisites

1. A GitHub account
2. A repository for your site (e.g., `ProfessorBrunner/innodative-site` or similar)
3. Access to innodative.com DNS settings

## Step 1: Push Site to GitHub

1. Create a new repository on GitHub (can be public or private)
   - Go to https://github.com/new
   - Name it something like `innodative-site` or `website`
   - Do NOT initialize with README, .gitignore, or license (we have our files)

2. Initialize git in your site directory and push:
   ```bash
   cd pelican-tufte-site
   git init
   git add .
   git commit -m "Initial commit - Innodative website"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   git push -u origin main
   ```

## Step 2: Configure GitHub Pages

1. Go to your repository on GitHub
2. Click "Settings" → "Pages" (in the left sidebar)
3. Under "Build and deployment":
   - Source: Select "GitHub Actions"
4. The site will automatically build and deploy when you push to main

## Step 3: Configure Custom Domain (innodative.com)

### In GitHub Repository Settings:
1. Go to Settings → Pages
2. Under "Custom domain", enter: `innodative.com`
3. Click "Save"
4. Check "Enforce HTTPS" (may take a few minutes to become available)

### In Your Domain DNS Settings:
You need to add DNS records for innodative.com. Log into your domain registrar and add:

**For apex domain (innodative.com):**
Add these A records pointing to GitHub's IP addresses:
```
A    @    185.199.108.153
A    @    185.199.109.153
A    @    185.199.110.153
A    @    185.199.111.153
```

**For www subdomain (optional but recommended):**
```
CNAME    www    YOUR-USERNAME.github.io
```

**DNS propagation** can take up to 48 hours, but usually happens within minutes to hours.

### Verify DNS Configuration:
After DNS propagates, you can verify with:
```bash
dig innodative.com +noall +answer
```

## Step 4: Wait for Deployment

1. After pushing to GitHub, go to the "Actions" tab in your repository
2. You'll see a workflow run called "Deploy to GitHub Pages"
3. Wait for it to complete (usually 1-2 minutes)
4. Once complete, your site will be live at https://innodative.com

## Making Updates

To update your site:

1. Make changes to your content files (in `content/` directory)
2. Test locally if desired:
   ```bash
   cd pelican-tufte-site
   pelican content -s pelicanconf.py
   pelican --listen
   # Visit http://localhost:8000
   ```
3. Commit and push changes:
   ```bash
   git add .
   git commit -m "Description of your changes"
   git push
   ```
4. GitHub Actions will automatically rebuild and deploy

## Troubleshooting

### Site not loading at innodative.com:
- Check DNS propagation: `dig innodative.com`
- Verify CNAME file exists in repository: `content/extra/CNAME`
- Check GitHub Pages settings: Settings → Pages
- Look for errors in Actions tab

### SSL certificate issues:
- Wait up to 24 hours for certificate provisioning
- Ensure "Enforce HTTPS" is checked in GitHub Pages settings
- DNS must be properly configured first

### Changes not appearing:
- Check Actions tab for deployment status
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Wait a few minutes for CDN to update

## Files Configured for innodative.com

The following files are already configured for innodative.com:

- `publishconf.py`: SITEURL = 'https://innodative.com'
- `content/extra/CNAME`: Contains 'innodative.com'
- `content/extra/.nojekyll`: Prevents Jekyll processing
- `.github/workflows/deploy.yml`: GitHub Actions deployment workflow

No additional configuration is needed!
