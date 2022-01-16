from recreation import create_app

app = create_app()



if __name__ == '__main__':
    #run app on port 55402
    app.run(port=55402, debug=True)
    #accessing app via built-in developer server
    #app.run(host='0.0.0.0', port=8000, debug=True)
