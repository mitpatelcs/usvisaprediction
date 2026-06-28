import numpy as np
THRESHOLD = 0.45

def predict(model,X):
    """
    Predict visa status using the trained model.
    """
    
    # Predict probabilities
    probabilities=model.predict_proba(X)[:, 1]
    
    # Apply threshold
    predictions = np.where(probabilities>=THRESHOLD, 1, 0)
    
    return predictions