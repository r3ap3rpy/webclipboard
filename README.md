### The webclipboard can be operated via the flask module

The basic idea is to be able to provide a clipboard outside the computer which can be used via a password and username combination!

If you use the GET request with basic HTTP authentication you get the content of the clipboard defined by the username and password combination, of you use the POST request with username and password defined in the payload, you can store stuff in the clipboard which will expire in 5 minutes and the only one getting a response will be the one who knows your username and password you specified!
