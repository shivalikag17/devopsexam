from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to ITIL exam."

@app.route('/modules', methods=['GET'])
def get_modules():
    modules_list = ["Fundamental of Computer Networks", "Concepts of Operating System and Administration", "Security Concepts", "Compliance Audit", "Network Defense and Countermeasures (NDC)", "Cyber Forensics", "Public Key Infrastructure", "IT Infrastructure Management & DevOps"]
    return jsonify(modules_list)
@app.route('/me', methods=['GET'])
def get_me():
    me_list = ["PRN=230344223047", "Name=Shivalika Gupta", "Phone number= 9109692039"]
    return jsonify(me_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
