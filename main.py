from website import create_app

app = create_app()

# Only run the web server if this file is ran not when you import the file
if __name__ == '__main__': 
  app.run(debug=True)