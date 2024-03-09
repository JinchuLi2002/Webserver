import matplotlib.pyplot as plt
import requests
from multiprocessing import Pool


def send_request(url):
    """Function to send a single request."""
    try:
        response = requests.get(url)
        return response.status_code == 200
    except Exception as e:
        print(e)
        return False


def stress_test_process(concurrent_requests):
    """Stress test using multiple processes."""
    urls = [
        'http://10.0.0.184:5500/',
        'http://10.0.0.184:5500/page2',
        'http://10.0.0.184:5500/page3',
        'http://10.0.0.184:5500/page4',
        'http://10.0.0.184:5500/page5',
    ] * concurrent_requests  # Increase list size based on concurrent requests

    with Pool(processes=concurrent_requests) as pool:
        results = pool.map(send_request, urls)

    success_rate = sum(results) / len(results)
    return success_rate


if __name__ == '__main__':
    concurrent_requests_list = [1, 5, 10, 20, 40, 80, 100, 200, 400, 600]
    success_rates = []

    for concurrent_requests in concurrent_requests_list:
        success_rate = stress_test_process(concurrent_requests)
        success_rates.append(success_rate)
        print(
            f"Concurrent Requests: {concurrent_requests}, Success Rate: {success_rate}")

    plt.figure(figsize=(10, 6))
    plt.plot(concurrent_requests_list, success_rates,
             marker='o', linestyle='-', color='blue')
    plt.title('Success Rate vs. Concurrent Requests')
    plt.xlabel('Concurrent Requests')
    plt.ylabel('Success Rate')
    # Optional: Use a logarithmic scale for x-axis if your concurrent_requests_list spans large ranges
    plt.xscale('log')
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()  # Adjust the padding between and around subplots
    plt.show()
