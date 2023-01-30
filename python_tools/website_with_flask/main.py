from flask import Flask

# Add instance
app = Flask(__name__)


# Create home page
@app.route('/')
# Add home page logic
def home():
    return "Welcome to my website!"


# Start the app
app.run()
