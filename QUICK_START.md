# Quick Start Guide

## Running the Portfolio Locally

### ✅ Correct Way (Server from Project Root)

```bash
# Navigate to project root
cd "C:\Users\antho\OneDrive\Desktop\CS Projects Folder\2 Data Visualization Portfolio Site"

# Start server from root
python -m http.server 8000
```

Then visit: **http://localhost:8000/site/index.html**

### ❌ Wrong Way (Server from site/ folder)

```bash
# DON'T DO THIS
cd site
python -m http.server 8000  # This won't work!
```

**Why?** The HTML files in `site/` use relative paths `../visualizations/` to access images and interactive charts in the parent directory. The server must run from the project root to serve these files.

## Project Structure

```
project-root/                    ← Start server HERE
├── site/
│   ├── index.html              ← Visit: http://localhost:8000/site/index.html
│   ├── playground.html         ← Visit: http://localhost:8000/site/playground.html
│   └── resume.html             ← Visit: http://localhost:8000/site/resume.html
├── visualizations/
│   ├── static/                 ← Accessed via ../visualizations/static/
│   └── interactive/            ← Accessed via ../visualizations/interactive/
└── data/
    └── processed/              ← Accessed via ../data/processed/
```

## Accessing Pages

| Page | URL |
|------|-----|
| Main Portfolio | http://localhost:8000/site/index.html |
| Data Playground | http://localhost:8000/site/playground.html |
| Resume | http://localhost:8000/site/resume.html |

## Common Issues & Solutions

### Issue: "Interactive charts show 404 errors"
**Solution:** Make sure the server is running from the **project root**, not from `site/`

### Issue: "Playground charts not loading"
**Solution:**
1. Server must be from project root
2. Access via `http://localhost:8000/site/playground.html` (not `file://`)
3. Check browser console for CORS errors

### Issue: "Images not showing"
**Solution:** Verify server is at project root and access via `http://localhost:8000/site/index.html`

## Deployment to GitHub Pages

When deploying to GitHub Pages, the site structure will need adjustment since GitHub Pages serves from a root or `/docs` folder. You have two options:

### Option 1: Move everything to root
- Move all files from `site/` to project root
- Update paths from `../visualizations/` to `visualizations/`

### Option 2: Use `/docs` folder
- Rename `site/` to `docs/`
- Move `visualizations/` and `data/` into `docs/`
- Update GitHub Pages to serve from `/docs`

## All Bugs Fixed (8 Total)

✅ Playground X-axis labels corrected
✅ Column name mismatches fixed
✅ Missing `requests` library added
✅ Empty data validation added
✅ Null safety throughout data processing
✅ URL encoding fixed in contact form
✅ Passive scroll listeners for performance
✅ Accessibility labels added

## Need Help?

Check the main README.md for detailed setup instructions and project documentation.
