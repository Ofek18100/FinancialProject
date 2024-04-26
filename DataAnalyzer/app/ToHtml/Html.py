def touple_to_html_table(touples_array):
        
    # Create an HTML string with a basic table structure and some minimal styling
    HTML_PAGE = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Stock Analysis</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            table {
                border-collapse: collapse;
                width: 100%;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>Stock Analysis</h1>
        <table>
            <thead>
                <tr>
                    <th>Ticker Symbol</th>
                    <th>Distance from SMA</th>
                </tr>
            </thead>
            <tbody>
    """
    
    # Populate the table rows with stock data
    for stock in touples_array:
        color = "green" if stock[1] > 0 else "red"
        HTML_PAGE += f"""
        
            <tr>
                <td>{stock[0]}</td>
                <td style='color: {color};'>{stock[1]}%</td>
            </tr>
        """
    
    # Close the HTML tags
    HTML_PAGE += """
            </tbody>
        </table>
    </body>
    </html>
    """
    
    return HTML_PAGE
