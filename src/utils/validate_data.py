import great_expectations as ge
from datetime import date


def validate_data(df):
    """
    Validate the US Visa dataset using Great Expectations.
    """

    ge_df = ge.dataset.PandasDataset(df)

    # Required Columns
    required_columns = [
        "case_id",
        "continent",
        "education_of_employee",
        "has_job_experience",
        "requires_job_training",
        "no_of_employees",
        "yr_of_estab",
        "region_of_employment",
        "prevailing_wage",
        "unit_of_wage",
        "full_time_position",
        "case_status",
    ]

    for col in required_columns:
        ge_df.expect_column_to_exist(col)
        ge_df.expect_column_values_to_not_be_null(col)

    # Unique Case ID
    ge_df.expect_column_values_to_be_unique("case_id")

    # Categorical Validation
    ge_df.expect_column_values_to_be_in_set(
        "case_status",
        ["Certified", "Denied"]
    )

    ge_df.expect_column_values_to_be_in_set(
        "has_job_experience",
        ["Y", "N"]
    )

    ge_df.expect_column_values_to_be_in_set(
        "requires_job_training",
        ["Y", "N"]
    )

    ge_df.expect_column_values_to_be_in_set(
        "full_time_position",
        ["Y", "N"]
    )

    ge_df.expect_column_values_to_be_in_set(
        "education_of_employee",
        ["High School", "Bachelor's", "Master's", "Doctorate"]
    )

    ge_df.expect_column_values_to_be_in_set(
        "unit_of_wage",
        ["Hour", "Week", "Month", "Year"]
    )

    # Numeric Validation
    ge_df.expect_column_values_to_be_between(
        "prevailing_wage",
        min_value=0
    )

    ge_df.expect_column_values_to_be_between(
        "yr_of_estab",
        min_value=1800,
        max_value=date.today().year
    )

    # Run validation
    results = ge_df.validate()

    failed_expectations = [
        r["expectation_config"]["expectation_type"]
        for r in results["results"]
        if not r["success"]
    ]

    return results["success"], failed_expectations