import requests
import json
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("QUICKNODE_FLIPSIDE_API_KEY")  # Retrieve API key from environment variable

def query_flipside_api(query):
    """Queries the Quicknode Flipside Query API with the provided query string.

    Args:
        query (str): The query string to execute.

    Returns:
        dict: The parsed JSON response from the API.

    Raises:
        Exception: If the API request fails or the response is invalid.
    """

    url = "https://api.flipsidecrypto.com/api/v2/queries"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {"query": query}

    response = requests.post(url, headers=headers, json=data)

    try:
        response.raise_for_status()  # Raise an exception for non-200 status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as err:
        raise Exception(f"API request failed: {err}")
    except json.JSONDecodeError as err:
        raise Exception(f"Invalid JSON response: {err}")

def process_data(data):
    """Processes the data retrieved from the API.

    This function should be implemented to handle the specific data structure and processing requirements of your pipeline.

    Args:
        data (dict): The parsed JSON response from the API.

    Returns:
        Any: The processed data in the desired format.
    """

    # Implement your data processing logic here
    # ...

    # Example:
    processed_data = [item["value"] for item in data["data"]]
    return processed_data

def main():
    """Main function to execute the data pipeline."""

    # Example queries:

    # Aggregation and sorting
    query = "SELECT token_address, SUM(value) AS total_volume FROM erc20_transfers WHERE chain_id = 137 GROUP BY token_address ORDER BY total_volume DESC LIMIT 10"

    # Trend analysis
    query = "SELECT date_trunc('day', block_timestamp) AS day, COUNT(*) AS daily_transactions FROM polygon_blocks WHERE block_timestamp >= '2023-12-01' AND block_timestamp < '2023-12-26' GROUP BY day ORDER BY day"

    try:
        data = query_flipside_api(query)
        processed_data = process_data(data)

        # Do something with the processed data, e.g., store it, visualize it, etc.
        # ...

    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()
