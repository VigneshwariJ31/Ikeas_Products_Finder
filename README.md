# IKEA Product Search

## Product Search Platform

This repository contains the source code for the **IKEA Product Search Platform**, which allows users to search for IKEA products based on various criteria like category or keyword.

The backend is built with **Flask** (or any preferred backend framework), and the frontend is an HTML page that allows users to enter search queries and filter results by product category or keyword.

## Project Structure

### Frontend
- **ikea_ui.html**: The main HTML page that provides the search interface for users.

### Backend
- **app.py / ikea_app.py**: The backend script that handles the search functionality. It provides endpoints like `/get_products/{category}` and `/search_products` for searching IKEA products.
- **ikea_products.json**: A JSON file containing mock product data that the backend can return when a user performs a search.

### Features
- **Search by Category**: Users can search for products by selecting a category from a dropdown list.
- **Search by Keyword**: Users can search for products using a keyword in the product name or description.
- **Product Details**: Each search result includes a link to view the product page with details like price, description, dimensions, etc.
- **Responsive UI**: The user interface is designed to be responsive and works well on various devices.

## Setup Elasticsearch and Kibana (Manual Installation)

Follow these steps to install and run Elasticsearch and Kibana on your local machine:

### 1. Download and Install Elasticsearch and Kibana

#### Download Elasticsearch:
Visit the official [Elasticsearch download page](https://www.elastic.co/downloads/elasticsearch) and download the appropriate version for your operating system.

#### Download Kibana:
Visit the official [Kibana download page](https://www.elastic.co/downloads/kibana) and download the version that matches your Elasticsearch version.

### 2. Run Elasticsearch and Kibana in the Background

- Extract the downloaded ZIP files for both Elasticsearch and Kibana to your desired directories.
- Start **Elasticsearch**:
  - Navigate to the `bin` folder inside the extracted Elasticsearch directory.
  - Run the following command:
    - For **Windows**: `elasticsearch.bat`
    - For **macOS/Linux**: `./bin/elasticsearch`
  This will start Elasticsearch, and it will run in the background, listening on port 9200.

- Start **Kibana**:
  - Navigate to the `bin` folder inside the extracted Kibana directory.
  - Run the following command:
    - For **Windows**: `kibana.bat`
    - For **macOS/Linux**: `./bin/kibana`
  This will start Kibana, and it will run in the background, accessible through [http://localhost:5601](http://localhost:5601).

### 3. Access Elasticsearch and Kibana

#### Elasticsearch:
Once Elasticsearch is running, you can test it by navigating to [http://localhost:9200](http://localhost:9200) in your browser.

#### Kibana:
Open your browser and go to [http://localhost:5601](http://localhost:5601). You will be prompted to log in with your username, password, and authentication token (if applicable).
Once logged in, Kibana will allow you to visualize and interact with your data stored in Elasticsearch.

## Setup

### 1. Prerequisites
- **Python 3.x**: Ensure you have Python 3.x installed on your system.
- **Flask**: The backend is built using Flask. Install Flask by running the following command:
  ```bash
  pip install flask

### 2. Instructions to Upload JSON Data to Elasticsearch
#### 1. Ensure Elasticsearch is Running
Make sure Elasticsearch is running on http://localhost:9200 and Kibana on http://localhost:5601.
#### 2. Place JSON Data and Python Script
 - Ensure your JSON data file (data/ikea_products.json) is in the project directory.
 - Ensure your Python script (app.py/Load_ikea_products.py) is ready to load data into Elasticsearch.
#### 3. Run the Python Script
In your terminal or command line, navigate to the project directory and run the Python script:
  python Load_Ikea_products.py
#### 4. Verify Data in Kibana
Go to Kibana (http://localhost:5601), navigate to Discover, and check the uploaded data in your Elasticsearch index.
### 3. Run the Flask Server
Start the Flask application by running the following command:
python Ikea_app.py
By default, Flask runs on http://127.0.0.1:5000. Open this URL in your browser to access the product search platform.
### 4. View the Product Search Interface
Once the server is running, navigate to the following URL in your browser:
http://127.0.0.1:5000
You should see the IKEA product search interface where you can search for products by category or keyword.
## Folder Structure
![image_alt](https://github.com/VigneshwariJ31/Ikeas_Products_Finder/blob/2ca8e22aaa6b9a2d121fe31f8c35f3c9dd08b6f7/Folder%20structure.png)
## Main Page
![image_alt](https://github.com/VigneshwariJ31/Ikeas_Products_Finder/blob/1920f0ad0f85eb7d24150e7d31d4b350939f534c/Main%20Screen.png)
## Search by category 
![image_alt](https://github.com/VigneshwariJ31/Ikeas_Products_Finder/blob/1920f0ad0f85eb7d24150e7d31d4b350939f534c/Search_by_category.png)
## Search by keyword 
![image_alt](https://github.com/VigneshwariJ31/Ikeas_Products_Finder/blob/1920f0ad0f85eb7d24150e7d31d4b350939f534c/Search_by_Keyword.png)
## Contributing
Feel free to fork this repository, open issues, and submit pull requests. Contributions are welcome to enhance the product search experience or add more features.
## License
This project is open-source and available under the MIT License.
