import requests

# Replace 'your_api_key' with your actual API key
api_key = 'your_api_key'

# Set your prompt text for the image generation
prompt_text = 'Generate an image of a sunset over the ocean.'

# Define the API endpoint
url = 'https://api.openai.com/v1/images/generations'

# Set up the headers with the API key and content type
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

# Set up the data to send in the request, including the prompt text and other options
data = {
    'prompt': prompt_text,
    'num_images': 1,
    'size': '256x256',
    'response_format': 'url',
}

# Send the request to the API
response = requests.post(url, json=data, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON
    response_data = response.json()

    # Get the generated image URL
    image_url = response_data['data'][0]['url']

    print(f'Generated image URL: {image_url}')
else:
    print(f'Error: {response.status_code} - {response.text}')
