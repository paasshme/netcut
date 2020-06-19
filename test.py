from flask import Flask, jsonify


app = Flask(__name__)
apiPath = '/api/'

@app.route('/')
@app.route(f'{apiPath}')
def test():
	return "Page de base"
	
@app.route(f'{apiPath}getIp')
def get_all_connected_devices():
    devices=[]

    for k in range (0,10):
        devices.append({'ip': f'192.168.0.{k*15%255}','mac':f'AA:BB:CC:DD:EE:{k}{k}'})
    
    return jsonify(devices)

@app.route(f'{apiPath}<string:ip>/<int:nb>')
def cut_ip(ip,nb):
    return f'Ok for {ip}, {nb} times'

@app.route(f'{apiPath}<string:ip>/<string:hw>/<int:nb>')
def cut_ip_mac(ip,hw,nb):
    return f'Ok for {ip} linked with {hw}, {nb} times'



if __name__ == '__main__':
    app.run(debug=True)
