# 🚀 Quick Start Guide - ML Assignment 2

## ⏱️ Complete in 60 Minutes

This is your express guide to complete the assignment. Follow these steps exactly.

---

## 📋 Before You Start

**You Need:**
- [ ] BITS Virtual Lab access
- [ ] GitHub account
- [ ] This ML_Assignment_2 folder

**Deadline:** 15-Feb-2026, 23:59 PM

---

## ⚡ Step 1: BITS Virtual Lab (15 mins)

### 1. Transfer folder to BITS Lab
Copy the entire `ML_Assignment_2` folder to your BITS Virtual Lab.

### 2. Install dependencies
```bash
cd ML_Assignment_2
pip install -r requirements.txt
```

### 3. Train models
```bash
python model/train_models.py
```

**Expected:** 
- Dataset downloads (1-2 mins)
- Models train (2-3 mins)
- Files created: 6 .pkl files, test_data.csv, results.txt

### 4. Run app
```bash
streamlit run app.py
```

### 5. Test app
- Upload test_data.csv
- Try all 6 models
- Check metrics appear

### 6. 📸 SCREENSHOT (CRITICAL!)
Take screenshot showing:
- BITS Lab interface
- Terminal with successful execution
- Streamlit app running

**Save as:** `BITS_Lab_Screenshot.png`

---

## 🐙 Step 2: GitHub (10 mins)

### 1. Create repository
- Go to https://github.com/new
- Name: `ML-Assignment-2-Classification`
- **Make it PUBLIC**
- Don't initialize with README

### 2. Push code
```bash
cd ML_Assignment_2
git init
git add .
git commit -m "ML Assignment 2: Classification Models"
git remote add origin https://github.com/YOUR_USERNAME/ML-Assignment-2-Classification.git
git branch -M main
git push -u origin main
```

### 3. Verify
Open your GitHub repo URL and check all files are there.

**Copy this link:** `https://github.com/YOUR_USERNAME/ML-Assignment-2-Classification`

---

## ☁️ Step 3: Streamlit Cloud (15 mins)

### 1. Deploy
- Go to https://streamlit.io/cloud
- Sign in with GitHub
- Click "New App"
- Repository: Select your repo
- Branch: main
- Main file: app.py
- Click "Deploy"

### 2. Wait
Deployment takes 2-5 minutes. You'll get a URL like:
`https://your-app-name.streamlit.app`

### 3. Test
- Open the URL
- Upload test_data.csv
- Test all models
- 📸 Take screenshot

**Copy this link:** `https://your-app-name.streamlit.app`

---

## 📄 Step 4: Create PDF (20 mins)

Create a PDF with these sections **in this exact order:**

### Page 1: Links
```
GitHub Repository Link:
[Make this clickable] https://github.com/YOUR_USERNAME/ML-Assignment-2-Classification

Live Streamlit App Link:
[Make this clickable] https://your-app-name.streamlit.app
```

### Page 2-3: Screenshots
1. BITS Lab screenshot (clear, showing execution)
2. Streamlit app screenshot (showing functionality)

### Page 4+: README Content
Copy the entire README.md file content:
- Problem statement
- Dataset description
- Model comparison table
- Observations for all 6 models
- All other sections

**Save PDF as:** `ML_Assignment2_YourName.pdf`

---

## 📤 Step 5: Submit (5 mins)

1. Go to Taxila LMS
2. Find ML Assignment 2
3. Upload your PDF
4. **SUBMIT** (not save draft)
5. Verify submission successful

**✅ Done!**

---

## 🎯 Success Checklist

Before submitting, verify:
- [ ] BITS Lab screenshot is clear and shows BITS interface
- [ ] Both links in PDF are clickable
- [ ] GitHub repo is public and accessible
- [ ] Streamlit app opens and works
- [ ] Complete README is in PDF
- [ ] PDF is properly formatted
- [ ] Submitted (not draft) before deadline

---

## 🆘 Emergency Troubleshooting

### Models won't train?
```bash
pip install --upgrade xgboost scikit-learn
python model/train_models.py
```

### Streamlit won't start?
```bash
streamlit --version  # Check if installed
pip install streamlit
streamlit run app.py
```

### Git push fails?
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git push -u origin main
```

### Deployment fails?
- Check requirements.txt has all packages
- Verify repo is public
- Check Streamlit Cloud logs for errors

---

## ⏰ Time Breakdown

- BITS Lab execution: 15 mins
- GitHub setup: 10 mins  
- Streamlit deployment: 15 mins
- PDF creation: 20 mins
- **Total: 60 minutes**

---

## 📊 What You're Submitting

### Your GitHub Repo Contains:
```
ML_Assignment_2/
├── app.py                  ✓ Streamlit app
├── requirements.txt        ✓ Dependencies
├── README.md               ✓ Documentation
├── model/
│   └── train_models.py    ✓ Training script
└── other docs...
```

### Your PDF Contains:
1. ✓ GitHub link (clickable)
2. ✓ Streamlit link (clickable)
3. ✓ BITS Lab screenshot
4. ✓ Streamlit app screenshot
5. ✓ Complete README content

---

## 🎓 Marks (Total: 15)

- Models + GitHub: 10 marks ✓
- Streamlit App: 4 marks ✓
- BITS Lab Screenshot: 1 mark ⏳

---

## ⚠️ Critical Reminders

1. **Only ONE submission** - No resubmissions allowed
2. **Deadline is strict** - 15-Feb-2026, 23:59 PM
3. **Links must work** - Test from different browser
4. **BITS screenshot required** - Shows BITS Lab interface
5. **README in PDF** - Complete content required

---

## 📞 Help

**BITS Lab Issues:**
Email: neha.vinayak@pilani.bits-pilani.ac.in
Subject: "ML Assignment 2: BITS Lab issue"

**For more details, see:**
- SETUP_INSTRUCTIONS.md
- DEPLOYMENT_GUIDE.md
- SUBMISSION_CHECKLIST.md

---

## ✨ You're Ready!

Everything is prepared. Just follow these 5 steps and you're done!

**Good luck! 🚀**

---

**Remember:** This is a complete, ready-to-submit project. All code works. All features implemented. Just execute, deploy, and submit!