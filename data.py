import pandas as pd

def load_data():
    data = {
        "city": ["Kyiv", "Lviv", "Odesa", "Kyiv", "Lviv", "Odesa"],
        "month": ["Jan", "Jan", "Jan", "Feb", "Feb", "Feb"],
        "sales": [1200, 980, 500, 1500, 1100, 7001]
    }
    return pd.DataFrame(data)