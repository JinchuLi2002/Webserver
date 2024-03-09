import requests
import time
import random

# URLs to access randomly
urls = [
    'http://10.0.0.184:5500/',
    'http://10.0.0.184:5500/page2',
    'http://10.0.0.184:5500/page3',
    'http://10.0.0.184:5500/page4',
    'http://10.0.0.184:5500/page5',
]

number_of_requests = 100  # Total number of requests to send
latencies = []  # To store the latency of each request

start_time = time.time()  # Start time of the test

for _ in range(number_of_requests):
    url = random.choice(urls)  # Select a random URL to access
    request_start_time = time.time()  # Start time of the request
    response = requests.get(url)
    request_end_time = time.time()  # End time of the request

    latency = request_end_time - request_start_time
    latencies.append(latency)

end_time = time.time()  # End time of the test

# Calculate metrics
total_time = end_time - start_time
average_latency = sum(latencies) / number_of_requests
throughput = number_of_requests / total_time  # Requests per second

print(f"Total time for {number_of_requests} requests: {total_time} seconds")
print(f"Average latency per request: {average_latency} seconds")
print(f"Throughput: {throughput} requests per second")
