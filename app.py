from flask import render_template, Flask, request
import boto3
import json
account_id = "AKIAUTP2CT7AAYERIVHJ"
account_key = "Ao4B8MS7KUu0lVWHaAR7n4/VAZJVItwkAn1v4tXA"
def client():
    global account_id
    global account_key
    global account_token
    print(account_id, account_key)
    client = boto3.client("textract", aws_access_key_id=account_id,
                          aws_secret_access_key=account_key,
                          region_name='us-east-1')
    return client
app = Flask(__name__)

@ app.route("/", methods=["GET"])
def main():
    extractedText = ""
    responseJson = {

        "text": extractedText
    }
    return render_template("index.html", jsonData=json.dumps(responseJson))


@ app.route("/extracttext", methods=["POST"])
def extractImage():
    file = request.files.get("filename")
    binaryFile = file.read()
    textractclient = client()
    response = textractclient.detect_document_text(
        Document={
            'Bytes': binaryFile
        }
    )
    extractedText = ""
    for block in response['Blocks']:
        if block["BlockType"] == "LINE":
            extractedText = extractedText+block["Text"]+" "
    responseJson = {

        "text": extractedText
    }
    print(responseJson)
    return render_template("index.html", jsonData=json.dumps(responseJson))


@ app.route("/extracttext", methods=["POST"])
def extractImagenew():
    file = request.files.get("filename")
    binaryFile = file.read()
    textractclient = client()
    response = textractclient.detect_document_text(
        Document={
            'Bytes': binaryFile
        }
    )
    extractedText = ""
    for block in response['Blocks']:
        if block["BlockType"] == "LINE":
            extractedText = extractedText+block["Text"]+" "
    responseJson = {

        "text": extractedText
    }
    print(responseJson)
    return render_template("index.html", jsonData=json.dumps(responseJson))
@ app.route("/translatedocument", methods=["POST"])
def extractDocument():
    file = request.files.get("filenameDocument")
    binaryFile = file.read()
    textractclient = client()
    response = textractclient.detect_document_text(
        Document={
            'Bytes': binaryFile
        }
    )
    extractedText = ""
    for block in response['Blocks']:
        if block["BlockType"] == "LINE":
            extractedText = extractedText+block["Text"]+" "
    responseJson = {

        "text": extractedText
    }
    print(responseJson)
    return render_template("index.html", jsonData=json.dumps(responseJson))
if __name__ == '__main__':
    app.run()