from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    # Replace 'your_api_key' with your actual API key
    api_key = "REMOVED_REMOVED_SENSITIVE_DATA"
    prompt_text = request.form['prompt']

    # Define the API endpoint
    url = 'https://api.openai.com/v1/images/generations'

    # Set up the headers with the API key and content type
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    # Set up the data to send in the request
    data = {
        'prompt': prompt_text,
        'num_images': 1,
        'size': '256x256',
        'response_format': 'url',
    }

    # Send the request to the API
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        # Parse the response JSON
        response_data = response.json()

        # Get the generated image URL
        image_url = response_data['data'][0]['url']

        return {'url': image_url}
    else:
        return {'error': f'Error: {response.status_code} - {response.text}'}

if __name__ == '__main__':
    app.run(debug=True)
