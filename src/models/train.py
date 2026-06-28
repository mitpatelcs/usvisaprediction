from xgboost import XGBClassifier


def train_model(X_train, y_train):
    """
    Train the final XGBoost model.
    """

    model = XGBClassifier(
        objective="binary:logistic",
        n_estimators=110,
        max_depth=10,
        learning_rate=0.024563676146662234,
        subsample=0.984871310317357,
        colsample_bytree=0.6741976585164232,
        random_state=42,
        eval_metric="logloss"
    )

    model.fit(X_train, y_train)

    return model