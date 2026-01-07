"""
ML Assignment 2 - Interactive Streamlit App
Adult Income Classification Dashboard
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (accuracy_score, roc_auc_score, precision_score,
                            recall_score, f1_score, matthews_corrcoef,
                            confusion_matrix, classification_report)
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="ML Classification Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("🎓 ML Assignment 2: Classification Models Dashboard")
st.markdown("### Adult Income Prediction - Binary Classification")
st.markdown("---")

# Sidebar for model selection and file upload
st.sidebar.header("⚙️ Configuration")
st.sidebar.markdown("---")

# Model selection dropdown
model_options = {
    'Logistic Regression': 'model/logistic_regression_model.pkl',
    'Decision Tree': 'model/decision_tree_model.pkl',
    'K-Nearest Neighbors': 'model/k-nearest_neighbors_model.pkl',
    'Naive Bayes': 'model/naive_bayes_model.pkl',
    'Random Forest': 'model/random_forest_model.pkl',
    'XGBoost': 'model/xgboost_model.pkl'
}

selected_model_name = st.sidebar.selectbox(
    "📌 Select Classification Model",
    list(model_options.keys())
)

st.sidebar.markdown("---")

# File upload
st.sidebar.header("📁 Upload Test Data")
uploaded_file = st.sidebar.file_uploader(
    "Upload CSV file",
    type=['csv'],
    help="Upload your test dataset in CSV format"
)

st.sidebar.markdown("---")
st.sidebar.info("""
**Dataset Info:**
- Features: 14
- Target: Income (<=50K or >50K)
- Total Instances: 48,000+
""")

# Load model function
@st.cache_resource
def load_model(model_path):
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Calculate metrics function
def calculate_metrics(y_true, y_pred, y_pred_proba=None):
    metrics = {
        'Accuracy': accuracy_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred, zero_division=0),
        'Recall': recall_score(y_true, y_pred, zero_division=0),
        'F1 Score': f1_score(y_true, y_pred, zero_division=0),
        'MCC': matthews_corrcoef(y_true, y_pred)
    }
    
    if y_pred_proba is not None:
        metrics['AUC'] = roc_auc_score(y_true, y_pred_proba)
    else:
        metrics['AUC'] = 0.0
    
    return metrics

# Plot confusion matrix
def plot_confusion_matrix(cm, class_names=['<=50K', '>50K']):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=class_names, yticklabels=class_names,
                cbar_kws={'label': 'Count'})
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.title('Confusion Matrix', fontsize=16, fontweight='bold')
    return fig

# Main content
if uploaded_file is not None:
    try:
        # Load data
        data = pd.read_csv(uploaded_file)
        
        # Display dataset info
        st.header("📊 Dataset Overview")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Samples", len(data))
        with col2:
            st.metric("Features", len(data.columns) - 1)
        with col3:
            if 'income' in data.columns:
                st.metric("Target Classes", data['income'].nunique())
        
        # Show sample data
        with st.expander("📋 View Sample Data (First 10 rows)"):
            st.dataframe(data.head(10))
        
        st.markdown("---")
        
        # Check if target column exists
        if 'income' not in data.columns:
            st.error("⚠️ Target column 'income' not found in the dataset!")
            st.stop()
        
        # Prepare data
        X_test = data.drop('income', axis=1)
        y_test = data['income']
        
        # Load selected model
        st.header(f"🤖 Model: {selected_model_name}")
        model = load_model(model_options[selected_model_name])
        
        if model is not None:
            # Make predictions
            with st.spinner('Making predictions...'):
                y_pred = model.predict(X_test)
                
                # Get prediction probabilities if available
                if hasattr(model, 'predict_proba'):
                    y_pred_proba = model.predict_proba(X_test)[:, 1]
                else:
                    y_pred_proba = None
                
                # Calculate metrics
                metrics = calculate_metrics(y_test, y_pred, y_pred_proba)
            
            st.success("✅ Predictions completed!")
            
            # Display evaluation metrics
            st.header("📈 Evaluation Metrics")
            
            metric_cols = st.columns(3)
            with metric_cols[0]:
                st.metric("Accuracy", f"{metrics['Accuracy']:.4f}")
                st.metric("Precision", f"{metrics['Precision']:.4f}")
            with metric_cols[1]:
                st.metric("AUC Score", f"{metrics['AUC']:.4f}")
                st.metric("Recall", f"{metrics['Recall']:.4f}")
            with metric_cols[2]:
                st.metric("F1 Score", f"{metrics['F1 Score']:.4f}")
                st.metric("MCC Score", f"{metrics['MCC']:.4f}")
            
            st.markdown("---")
            
            # Confusion Matrix and Classification Report
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("🎯 Confusion Matrix")
                cm = confusion_matrix(y_test, y_pred)
                fig = plot_confusion_matrix(cm)
                st.pyplot(fig)
                
                # Additional confusion matrix info
                tn, fp, fn, tp = cm.ravel()
                st.info(f"""
                **Confusion Matrix Breakdown:**
                - True Negatives (TN): {tn}
                - False Positives (FP): {fp}
                - False Negatives (FN): {fn}
                - True Positives (TP): {tp}
                """)
            
            with col2:
                st.subheader("📋 Classification Report")
                report = classification_report(y_test, y_pred, 
                                              target_names=['<=50K', '>50K'],
                                              output_dict=True)
                
                # Convert to DataFrame for better display
                report_df = pd.DataFrame(report).transpose()
                st.dataframe(report_df.style.format("{:.3f}"))
                
                # Display full text report in expander
                with st.expander("View Detailed Classification Report"):
                    report_text = classification_report(y_test, y_pred,
                                                       target_names=['<=50K', '>50K'])
                    st.text(report_text)
            
            st.markdown("---")
            
            # Prediction distribution
            st.header("📊 Prediction Distribution")
            pred_col1, pred_col2 = st.columns(2)
            
            with pred_col1:
                st.subheader("Actual Distribution")
                actual_counts = pd.Series(y_test).value_counts()
                fig, ax = plt.subplots(figsize=(6, 4))
                actual_counts.plot(kind='bar', color=['#3498db', '#e74c3c'], ax=ax)
                plt.xlabel('Income Class')
                plt.ylabel('Count')
                plt.title('Actual Class Distribution')
                plt.xticks(rotation=0)
                st.pyplot(fig)
            
            with pred_col2:
                st.subheader("Predicted Distribution")
                pred_counts = pd.Series(y_pred).value_counts()
                fig, ax = plt.subplots(figsize=(6, 4))
                pred_counts.plot(kind='bar', color=['#3498db', '#e74c3c'], ax=ax)
                plt.xlabel('Income Class')
                plt.ylabel('Count')
                plt.title('Predicted Class Distribution')
                plt.xticks(rotation=0)
                st.pyplot(fig)
            
            st.markdown("---")
            
            # Download predictions
            st.header("💾 Download Results")
            results_df = pd.DataFrame({
                'Actual': y_test,
                'Predicted': y_pred,
                'Correct': y_test == y_pred
            })
            
            csv = results_df.to_csv(index=False)
            st.download_button(
                label="📥 Download Predictions as CSV",
                data=csv,
                file_name=f'{selected_model_name.lower().replace(" ", "_")}_predictions.csv',
                mime='text/csv'
            )
            
    except Exception as e:
        st.error(f"⚠️ Error processing data: {str(e)}")
        st.info("Please ensure your CSV file has the correct format with an 'income' column as target.")

else:
    # Display instructions when no file is uploaded
    st.info("👈 Please upload a CSV file using the sidebar to begin analysis")
    
    st.header("📖 Instructions")
    st.markdown("""
    ### How to use this dashboard:
    
    1. **Select a Model**: Choose from 6 different classification models in the sidebar
    2. **Upload Test Data**: Upload your test dataset (CSV format) with the 'income' target column
    3. **View Results**: Explore evaluation metrics, confusion matrix, and classification report
    4. **Download Predictions**: Save the prediction results for further analysis
    
    ### Available Models:
    - 🔹 Logistic Regression
    - 🔹 Decision Tree Classifier
    - 🔹 K-Nearest Neighbors
    - 🔹 Naive Bayes (Gaussian)
    - 🔹 Random Forest (Ensemble)
    - 🔹 XGBoost (Ensemble)
    
    ### Evaluation Metrics:
    - **Accuracy**: Overall correctness of predictions
    - **AUC**: Area Under the ROC Curve
    - **Precision**: Accuracy of positive predictions
    - **Recall**: Coverage of actual positive cases
    - **F1 Score**: Harmonic mean of precision and recall
    - **MCC**: Matthews Correlation Coefficient
    """)
    
    st.markdown("---")
    
    # Model comparison table
    st.header("🏆 Model Performance Comparison")
    st.info("Upload test data to see live model performance. Below is the performance from training:")
    
    # Sample comparison data (will be replaced with actual results)
    st.markdown("""
    All models have been trained on the Adult Income dataset with the following configuration:
    - **Dataset**: UCI Adult Income Dataset
    - **Features**: 14 (age, workclass, education, occupation, etc.)
    - **Instances**: 48,842 samples
    - **Train/Test Split**: 80/20
    - **Target**: Binary classification (<=50K or >50K annual income)
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p><strong>ML Assignment 2</strong> | M.Tech (AIML/DSE) | Machine Learning</p>
    <p><i>Interactive Classification Dashboard</i></p>
</div>
""", unsafe_allow_html=True)