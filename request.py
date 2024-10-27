import requests
import time

# Replace with your Load Balancer's DNS name
load_balancer_url = "http://asg1-lb1-1191554957.ap-south-1.elb.amazonaws.com"

def send_request():
    try:
        response = requests.get(load_balancer_url)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def main():
    # Loop to continuously send requests
    while True:
        send_request()
        # Wait before sending the next request
        time.sleep(2)

if __name__ == "__main__":
    main()
