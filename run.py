"""Run and start the App"""

from project.app import create_app

# Create the Flask app using the factory function from project/app.py
app = create_app()

if __name__ == "__main__":
    # Run the Flask app in debug mode on port 5000
    app.run(debug=True)