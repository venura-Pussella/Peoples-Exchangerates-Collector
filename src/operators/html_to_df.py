import pandas as pd
from io import StringIO
from datetime import datetime

# Currency code mapping
currency_code_mapping = {
    "US Dollars": "USD",
    "Japanese Yen": "JPY",
    "British Pound Sterling": "GBP",
    "Euro": "EUR",
    "Australian Dollar": "AUD",
    "Thai Baht": "THB",
    "Singapore Dollar": "SGD",
    "Swedish Krona": "SEK",
    "Saudi Riyal": "SAR",
    "Qatari Rial": "QAR",
    "Omani Rial": "OMR",
    "New Zealand Dollar": "NZD",
    "Norwegian Krone": "NOK",
    "Malaysian Ringgit": "MYR",
    "Kuwaiti Dinar": "KWD",
    "Jordanian Dinar": "JOD",
    "Indian Rupee": "INR",
    "Hong Kong Dollar": "HKD",
    "Danish Krone": "DKK",
    "Chinese Yuan": "CNY",
    "Swiss Franc": "CHF",
    "Canadian Dollar": "CAD",
    "Bahraini Dinar": "BHD",
    "UAE Dirham": "AED"
}

def process_html_content(html_content):
    html_file_like = StringIO(html_content)
    df = pd.read_html(html_file_like)[0]

    df.columns = ['_'.join(col).strip() for col in df.columns.values]
    # Reset the index of the DataFrame
    df1 = df.reset_index()
    
    # Drop the first column of the DataFrame
    df_dropped = df1.drop(df1.columns[[0, 1]], axis=1)
    df_dropped.columns = ['Currency', 'Currency_Buying_Rate', 'Currency_Selling_Rate','TCs_Drafts_Buying_Rate',
                          'TCs_Drafts_Selling_Rate','Telegraphic_Transfers_Buying_Rate','Telegraphic_Transfers_Selling_Rate']
    
    df_dropped['Bank'] = 'Peoples'
    df_dropped['Date'] = datetime.now().strftime('%Y-%m-%d')  # today's date 
    df_dropped['Time'] = datetime.now().strftime('%H:%M:%S')  # today's time
    df_dropped['ST BANK CODE'] = '7135'
    
    # Map the currency to the corresponding code using the mapping dictionary
    df_dropped['Code'] = df_dropped['Currency'].map(currency_code_mapping)

    return df_dropped
