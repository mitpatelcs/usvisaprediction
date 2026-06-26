import joblib
import pandas as pd
PREPROCESSOR_PATH="artifacts/preprocessor.pkl"

def build_features(df:pd.DataFrame)->pd.DataFrame:
    """
    Transform the data using the trained preprocessor.
    
    """
    
    # Load the trained preprocessor
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    
    # Transform the data
    transformed_data = preprocessor.transform(df)
    
    # Get feature names
    feature_names = preprocessor.get_feature_names_out()
    
    # Return the transformed data and feature names as a DataFrame
    return pd.DataFrame(transformed_data, columns=feature_names)
