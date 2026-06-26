import pandas as pd
REFERENCE_YEAR=2026

def preprocess_data(df:pd.DataFrame)->pd.DataFrame:
    """
    Apply data cleaning and feature engineering.
    
    """
    df=df.copy()
    
    # Remove unnecessary columns
    cols_to_drop = [
        "case_id",
        "requires_job_training"
    ]
    df.drop(columns=cols_to_drop, inplace=True, errors='ignore')
    
    # Fix negative employee count
    df['no_of_employees']=df['no_of_employees'].abs()
    
    # Convert wage to annual salary
    wage_multiplier = {
        "Hour": 2080,
        "Week": 52,
        "Month": 12,
        "Year": 1
    }
    
    df["prevailing_wage_annual"] = (df["prevailing_wage"]*df["unit_of_wage"].map(wage_multiplier))
    
    # Drop original wage columns
    df.drop(columns=["prevailing_wage", "unit_of_wage"],inplace=True, errors="ignore")
    
    # Create company age
    df["company_age"] = REFERENCE_YEAR - df["yr_of_estab"]
    
    # Drop original year column
    df.drop(columns=["yr_of_estab"],inplace=True,errors="ignore")
    
    return df
