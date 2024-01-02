# app.py
from flask import Flask, render_template_string, render_template
from bs4 import BeautifulSoup as BS
import requests as req
import pandas as pd
from tabulate import tabulate


app = Flask(__name__)

# Scraping code
url = "https://www.businesstoday.in/latest/economy"
webpage = req.get(url)
trav = BS(webpage.content, "html.parser")

@app.route('/tax-calculation')
def tax_calculation():
    return render_template('tax_calculation.html')

@app.route('/portfolio-management')
def portfolio_management():
    return render_template('portfolio_management.html')

@app.route('/stock-analysis')
def stock_analysis():
    return render_template('stock_analysis.html')
@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <link href="https://fonts.googleapis.com/css?family=Archivo+Black&display=swap" rel="stylesheet">
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                                  
                        
                :root {
                  --shadow-color: #000000;
                  --shadow-color-light: #34EC20;
                }

                * {
                  padding: 0;
                  margin: 0;
                  box-sizing: border-box;
                }

                body {
                  background-color: #D6FED2;
                  opacity: 0.8;
                  background-image: radial-gradient(#000000 0.5px, #D6FED2 0.5px);
                  background-size: 10px 10px;
                  margin: 0;
                  font-family: 'Arial', sans-serif;
                }
                table, td, th {
                    border: 1px solid black;
                    text-align: centre;
                    }
                p {
                  font-size: 65px;
                  text-transform: uppercase;
                  font-family: "Archivo Black", "Archivo", sans-serif;
                  font-weight: normal;
                  display: block;
                  height: auto;
                  text-align: center;
                }

                .logo-1 {
                  color: white;
                  animation: neon 3s infinite;
                }

                @keyframes neon {
                  0% {
                    text-shadow: -1px -1px 1px var(--shadow-color-light), -1px 1px 1px var(--shadow-color-light), 1px -1px 1px var(--shadow-color-light), 1px 1px 1px var(--shadow-color-light),
                    0 0 3px var(--shadow-color-light), 0 0 10px var(--shadow-color-light), 0 0 20px var(--shadow-color-light),
                    0 0 30px var(--shadow-color), 0 0 40px var(--shadow-color), 0 0 50px var(--shadow-color), 0 0 70px var(--shadow-color), 0 0 100px var(--shadow-color), 0 0 200px var(--shadow-color);
                  }
                  50% {
                    text-shadow: -1px -1px 1px var(--shadow-color-light), -1px 1px 1px var(--shadow-color-light), 1px -1px 1px var(--shadow-color-light), 1px 1px 1px var(--shadow-color-light),
                    0 0 5px var(--shadow-color-light), 0 0 15px var(--shadow-color-light), 0 0 25px var(--shadow-color-light),
                    0 0 40px var(--shadow-color), 0 0 50px var(--shadow-color), 0 0 60px var(--shadow-color), 0 0 80px var(--shadow-color), 0 0 110px var(--shadow-color), 0 0 210px var(--shadow-color);
                  }
                  100% {
                    text-shadow: -1px -1px 1px var(--shadow-color-light), -1px 1px 1px var(--shadow-color-light), 1px -1px 1px var(--shadow-color-light), 1px 1px 1px var(--shadow-color-light),
                    0 0 3px var(--shadow-color-light), 0 0 10px var(--shadow-color-light), 0 0 20px var(--shadow-color-light),
                    0 0 30px var(--shadow-color), 0 0 40px var(--shadow-color), 0 0 50px var(--shadow-color), 0 0 70px var(--shadow-color), 0 0 100px var(--shadow-color), 0 0 200px var(--shadow-color);
                  }
                }
                                  table {
  border-collapse: collapse;
                                  
}td {
  text-align: center;
    padding:2px;
}

                /* Dropdown Button */
                .dropbtn {
                  font-family: "Archivo Black", "Archivo", sans-serif;
                  background-color: #34EC20;
                  color: white;
                  padding: 16px;
                  font-size: 16px;
                  border: none;
                }
                .mydiv{
                                  -webkit-box-shadow:0px 0px 10px 3px #00f900 ;
                -moz-box-shadow:0px 0px 10px 3px #00f900 ;
                box-shadow:0px 0px 10px 3px #000000 ;
                                  padding:20px;
                                  margin:20px;
                
                }
                .mydiv1{
                                  -webkit-box-shadow:0px 0px 10px 3px #00f900 ;
                -moz-box-shadow:0px 0px 10px 3px #00f900 ;
                box-shadow:0px 0px 10px 3px #000000 ;
                                  padding:20px;
                                  margin:20px;
                                  width:30%;
                
                }
                .mydiv2{
                                  -webkit-box-shadow:0px 0px 10px 3px #00f900 ;
                -moz-box-shadow:0px 0px 10px 3px #00f900 ;
                box-shadow:0px 0px 10px 3px #000000 ;
                                  padding:20px;
                                  margin:20px;
                                  width:30%;
                
                }
                                  

                .myButton {
                  font-family: "Archivo Black", "Archivo", sans-serif;                           
                  box-shadow: 0px 10px 14px -7px #5feb1e;
                  background:linear-gradient(to bottom, #89db60 5%, #63d42a 100%);
                  background-color:#89db60;
                  border-radius:4px;
                  border:1px solid #4b8f29;
                  display:inline-block;
                  cursor:pointer;
                  color:#ffffff;
                  font-family:Arial;
                  font-size:13px;
                  font-weight:bold;
                  padding:8px 17px;
                  text-decoration:none;
                  text-shadow:0px 1px 0px #000000;
                }

                .myButton:hover {
                  background:linear-gradient(to bottom, #63d42a 5%, #89db60 100%);
                  background-color:#63d42a;
                }

                .myButton:active {
                  position:relative;
                  top:1px;
                }

                /* The container <div> - needed to position the dropdown content */
                .dropdown {
                  position: relative;
                  display: inline-block;
                }

                /* Dropdown Content (Hidden by Default) */
                .dropdown-content {
                  display: none;
                  position: absolute;
                  background-color: #f1f1f1;
                  min-width: 160px;
                  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                  z-index: 1;
                }

                /* Links inside the dropdown */
                .dropdown-content a {
                  color: black;
                  padding: 12px 16px;
                  text-decoration: none;
                  display: block;
                }

                /* Change color of dropdown links on hover */
                .dropdown-content a:hover {background-color: #ddd;}

                /* Show the dropdown menu on hover */
                .dropdown:hover .dropdown-content {display: block;}

                /* Change the background color of the dropdown button when the dropdown content is shown */
                .dropdown:hover .dropbtn {background-color: #3e8e41;}

                .dashboard {
                  padding: 20px;
                }

                .title-bar {
                  background-color: #333;
                  color: white;
                  padding: 10px;
                  display: flex;
                  justify-content: space-between;
                  align-items: center;
                }

                .menu-icon {
                  font-size: 24px;
                  cursor: pointer;
                }

                h1 {
                  margin: 0;
                }

                .scrollable-div {
                  overflow-y: auto;
                  max-height: 400px;
                  border: 1px solid #000000;
                  padding: 10px;
                  margin-top: 20px;
                                  
                }
            </style>
            <title>Finsuite Dashboard</title>
        </head>
        <body>
            <div class="dashboard">
                <div class="title-bar">
                    <div class="dropdown">
                        <button class="dropbtn">Menu</button>
                        <div class="dropdown-content">
                            <a href="#">View Portfolio</a>
                            <a href="#">Analyse Stock</a>
                            <a href="/tax-calculation">Tax calculator</a>
                        </div>
                    </div>
                    
                    <h1 class="logo-1">Finsuite</h1>
                </div >
                <div class="mydiv"> <h2>Latest Financial News</h2>
                <div class="scrollable-div" id="outputContainer"></div></div>
                                  
                                  <div class="mydiv1"> <h2>Latest Global Indices</h2>
                <div class="scrollable-div" id="outputContainer2"></div></div>
                                  </div>
                                  <div class="mydiv2">Latest Indian Indices<div class="scrollable-div" id="outputContainer3"></div></div>
            
            
            <script>
                document.addEventListener('DOMContentLoaded', function () {
                    // Function to fetch and display the output
                    function fetchOutput() {
                        fetch('/get_output')  // Route to fetch output from Flask app
                            .then(response => response.text())
                            .then(data => {
                                const outputContainer = document.getElementById('outputContainer');
                                outputContainer.innerHTML = data;
                            })
                            .catch(error => console.error('Error fetching output:', error));
                    }

                    // Initial fetch when the page loads
                    fetchOutput();

                    // Fetch output every 5 minutes (adjust as needed)
                    setInterval(fetchOutput, 5 * 60 * 1000);
                });
                                  
                                  document.addEventListener('DOMContentLoaded', function () {
                    // Function to fetch and display the output
                    function fetchOutput() {
                        fetch('/get_indices')  // Route to fetch output from Flask app
                            .then(response => response.text())
                            .then(data => {
                                const outputContainer = document.getElementById('outputContainer2');
                                outputContainer.innerHTML = data;
                            })
                            .catch(error => console.error('Error fetching output:', error));
                    }

                    // Initial fetch when the page loads
                    fetchOutput();

                    // Fetch output every 5 minutes (adjust as needed)
                    setInterval(fetchOutput, 5 * 60 * 1000);
                });
                                  document.addEventListener('DOMContentLoaded', function () {
                    // Function to fetch and display the output
                    function fetchOutput() {
                        fetch('/get_nifty')  // Route to fetch output from Flask app
                            .then(response => response.text())
                            .then(data => {
                                const outputContainer = document.getElementById('outputContainer3');
                                outputContainer.innerHTML = data;
                            })
                            .catch(error => console.error('Error fetching output:', error));
                    }

                    // Initial fetch when the page loads
                    fetchOutput();

                    // Fetch output every 5 minutes (adjust as needed)
                    setInterval(fetchOutput, 5 * 60 * 1000);
                });
            </script>
        </body>
        </html>
    ''')

@app.route('/get_output')
def get_output():
    output = ""
    M = 1
    for link in trav.find_all('a'):
        if (
            str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
            and len(link.string) > 35
        ):
            output += str(M) + ". " + link.string + "<br><br>"
            M += 1
    return output

@app.route('/get_indices')
def get_indeices():

    url = 'https://finance.yahoo.com/world-indices/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/681.3.9'
    }
    response = req.get(url, headers=header)
    df = pd.read_html(response.content)[0]  # Assuming the table you want is the first one

    # Select only the columns you need
    selected_columns = ['Name', 'Last Price', '% Change']
    df_selected = df[selected_columns]

    # Convert selected DataFrame to HTML table
    html_table = df_selected.to_html(index=False)

    return(html_table)
@app.route('/get_nifty')
def get_nifty():

  url = "https://www.tickertape.in/indices/nifty-50-index-.NSEI"
  header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/681.3.9'
    }
  try:
      response = req.get(url)
      response.raise_for_status()

      soup = BS(response.text, 'html.parser')

      # Find elements with class containing "current-price" and "change percentage-value"
      current_price_element = soup.find('span', class_=lambda x: x and 'current-price' in x)
      percent_change_element = soup.find('span', class_=lambda x: x and 'change percentage-value' in x)

      if current_price_element and percent_change_element:
          current_price = current_price_element.text.strip()
          percent_change = percent_change_element.text.strip()

          return (f"<table><tr><td>Current Price: </td><td>{current_price} </td>")
      else:
          print("Current price or percent change element not found on the page.")
  except req.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")




if __name__ == '__main__':
    app.run(debug=True)

