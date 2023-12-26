# Quicknode Data Pipeline

Background
This Python script interacts with the Quicknode Flipside Query API to retrieve and process blockchain data. The script provides a simple framework to query the API, process the response data, and execute a data pipeline for further analysis.

Prerequisites
Before running the script, make sure you have the following prerequisites:

Python 3.x installed

Required Python packages installed. Install them using:

`pip install requests python-dotenv`
Quicknode Flipside API Key: Obtain your API key from Quicknode and set it in the .env file as `QUICKNODE_FLIPSIDE_API_KEY.`

How to Run
Clone the repository:

`git clone https://github.com/TechieTeeee/Quicknode_Datapipeline.git`
cd Quicknode_Datapipeline
Install dependencies:

Install the requirements.

Set your Quicknode Flipside API key:

Create a .env file in the project root and add:

env
`QUICKNODE_FLIPSIDE_API_KEY=your_api_key_here`

Execute the script:

Run the script using:

`python data_pipeline.py`
The script will execute the example queries defined in the main function. Modify the queries as needed.

Custom Queries
To run custom queries, edit the query variable in the main function in data_pipeline.py. Replace the example queries with your own.

Data Processing
The process_data function in data_pipeline.py is a placeholder for your specific data processing logic. Customize this function based on the structure of the data returned by your queries.

Error Handling
If an error occurs during the API request or processing, detailed error messages will be displayed in the console.
