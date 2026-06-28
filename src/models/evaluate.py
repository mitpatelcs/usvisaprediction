from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,classification_report

def evaluate_model(y_true, y_pred):
    """
    Evaluate model performance.
    """
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    
    print(classification_report(y_true, y_pred))
    
    return accuracy, precision, recall, f1