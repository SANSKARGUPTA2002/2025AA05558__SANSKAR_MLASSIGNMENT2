# Deployment Guide: Streamlit Community Cloud

## Prerequisites
- GitHub account
- Completed project with all files
- Streamlit Community Cloud account (free)

---

## Step 1: Prepare Your GitHub Repository

### 1.1 Initialize Git Repository (if not already done)
```bash
cd ML_Assignment_2
git init
```

### 1.2 Configure Git (first time only)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 1.3 Create Repository on GitHub
1. Go to https://github.com
2. Click "New Repository" (+ icon in top right)
3. Name: `ML-Assignment-2-Classification` (or any name)
4. Description: "ML Assignment 2: Adult Income Classification Models"
5. Keep it Public (required for free Streamlit deployment)
6. Don't initialize with README (we already have one)
7. Click "Create repository"

### 1.4 Connect Local Repository to GitHub
```bash
# Add all files
git add .

# Commit
git commit -m "Initial commit: ML Assignment 2 - Classification Models"

# Add remote origin (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/ML-Assignment-2-Classification.git

# Set main branch
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## Step 2: Verify GitHub Repository

### Check that all required files are present:
- [ ] app.py
- [ ] requirements.txt
- [ ] README.md
- [ ] model/train_models.py
- [ ] .gitignore

**Note:** Model files (.pkl) and test_data.csv will be generated during deployment or can be committed if small enough.

---

## Step 3: Prepare for Streamlit Deployment

### 3.1 Important: Model Files Handling

**Option A: Include Small Test Models (Recommended)**
If your model files are small (<100 MB), you can commit them:

```bash
# Remove .pkl from .gitignore temporarily
# Edit .gitignore and comment out: # *.pkl

# Add model files
git add model/*.pkl test_data.csv

# Commit
git commit -m "Add trained models and test data"

# Push
git push origin main
```

**Option B: Train Models on Streamlit Cloud**
If models are large, add a startup script to train them during deployment.

Create `startup.sh`:
```bash
#!/bin/bash
python model/train_models.py
```

And update your deployment to run this script first.

---

## Step 4: Deploy on Streamlit Community Cloud

### 4.1 Sign Up / Sign In
1. Go to https://share.streamlit.io/ or https://streamlit.io/cloud
2. Click "Sign in with GitHub"
3. Authorize Streamlit to access your GitHub account

### 4.2 Create New App
1. Click "New app" button
2. Fill in the deployment form:

   **Repository:**
   - Select your repository: `YOUR_USERNAME/ML-Assignment-2-Classification`
   
   **Branch:**
   - Select: `main`
   
   **Main file path:**
   - Enter: `app.py`
   
   **App URL (optional):**
   - Custom subdomain (e.g., `ml-assignment-2-yourname`)
   - Or leave blank for auto-generated URL

3. Click "Deploy!"

### 4.3 Wait for Deployment
- Initial deployment takes 2-5 minutes
- You'll see a deployment log
- Status will change from "Building" → "Running"
- Any errors will be shown in the logs

### 4.4 Deployment Complete
- You'll receive a public URL: `https://YOUR-APP-NAME.streamlit.app`
- App is now live and accessible to anyone with the link

---

## Step 5: Test Your Deployed App

### 5.1 Basic Functionality Test
1. Open the Streamlit app URL
2. Verify the app loads without errors
3. Check that all 6 models appear in dropdown
4. Upload test_data.csv (if you committed it, download from GitHub first)
5. Select each model and verify metrics display
6. Check confusion matrix renders correctly
7. Verify classification report shows

### 5.2 Common Deployment Issues

**Issue 1: Module Not Found**
- **Cause:** Missing package in requirements.txt
- **Solution:** Add missing package to requirements.txt, commit, and push

**Issue 2: Model Files Not Found**
- **Cause:** Model files not in repository
- **Solution:** Either commit model files or add training script to run on startup

**Issue 3: Memory Limit Exceeded**
- **Cause:** Streamlit free tier has memory limits
- **Solution:** Use smaller models or reduce dataset size

**Issue 4: Build Fails**
- **Cause:** Syntax errors or incompatible package versions
- **Solution:** Check deployment logs for specific error messages

---

## Step 6: Update Your App (After Deployment)

### 6.1 Make Changes Locally
```bash
# Edit files as needed
# Example: Update app.py

# Add changes
git add app.py

# Commit
git commit -m "Update: Improve UI layout"

# Push
git push origin main
```

### 6.2 Automatic Re-deployment
- Streamlit automatically detects changes
- App rebuilds and redeploys automatically
- Usually takes 1-2 minutes

### 6.3 Manual Re-deployment
If automatic deployment fails:
1. Go to Streamlit Cloud dashboard
2. Find your app
3. Click "Reboot" button

---

## Step 7: Manage Your App

### Access Streamlit Cloud Dashboard
- URL: https://share.streamlit.io/
- View all your deployed apps
- Check deployment status
- View logs
- Reboot or delete apps

### App Settings
Click on your app → Settings:
- **Secrets:** Add API keys (not needed for this project)
- **Logs:** View runtime logs
- **Resources:** Check memory/CPU usage
- **Delete:** Remove the app

---

## Step 8: Submission Preparation

### 8.1 Collect Required Links

**GitHub Repository Link:**
```
https://github.com/YOUR_USERNAME/ML-Assignment-2-Classification
```

**Live Streamlit App Link:**
```
https://YOUR-APP-NAME.streamlit.app
```

### 8.2 Verify Links Work
- [ ] GitHub link opens and shows all files
- [ ] Streamlit app link opens and app loads
- [ ] App is functional and shows no errors
- [ ] README.md is visible on GitHub

### 8.3 Create Screenshot
- [ ] Open app in browser
- [ ] Select a model and upload test data
- [ ] Ensure metrics and confusion matrix are visible
- [ ] Take full-screen screenshot
- [ ] Save as `Streamlit_App_Screenshot.png`

---

## Step 9: Create Submission PDF

### Include in PDF (in order):
1. **Cover Page**
   - Assignment title
   - Your name and ID
   - Course details

2. **Links Section**
   - GitHub Repository Link (clickable)
   - Live Streamlit App Link (clickable)

3. **Screenshots**
   - BITS Virtual Lab screenshot showing model training
   - Streamlit app screenshot showing live deployment

4. **Complete README.md Content**
   - Copy entire README.md
   - Include all tables and observations

---

## Troubleshooting Guide

### Problem: App is slow
**Solution:**
- Optimize model loading with @st.cache_resource
- Reduce model complexity
- Use smaller test datasets

### Problem: Build timeout
**Solution:**
- Reduce dependencies in requirements.txt
- Use specific package versions
- Check if model files are too large

### Problem: Cannot upload files
**Solution:**
- Check file size limits (200 MB for free tier)
- Verify file format is CSV
- Ensure correct column names

### Problem: Confusion matrix not displaying
**Solution:**
- Check matplotlib/seaborn versions
- Verify data preprocessing
- Check for NaN values in predictions

---

## Best Practices

1. **Keep Repository Clean**
   - Use .gitignore properly
   - Don't commit large binary files unless necessary
   - Keep commits meaningful

2. **Version Control**
   - Commit frequently with clear messages
   - Use branches for experimental features
   - Tag releases for milestones

3. **Documentation**
   - Keep README.md updated
   - Document any special requirements
   - Include usage examples

4. **Testing**
   - Test locally before deploying
   - Test on different browsers
   - Test with different datasets

---

## Quick Reference: Common Commands

```bash
# Check git status
git status

# Add all changes
git add .

# Commit with message
git commit -m "Your message here"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# View commit history
git log --oneline

# Check remote URL
git remote -v
```

---

## Support Resources

- **Streamlit Documentation:** https://docs.streamlit.io/
- **Streamlit Community Forum:** https://discuss.streamlit.io/
- **GitHub Documentation:** https://docs.github.com/
- **Python Documentation:** https://docs.python.org/

---

## Submission Checklist

Before final submission:
- [ ] GitHub repository is public and accessible
- [ ] All required files are committed
- [ ] README.md is complete and formatted correctly
- [ ] Streamlit app is deployed and running
- [ ] App URL is accessible from any browser
- [ ] BITS Lab screenshot is clear and shows execution
- [ ] Streamlit app screenshot shows functionality
- [ ] PDF contains all required components
- [ ] Links in PDF are clickable and working
- [ ] Submitted before deadline: 15-Feb-2026, 23:59 PM

---

**Good Luck with Your Deployment! 🚀**