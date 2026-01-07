# Setup Instructions for BITS Virtual Lab

## Step-by-Step Guide to Run this Project on BITS Virtual Lab

### Step 1: Access BITS Virtual Lab
1. Login to BITS Virtual Lab
2. Start your virtual machine
3. Open a terminal

### Step 2: Install Required Packages

```bash
# Update pip
pip install --upgrade pip

# Install all dependencies
pip install streamlit==1.31.0
pip install scikit-learn==1.4.0
pip install numpy==1.26.3
pip install pandas==2.1.4
pip install matplotlib==3.8.2
pip install seaborn==0.13.1
pip install xgboost==2.0.3
```

Or install from requirements.txt:
```bash
pip install -r requirements.txt
```

### Step 3: Navigate to Project Directory

```bash
cd ML_Assignment_2
```

### Step 4: Train the Models

```bash
python model/train_models.py
```

**Expected Output:**
- Dataset will be downloaded from UCI repository
- All 6 models will be trained
- Evaluation metrics will be displayed
- Model files (*.pkl) will be saved in the model/ directory
- test_data.csv will be generated
- results.txt will be created with detailed metrics

**Time Required:** Approximately 2-5 minutes

### Step 5: Run Streamlit App Locally

```bash
streamlit run app.py
```

**Expected Output:**
- Streamlit will start a local server
- Browser will open automatically at http://localhost:8501
- If browser doesn't open, manually navigate to the URL shown in terminal

### Step 6: Test the Application

1. Upload the generated `test_data.csv` file
2. Select different models from the dropdown
3. Observe the metrics, confusion matrix, and classification report
4. Download predictions if needed

### Step 7: Take Screenshot

**IMPORTANT for Assignment Submission:**
1. Ensure the terminal showing successful model training is visible
2. Ensure the Streamlit app is running and showing results
3. Take a screenshot showing:
   - Terminal with training output
   - Streamlit app with model results
   - BITS Virtual Lab interface visible
4. Save screenshot as `BITS_Lab_Screenshot.png`

---

## Troubleshooting

### Issue 1: Module Not Found Error
**Error:** `ModuleNotFoundError: No module named 'xgboost'`

**Solution:**
```bash
pip install xgboost
```

### Issue 2: Permission Denied
**Error:** `Permission denied when writing files`

**Solution:**
```bash
chmod +x model/train_models.py
```

### Issue 3: Dataset Download Fails
**Error:** `Unable to download dataset from UCI`

**Solution:**
- Check internet connection
- Try running the script again
- Dataset will be cached after first successful download

### Issue 4: Streamlit Port Already in Use
**Error:** `Port 8501 is already in use`

**Solution:**
```bash
# Kill existing streamlit processes
pkill streamlit

# Or run on different port
streamlit run app.py --server.port 8502
```

### Issue 5: Memory Error
**Error:** `MemoryError during model training`

**Solution:**
- Close unnecessary applications
- Reduce n_estimators in Random Forest and XGBoost (in train_models.py)
- Use a smaller subset of data for testing

---

## Verification Checklist

Before taking screenshot, verify:
- [ ] All 6 models trained successfully
- [ ] Model files (.pkl) created in model/ directory
- [ ] test_data.csv generated
- [ ] results.txt contains comparison table
- [ ] Streamlit app opens without errors
- [ ] Can upload test_data.csv successfully
- [ ] All models selectable from dropdown
- [ ] Metrics display correctly
- [ ] Confusion matrix visible
- [ ] Classification report shows

---

## Quick Commands Reference

```bash
# Install dependencies
pip install -r requirements.txt

# Train models
python model/train_models.py

# Run app
streamlit run app.py

# Check Python version
python --version

# List installed packages
pip list

# Check if streamlit is installed
streamlit --version
```

---

## Expected Files After Training

```
ML_Assignment_2/
├── app.py
├── requirements.txt
├── README.md
├── test_data.csv                           # ✓ Generated
│
└── model/
    ├── train_models.py
    ├── results.txt                         # ✓ Generated
    ├── scaler.pkl                          # ✓ Generated
    ├── label_encoders.pkl                  # ✓ Generated
    ├── logistic_regression_model.pkl       # ✓ Generated
    ├── decision_tree_model.pkl             # ✓ Generated
    ├── k-nearest_neighbors_model.pkl       # ✓ Generated
    ├── naive_bayes_model.pkl               # ✓ Generated
    ├── random_forest_model.pkl             # ✓ Generated
    └── xgboost_model.pkl                   # ✓ Generated
```

---

## Support

If you encounter any issues specific to BITS Virtual Lab:
- Email: neha.vinayak@pilani.bits-pilani.ac.in
- Subject: "ML Assignment 2: BITS Lab issue"

---

## Notes for Assignment Submission

1. **Screenshot Requirements:**
   - Must show BITS Virtual Lab interface
   - Must show successful execution
   - Must be clear and readable
   - File name: `BITS_Lab_Screenshot.png`

2. **What to Include in PDF:**
   - GitHub repository link
   - Live Streamlit app link
   - Screenshot of BITS Lab execution
   - Complete README.md content

3. **Before Submission:**
   - Test GitHub repository link (should open correctly)
   - Test Streamlit app link (should load without errors)
   - Verify screenshot is clear and shows required details
   - Ensure README.md is included in PDF

---

## Estimated Timeline

- **Setup & Installation:** 5-10 minutes
- **Model Training:** 2-5 minutes
- **Testing Streamlit App:** 5-10 minutes
- **Taking Screenshot:** 2-3 minutes
- **Total:** ~20-30 minutes

---

**Good Luck with Your Assignment! 🎓**