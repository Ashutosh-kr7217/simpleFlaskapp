from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
        <head>
            <style>
                body {
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin: 0;
                    background: linear-gradient(45deg, #ff7e5f, #feb47b, #86a8e7, #91eae4); /* Gradient background */
                }
                h1 {
                    font-family: 'Comic Sans MS', cursive, sans-serif; /* Cartoon-like font */
                    font-size: 4em; /* Larger text */
                    color: #fff; /* White text color */
                    text-shadow: 2px 2px 0 #000, /* Adds a black shadow for cartoon effect */
                                 4px 4px 0 #00f, /* Blue offset shadow for depth */
                                 6px 6px 0 #0ff; /* Cyan offset shadow for depth */
                    padding: 20px;
                    border: 5px solid #fff; /* Border around the text */
                    background-color: rgba(0, 0, 0, 0.2); /* Slight black background behind text */
                    border-radius: 20px; /* Rounded corners */
                }
            </style>
        </head>
        <body>
            <center>
                <h1>Flask App Deployment!</h1>
            </center>
        </body>
    </html>
    '''

if __name__ == "__main__":
    app.run()
