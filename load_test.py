import requests
import time
from concurrent.futures import ThreadPoolExecutor

# Function to send HTTP requests
def send_request(url):
    try:
        response = requests.get(url)
        # You can add more logic here to analyze the response if needed
        print(f"Request to {url} returned with status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending request to {url}: {e}")

# Main function to run load test
def run_load_test(url, concurrent_users):
    print(f"Starting load test for {url} with {concurrent_users} concurrent users")
    
    # Using ThreadPoolExecutor to send multiple requests concurrently
    with ThreadPoolExecutor(max_workers=concurrent_users) as executor:
        # Infinite loop to keep sending requests until manually stopped
        while True:
            # Submitting tasks to the executor
            executor.map(send_request, [url] * concurrent_users)
            time.sleep(1)  # Adjust the delay between requests if needed

if __name__ == "__main__":
    # URL to test
    url_to_test = "https://buddydeals.in/"
    
    # Number of concurrent users
    concurrent_users = 100
    
    # Run the load test
    run_load_test(url_to_test, concurrent_users)
