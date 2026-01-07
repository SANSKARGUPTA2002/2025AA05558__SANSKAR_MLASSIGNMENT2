"""
ML Assignment 2 - Classification Models Training
Dataset: Adult Income Dataset (UCI Machine Learning Repository)
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import (accuracy_score, roc_auc_score, precision_score, 
                             recall_score, f1_score, matthews_corrcoef,
                             confusion_matrix, classification_report)
import pickle
import warnings
warnings.filterwarnings('ignore')

def load_and_preprocess_data():
    """
    Load and preprocess the Adult Income dataset
    """
    # Column names for the dataset
    column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num',
                   'marital-status', 'occupation', 'relationship', 'race', 'sex',
                   'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
    
    # Load dataset from UCI repository
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
    df = pd.read_csv(url, names=column_names, na_values=' ?', skipinitialspace=True)
    
    # Handle missing values
    df = df.dropna()
    
    # Encode target variable
    df['income'] = df['income'].map({'<=50K': 0, '>50K': 1})
    
    # Separate features and target
    X = df.drop('income', axis=1)
    y = df['income']
    
    # Encode categorical variables
    label_encoders = {}
    categorical_columns = X.select_dtypes(include=['object']).columns
    
    for col in categorical_columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])
        label_encoders[col] = le
    
    # Feature scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X = pd.DataFrame(X_scaled, columns=X.columns)
    
    return X, y, label_encoders, scaler

def train_and_evaluate_models(X_train, X_test, y_train, y_test):
    """
    Train all 6 classification models and calculate evaluation metrics
    """
    # Define models
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
        'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=10),
        'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=5),
        'Naive Bayes': GaussianNB(),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10),
        'XGBoost': XGBClassifier(n_estimators=100, random_state=42, max_depth=6, 
                                eval_metric='logloss', use_label_encoder=False)
    }
    
    results = {}
    trained_models = {}
    
    print("Training and evaluating models...\n")
    print("="*80)
    
    for name, model in models.items():
        print(f"\n{name}")
        print("-"*80)
        
        # Train model
        model.fit(X_train, y_train)
        trained_models[name] = model
        
        # Make predictions
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, zero_division=0)
        recall = recall_score(y_test, y_pred, zero_division=0)
        f1 = f1_score(y_test, y_pred, zero_division=0)
        mcc = matthews_corrcoef(y_test, y_pred)
        
        # Calculate AUC
        if y_pred_proba is not None:
            auc = roc_auc_score(y_test, y_pred_proba)
        else:
            auc = 0.0
        
        # Store results
        results[name] = {
            'Accuracy': accuracy,
            'AUC': auc,
            'Precision': precision,
            'Recall': recall,
            'F1': f1,
            'MCC': mcc,
            'confusion_matrix': confusion_matrix(y_test, y_pred),
            'classification_report': classification_report(y_test, y_pred)
        }
        
        # Print metrics
        print(f"Accuracy:  {accuracy:.4f}")
        print(f"AUC Score: {auc:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall:    {recall:.4f}")
        print(f"F1 Score:  {f1:.4f}")
        print(f"MCC Score: {mcc:.4f}")
        
        # Save model
        model_filename = f'model/{name.replace(" ", "_").lower()}_model.pkl'
        with open(model_filename, 'wb') as f:
            pickle.dump(model, f)
        print(f"Model saved: {model_filename}")
    
    return results, trained_models

def print_comparison_table(results):
    """
    Print comparison table of all models
    """
    print("\n" + "="*80)
    print("MODEL COMPARISON TABLE")
    print("="*80)
    print(f"{'Model Name':<25} {'Accuracy':<10} {'AUC':<10} {'Precision':<10} {'Recall':<10} {'F1':<10} {'MCC':<10}")
    print("-"*80)
    
    for model_name, metrics in results.items():
        print(f"{model_name:<25} "
              f"{metrics['Accuracy']:<10.4f} "
              f"{metrics['AUC']:<10.4f} "
              f"{metrics['Precision']:<10.4f} "
              f"{metrics['Recall']:<10.4f} "
              f"{metrics['F1']:<10.4f} "
              f"{metrics['MCC']:<10.4f}")
    print("="*80)

def save_results_to_file(results):
    """
    Save results to a text file for README
    """
    with open('model/results.txt', 'w') as f:
        f.write("MODEL COMPARISON TABLE\n")
        f.write("="*100 + "\n")
        f.write(f"{'Model Name':<25} {'Accuracy':<12} {'AUC':<12} {'Precision':<12} {'Recall':<12} {'F1':<12} {'MCC':<12}\n")
        f.write("-"*100 + "\n")
        
        for model_name, metrics in results.items():
            f.write(f"{model_name:<25} "
                   f"{metrics['Accuracy']:<12.4f} "
                   f"{metrics['AUC']:<12.4f} "
                   f"{metrics['Precision']:<12.4f} "
                   f"{metrics['Recall']:<12.4f} "
                   f"{metrics['F1']:<12.4f} "
                   f"{metrics['MCC']:<12.4f}\n")
        
        f.write("\n\nDETAILED RESULTS\n")
        f.write("="*100 + "\n")
        
        for model_name, metrics in results.items():
            f.write(f"\n{model_name}\n")
            f.write("-"*80 + "\n")
            f.write(f"Confusion Matrix:\n{metrics['confusion_matrix']}\n\n")
            f.write(f"Classification Report:\n{metrics['classification_report']}\n")
            f.write("-"*80 + "\n")

def main():
    """
    Main function to execute the training pipeline
    """
    print("="*80)
    print("ML ASSIGNMENT 2 - CLASSIFICATION MODELS")
    print("Dataset: Adult Income Dataset (UCI)")
    print("="*80)
    
    # Load and preprocess data
    print("\nLoading and preprocessing data...")
    X, y, label_encoders, scaler = load_and_preprocess_data()
    print(f"Dataset shape: {X.shape}")
    print(f"Features: {X.shape[1]}")
    print(f"Instances: {X.shape[0]}")
    print(f"Target distribution:\n{y.value_counts()}")
    
    # Split data
    print("\nSplitting data (80% train, 20% test)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"Training set: {X_train.shape[0]} samples")
    print(f"Test set: {X_test.shape[0]} samples")
    
    # Save test data for Streamlit app
    test_data = X_test.copy()
    test_data['income'] = y_test
    test_data.to_csv('test_data.csv', index=False)
    print(f"\nTest data saved to 'test_data.csv' for Streamlit app")
    
    # Save scaler and label encoders
    with open('model/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    with open('model/label_encoders.pkl', 'wb') as f:
        pickle.dump(label_encoders, f)
    
    # Train and evaluate models
    results, trained_models = train_and_evaluate_models(X_train, X_test, y_train, y_test)
    
    # Print comparison table
    print_comparison_table(results)
    
    # Save results
    save_results_to_file(results)
    print("\n✓ Results saved to 'model/results.txt'")
    print("\n✓ All models trained and saved successfully!")
    print("\n" + "="*80)

if __name__ == "__main__":
    main()