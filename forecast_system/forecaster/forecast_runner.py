# import joblib
# import importlib
# import pandas as pd
# from .utils.warehouse_api import get_current_stock

# def forecast_for_product(product_name: str):
#     # Load model and feature pipeline
#     model = joblib.load(f"forecaster/models/{product_name}.joblib")
#     features = importlib.import_module(f"forecaster.feature_pipelines.{product_name}")

#     # Generate base DataFrame with dates
#     df = pd.DataFrame({'ds': pd.date_range(start=pd.Timestamp.today(), periods=30)})

#     df = features.prepare_features(df)
#     forecast = model.predict(df)

#     # Get current stock
#     stock = get_current_stock(product_name)
#     total_forecast = forecast['yhat'].sum()
#     shortage = max(0, total_forecast - stock)

#     return {
#         "product": product_name,
#         "current_stock": stock,
#         "forecasted_demand_next_30_days": round(total_forecast, 2),
#         "stock_shortfall": round(shortage, 2),
#         "daily_predictions": forecast[['ds', 'yhat']].rename(columns={'ds': 'date', 'yhat': 'predicted'}).to_dict('records')
#     }
