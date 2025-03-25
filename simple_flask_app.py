# EX-11

import os
from flask import Flask


app = Flask(__name__)

@app.route("/content")
def content():
    my_file = open("C:/Users/master/Desktop/words.txt", "r")
    read_content = my_file.read()
    return read_content, 200

@app.route("/register")
def register():
    my_file = open("C:/Users/master/Desktop/hello.txt", "w")
    write_content = my_file.write("hello")
    return "Success!", 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=30000, debug=True)
