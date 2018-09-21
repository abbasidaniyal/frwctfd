from CTFd import create_app

app = create_app()
app.run(debug=True, threaded=True, host="192.168.0.104", port=4000)
