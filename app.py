from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Temporary storage for comments
comments = []

# Routes

@app.route('/')
def hello_world():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello Flask!</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
            }

            .container {
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }

            h1 {
                color: #333;
                text-align: center;
            }

            p {
                color: #666;
                text-align: justify;
            }

            .button {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                border-radius: 5px;
                transition: background-color 0.3s;
                cursor: pointer;
            }

            .button:hover {
                background-color: #45a049;
            }

            .weather-container {
                margin-top: 20px;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }

            .comments-container {
                margin-top: 20px;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }

            .message-container {
                margin-top: 20px;
                padding: 10px;
                background-color: #eaeaea;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, I'm telling you the weather :)</h1>
            <br>                        
            <p>Hi, I am a cute weather app. I will unfortunately not live long, because I was built for testing purposes.</p>
            <p>For the time I am going to be alive, I will try to be cute.</p>
            <p>Can you please be sweet to me too?</p>
            <br>
            <a href="https://home.openweathermap.org" class="button">Click Me To Get To openweathermap.org</a>
            <a href="https://www.por.com" class="button">Click Me if you want mu Forecast</a>

            <div class="weather-container">
                <h2>Today's Weather in Zurich</h2>
                <div id="weather-info"></div>
                </div>

            <div class="comments-container">
                <h2>Comments</h2>
                <form id="comment-form">
                    <textarea id="comment-text" rows="4" cols="50" placeholder="Write your comment here..."></textarea><br>
                    <button type="submit" class="button">Post Comment</button>
                </form>
                <div id="comments-list"></div>
            </div>
        </div>

        <script>
            document.addEventListener("DOMContentLoaded", function() {
                fetchWeather(); // Fetch weather data when the page loads
                fetchComments(); // Fetch comments when the page loads
            });

            // Function to fetch weather data and update the weather section
            function fetchWeather() {
                fetch('/api/weather')
                .then(response => response.json())
                .then(data => {
                    const weatherInfo = document.getElementById('weather-info');
                    weatherInfo.innerHTML = `<p><i class="fas fa-thermometer-half"></i> Temperature: ${data.temperature}°C</p>
                                            <p><i class="fas fa-cloud"></i> Description: ${data.description}</p>`;

                    // Add custom message based on temperature condition
                    const messageContainer = document.createElement('div');
                    messageContainer.classList.add('message-container');

                    if (data.temperature > 20) {
                        messageContainer.innerHTML = "<p>Advice: Immediately go out sunbathing!</p>";
                    } else {
                        messageContainer.innerHTML = "<p>Advice: Stay at home and do coding. Your life is done anyway.</p>";
                    }

                    weatherInfo.appendChild(messageContainer);
                })
                .catch(error => {
                    console.error('Error fetching weather data:', error);
                });
            }

            // Function to fetch comments and update the comments section
            function fetchComments() {
                fetch('/api/comments')
                .then(response => response.json())
                .then(data => {
                    const commentsList = document.getElementById('comments-list');
                    commentsList.innerHTML = '';
                    data.forEach((comment, index) => {
                        const commentElement = document.createElement('div');
                        commentElement.innerHTML = `
                            <p>${comment}</p>
                            <button onclick="deleteComment(${index})">Delete</button>
                            <button onclick="editComment(${index})">Edit</button>
                        `;
                        commentsList.appendChild(commentElement);
                    });
                })
                .catch(error => {
                    console.error('Error fetching comments:', error);
                });
            }

            // Function to delete a comment
            function deleteComment(commentIndex) {
                fetch(`/api/comments/${commentIndex}`, {
                    method: 'DELETE'
                })
                .then(response => response.json())
                .then(data => {
                    alert(data.message); // Show a message indicating success or failure
                    fetchComments(); // Refresh the comments list
                })
                .catch(error => {
                    console.error('Error deleting comment:', error);
                });
            }

            // Function to edit a comment
            function editComment(commentIndex) {
                const newCommentText = prompt("Enter the new comment text:");
                if (newCommentText !== null) {
                    fetch(`/api/comments/${commentIndex}`, {
                        method: 'PATCH',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({comment: newCommentText})
                    })
                    .then(response => response.json())
                    .then(data => {
                        alert(data.message); // Show a message indicating success or failure
                        fetchComments(); // Refresh the comments list
                    })
                    .catch(error => {
                        console.error('Error editing comment:', error);
                    });
                }
            }

            // Event listener for submitting a comment
            document.getElementById('comment-form').addEventListener('submit', function(event) {
                event.preventDefault();
                const commentText = document.getElementById('comment-text').value;
                fetch('/api/comments', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({comment: commentText})
                })
                .then(response => response.json())
                .then(data => {
                    alert(data.message); // Show a message indicating success or failure
                    if (data.message === 'Comment posted successfully') {
                        document.getElementById('comment-text').value = ''; // Clear the comment textarea
                        fetchComments(); // Refresh the comments list
                    }
                })
                .catch(error => {
                    console.error('Error posting comment:', error);
                });
            });
        </script>
    </body>
    </html>
    """

@app.route('/api/weather')
def get_weather():
    OPENWEATHER_API_KEY = 'cb57b5501a9386fd3a08e9aeb015e5b6'  # Replace 'YOUR_API_KEY' with your actual OpenWeather API key
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Zurich&appid={OPENWEATHER_API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'Failed to fetch weather data from OpenWeather API'})

@app.route('/api/comments', methods=['GET', 'POST'])
def manage_comments():
    if request.method == 'POST':
        data = request.json
        comment_text = data.get('comment')
        if comment_text:
            comments.append(comment_text)
            return jsonify({'message': 'Comment posted successfully'})
        else:
            return jsonify({'error': 'Invalid comment data'})
    elif request.method == 'GET':
        return jsonify(comments)

@app.route('/api/comments/<int:comment_id>', methods=['DELETE', 'PATCH'])
def delete_or_edit_comment(comment_id):
    if request.method == 'DELETE':
        if 0 <= comment_id < len(comments):
            del comments[comment_id]
            return jsonify({'message': 'Comment deleted successfully'})
        else:
            return jsonify({'error': 'Comment not found'})
    elif request.method == 'PATCH':
        data = request.json
        new_comment_text = data.get('comment')
        if new_comment_text:
            if 0 <= comment_id < len(comments):
                comments[comment_id] = new_comment_text
                return jsonify({'message': 'Comment edited successfully'})
            else:
                return jsonify({'error': 'Comment not found'})
        else:
            return jsonify({'error': 'Invalid comment data'})

if __name__ == '__main__':
    app.run()
