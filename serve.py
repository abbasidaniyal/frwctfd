from CTFd import create_app

app = create_app()
app.run(debug=True, threaded=True, host="192.168.29.211", port=4000)
