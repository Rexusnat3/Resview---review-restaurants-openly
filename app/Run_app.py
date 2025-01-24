import Initialization

app = Initialization.create_app()

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for development
